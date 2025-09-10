# Thread Programming in Python

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Build](https://img.shields.io/badge/build-manual-lightgrey)
[![PyPI - Python Version](https://img.shields.io/badge/doc-pydoc-yellow)](./doc/index.html)

This educational repository features a set of illustrative examples that demonstrate thread programming in Python. The learning objectives are:

- Demonstrate practical usage of key thread-related methods, including but not limited to:
  - Creating and running threads by using the [`thread`](https://python.readthedocs.io/en/v2.7.2/library/thread.html) module
  - Creating and running threads by using the [`threading`](https://docs.python.org/3.13/library/threading.html) module
- Serve as a reference for writing well-documented, multithreaded Python code.

This project is part of the **Concurrent Programming** module at the [Federal University of Rio Grande do Norte (UFRN)](https://www.ufrn.br), Natal, Brazil.

---

## 📂 Repository Structure

Each file in this repository demonstrates a different function for thread programming in Python. The files are organized according to the following structure:

```
.
├── doc/            # Documentation
├── src             # Source code
│   ├── __init__.py         # Source file to serve to [`pdoc`](https://pdoc.dev) to generate a landing page for the documentation
│   ├── thread.py           # Demonstration of thread creation relying on a callback function and the thread module
│   ├── threading-class.py  # Demonstration of thread creation based on a customized class
│   ├── threading-task.py   # Demonstration of thread creation relying on a callback function
└── README.md
```

---

## 🚀 Getting Started

### ✅ Prerequisites

For compiling and executing programs, the following elements must be properly installed on the development environment:

- [Python 3+](https://www.python.org)
- [pdoc](https://pdoc.dev), for automatic documentation generation

### ▶️ Running

To run a program, insert the following command in the operating system's terminal:

```bash
python3 src/threading-class.py
```

In this case, the demonstration program to be executed is the [`threading-class`](src/threading-class.py) example.

### 🗒️ Generating Documentation

The generation and visualization of documentation is provided by [`pdoc`](https://pdoc.dev). To render documentation as HTML pages, insert the following command in the operating system's terminal:

```bash
pdoc ./src -o ./doc
```

This will generate documentation for all source code files within the [`src`](src) directory into the [`doc`](doc) directory. It is also possible to render documentation live with the command

```bash
pdoc ./src
```

This command will result in opening a window in the browser running `pdoc` at a localhost server. In this case, the documentation pages will be automatically reloaded whenever changes are made to the source code.

---

## 🤝 Contributing

Contributions are welcome! Fork this repository and submit a pull request 🚀

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
