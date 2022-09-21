# Programming with threads in Python #

## About

This repository contains a set of examples to demonstrate thread programming with Python.

## Repository structure

Each file in this repository contains a different demonstration for thread programming with Python. The files are organized according to the following structure:

```
+─python-threads-examples      ---> Project directory
  ├─── doc                     ---> Directory where documentation will be generated
  └─── src                     ---> Directory with source code files
       └─── __init__.py        ---> Source file to serve to pdoc to generate a landing page for the documentation
       └─── thread.py          ---> Demonstrating creation of threads relying on a callback function and the thread module
       └─── threading-class.py ---> Demonstrating creation of threads based on a customer class
       └─── threading-task.py  ---> Demonstrating creation of threads relying on a callback function and the threading module
```

## Requirements

For compiling and executing programs, the following elements must be properly installed on the development environment:

- [Git](https://git-scm.com), as control version system
- [Python 3+](https://www.python.org)
- [pdoc](https://pdoc.dev), for automatic documentation generation

## Download, compilation, and execution

In the operating system’s terminal, insert the following commands to download the implementation from this Git repository and navigate to the resulting directory:

```bash
 # Download from the Git repository
 git clone https://github.com/ufrn-concprog/python-threads-examples
 
 # Navigation to the directory
 cd python-threads-examples
```

To run a program, insert the following command in the operating system's terminal:

```bash
python3 src/threading-class.py
```

In this case, the demonstration program to be executed is the [`threading-class`](src/threading-class.py) example.

## Automatic generation

The generation and visualization of documentation is provided by [pdoc](https://pdoc.dev). To render documentation as HTML pages, insert the following command in the operating system's terminal:

```bash
pdoc ./src -o ./doc
```

This will generate the documentation for all source code files within [`src`](src) into the [`doc`](doc) directory. It is also possible to render documentation live with the command

```bash
pdoc ./src
```

will open a window in the browser running `pdoc` at a localhost server. In this case, the documentation pages will be automatically reloaded upon changes in the source code.