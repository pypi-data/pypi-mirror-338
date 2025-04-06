## Python Inline Source 3: Syntax Highlighting Using Type Annotations

> The original [Python Inline Source](https://github.com/JuroOravec/python-inline-source-2) by @JuroOravec

> The PyPI package and VSCode extension have been migrated to:
> - PyPI: [sourcetypes3](https://pypi.org/project/sourcetypes3/)
> - VSCode: [chrx.python-inline-3](https://marketplace.visualstudio.com/items?itemName=chrx.python-inline-3)

This project enables inline syntax highligting of strings in python source files for 
multiple languages using type annotations.

Supports `html`, `css`, `javascript`, `typescript`, `sql`, `graphql`, 
multiple *css extension languages*, *template languages* and many more, 
[see below](#supported-languages) for a full list.

Uses [typing.Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)
to annotate the `str` type with the language used. You can use 
[typing.get_type_hints](https://docs.python.org/3/library/typing.html#typing.get_type_hints) 
at runtime to determine the language that a string has been annotated with.

- [sourcetypes](https://github.com/chrxer/python-inline-source-3/tree/main/sourcetypes) Python Types Package.
- [vscode-python-inline-source](https://github.com/chrxer/python-inline-source-3/tree/main/vscode-python-inline-source) VS Code Plugin.

## Installation

### Python package:

```bash
pip install sourcetypes3
```

### VS Code plugin:

Install `chrx.python-inline-3` from extensions (`ctrl + shift + x` or `cmd + shift + x` 
on mac).

## Example

[![Example](https://raw.githubusercontent.com/chrxer/python-inline-source-3/main/docs/examples.png)](https://github.com/chrxer/python-inline-source-3/blob/main/docs/examples.py)

## Usage

Use a type decoration named for language that you are using:

```python
import sourcetypes

my_html_string: sourcetypes.html = """
  <h1>Some HTML</h1>
"""
```

or:

```python
from sourcetypes import html

my_html_string: html = """
  <h1>Some HTML</h1>
"""
```

## Supported Languages

- `markdown` (aliased as `md`)
- `html`
- `django_html` (aliased as `django`)
- `django_txt`
- `jinja`
- `jinja_html`
- `css` (aliased as `style`, and `styles`)
- `scss`
- `less`
- `sass`
- `stylus`
- `javascript` (aliased as `js`)
- `jsx` (aliased as `javascriptreact`, and `react`)
- `typescript` (aliased as `ts`)
- `tsx` (aliased as `typescriptreact`)
- `coffeescript` (aliased as `coffee`)
- `sql`
- `json`
- `yaml`
- `graphql`
- `xml`
- `python` (aliased as `py`)
- `cpp` (aliased as `c`, `cc`, `h`, `hh`, and `hpp`)
- `golang` (aliased as `go`)
- `rust` (aliased as `rs`)
- `scm` (aliased as `tree_sitter`, and `trs`)

# Release Notes

#### [0.0.9] - 2025-03-28
- add Rust
- add tree-sitter (e.g. scm)

#### [0.0.8] - 2025-03-27
- add C++ & golang

#### [0.0.7] - 2025-03-27
- allow `\s*` around `=`

#### [0.0.6] - 2025-03-27
- forked from v0.0.5

## Building
see [BUILDING.md](https://github.com/chrxer/python-inline-source-3/blob/main/BUILDING.md)

### TODO

- allow _newline continuations_ // [Explicit line joining](https://docs.python.org/3/reference/lexical_analysis.html#explicit-line-joining)
