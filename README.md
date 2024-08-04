# PyMarkEditor

[![Me][user-badge]][user-url]

----

[![Python][python-badge]][python-url]

[![PyPI download month][pypi-badge]][pypi-url]

[![GitHub issues][git-issues]][git-issues-url]
[![GitHub branches][git-branches]][git-url]
[![GitHub Maintenance][git-maintenance]][git-activity-url]

----
## 📝 Table of Contents
1. [🔍 What is this repository about?](#-what-is-this-repository-about)
2. [❓ Why?](#-why)
3. [💻 Installing](#-installing)
4. [📑 Examples](#-examples)
   1. [Variables](#how-to-include-variables)
   2. [Files](#how-to-include-files)
____


## 🔍 What is this repository about?
PyMarkEditor (PME) is a Python package that enhances Markdown syntax by introducing new features. It does not use any external functionality nor add new filetypes, only creating new possibilities on existing .md. Interestingly, you can even use it with any .txt file or any other file type.

Here’s how PME works: Given a template file, PME identifies default patterns and transforms the content into a new file. It’s a straightforward tool that adds versatility to your Markdown documents.

## 🤔 Why?
Markdown boasts an elegant syntax, but its reusability leaves much to be desired. Picture this scenario: You’re writing numerous similar text blocks (like User Stories), only to discover that a crucial letter “a” is missing across all your lines. Heartbreaking, isn’t it?

This library exists mainly to give answer to those questions:
1. How to add variables to markdown?
    > PME allows you to add variables into markdown with ease. Define placeholders, and PME dynamically replaces them, ensuring consistency without manual edits.
2. How to include different files in one markdown file?
    > PME can include content of any text file into your Markdown, ensuring that it will be easy to maintain with time. Forget about endless scrolling 


## 🐒 Installing

Installation is simple:
```
pip install PyMarkEditor
```

## 📑 Examples
Pre-requirements: one template file (you can name it whatever you like; for now, let’s call it `readme_template.md`).

To use PME, follow this syntax:
```
pme <input_file> <output_file>
```

For instance, if you have a file named `readme_template.md` and want to create `README.md`, execute the following command:
```
pme readme_template.md README.md
```

### How to include variables?

You must create a block of variables at the beginning of your document using four hyphens (`----`). Each variable starts on a new line

```markdown
----
variable_name: any text with `any` format of any length
second_variable: any text with `any` format of any length
----
```

To use these variables throughout your document, enclose them in double curly braces (`{{variable_name}}`). Remember to add spaces before and after the variable:

```markdown
You can put {{variable_name}} anywhere
```

### How to include files?

To seamlessly include files within your Markdown document, follow this syntax:

```markdown
include::path/to/file/file_to_include.md
```
You can find more examples [here](example)



[user-badge]: https://img.shields.io/badge/Palibrix-DD9623?style=plastic
[user-url]: https://github.com/Palibrix


[python-badge]: http://ForTheBadge.com/images/badges/made-with-python.svg
[python-url]: https://www.python.org/

[pypi-badge]: https://img.shields.io/pypi/dm/PyMarkEditor
[pypi-url]: https://pypi.python.org/pypi/PyMarkEditor/

[git-activity-url]: https://GitHub.com/Palibrix/PyMarkEditor/graphs/commit-activity
[git-branches]: https://badgen.net/github/branches/Palibrix/PyMarkEditor
[git-issues-url]: https://github.com/Palibrix/PyMarkEditor/
[git-issues]: https://img.shields.io/github/issues/Palibrix/PyMarkEditor
[git-maintenance]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
[git-url]: https://github.com/Palibrix/PyMarkEditor/