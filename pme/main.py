import re
import sys


def process_includes(content):
    include_pattern = r'^include::(.+)$'
    processed_lines = []

    for line in content.splitlines():
        if re.match(include_pattern, line):
            include_path = line.strip().split('::')[1].strip()
            _included_content = read_content(include_path)
            if _included_content:
                processed_lines.extend(_included_content.splitlines())
            else:
                print(f"Error: File {include_path} not found.")
                continue
        else:
            processed_lines.append(line)
    return '\n'.join(processed_lines)


def read_content(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None


def replace_variables(content, _output_file):

    # Define a pattern to match the variable definitions
    var_pattern = r'----\n(.*?)----'
    var_definitions = re.search(var_pattern, content, flags=re.DOTALL).group(1)
    content = content.replace('----\n' + var_definitions + '----\n', '')
    var_dict = {}
    for line in var_definitions.split('\n'):
        if ':' in line:
            key, value = line.split(':')
            var_dict[key.strip()] = value.strip()

    # Replace variables in the content
    for placeholder, replacement in var_dict.items():
        content = re.sub('{{' + placeholder + '}}', replacement, content)

    # Write the modified content to the output file
    with open(_output_file, 'w') as file:
        file.write(content)


def main():
    if len(sys.argv) != 3:
        print("Usage: pme input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        original_content = read_content(input_file)
        # Checking if file is present for user-friendly error
        if not original_content:
            raise FileNotFoundError(f"File {input_file} not found")

        # Including all data before assigning variables
        included_content = process_includes(original_content)
        # Replacing the variables at the end
        replace_variables(included_content, output_file)


if __name__ == '__main__':
    main()
