# CodeCompiler: Compile and Copy Python Files

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-3.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Example](#example)

## Introduction

Welcome to **CodeCompiler**! 🎉

I created this tool while solving problems for my Django projects. The need to compile Python code and distribute it securely led to the birth of CodeCompiler. However, this tool isn't limited to Django projects alone; it can be applied to any Python project.

CodeCompiler compiles Python files to bytecode and copies them to a specified directory, excluding specific directories, and adjusts filenames to remove version-specific parts. It ensures that your source code remains secure and is not exposed when deployed or distributed.

## Features

- **Compile Python Files:** Converts `.py` files to `.pyc` bytecode files.
- **Directory Exclusion:** Exclude specified directories from the compilation process.
- **File Renaming:** Adjusts filenames to remove version-specific parts.
- **Secure Distribution:** Ideal for securely distributing Python applications.

## Example
I have provided and example django project which can be used to test this the structure of example project is as below:

```sh
example/
├── manage.py
├── app/
│   ├── __init__.py
│   └── views.py
└── ignoreDir/
    └── old_code.py
```

Here's an example structure after running the runner.py script:
```sh
target/
├── manage.pyc
├── app/
│   ├── __init__.pyc
│   └── views.pyc
```

