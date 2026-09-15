# Thread Programming in Python

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3)](https://www.python.org)
![Build](https://img.shields.io/badge/build-manual-lightgrey)
[![Documentation](https://img.shields.io/badge/docs-pdoc-yellow)](./doc/index.html)

This educational repository contains small, runnable examples of thread programming in Python. The examples illustrate two APIs:

- [`_thread`](https://docs.python.org/3/library/_thread.html), Python's low-level thread API
- [`threading`](https://docs.python.org/3/library/threading.html), the higher-level API recommended for most applications

This project is part of the **Concurrent Programming** module at the [Federal University of Rio Grande do Norte (UFRN)](https://www.ufrn.br), Natal, Brazil.

## 📂 Repository Structure

Each source file focuses on a different way to create and coordinate threads:

| Example | Demonstrates |
| --- | --- |
| [`thread.py`](src/thread.py) | Low-level `_thread.start_new_thread()` with a callback function |
| [`threading-class.py`](src/threading-class.py) | A custom `Thread` subclass that overrides `run()` |
| [`threading-task.py`](src/threading-task.py) | `Thread(target=..., args=...)` for running callback functions |

The repository is organized as follows:

```plain
.
├── doc/                    # Generated HTML documentation
├── src/                    # Example source code
│   ├── __init__.py         # Package entry point used by pdoc
│   ├── thread.py           # Low-level _thread callback example
│   ├── threading-class.py  # Custom Thread subclass example
│   └── threading-task.py   # Thread callback example
└── README.md               # Project documentation
```

## 🚀 Getting Started

### ✅ Prerequisites

The following are required:

- [Python 3+](https://www.python.org)

Install [pdoc](https://pdoc.dev) only if you want to regenerate the HTML documentation:

```bash
python3 -m pip install pdoc
```

### ▶️ Running

Run any example from the repository root:

```bash
python3 src/thread.py
python3 src/threading-class.py
python3 src/threading-task.py
```

The output order of messages from different threads is not guaranteed because it depends on the operating system scheduler. In `thread.py`, the low-level API does not provide a `join()` call in the example, so the final message is not a reliable indicatior of the order in which worker messages will appear. The other two examples call `join()` and wait for all workers before printing their final message.

For example, `threading-class.py` prints messages similar to:

```text
Thread T1 suspending for 3 seconds
Thread T2 suspending for 1 seconds
Thread T2 finished
Thread T1 finished
All threads finished execution
```

### 🗒️ Generating Documentation

The generated documentation is provided by [`pdoc`](https://pdoc.dev). From the repository root, render documentation as HTML with:

```bash
pdoc ./src -o ./doc
```

This generates documentation for the source files in [`src`](src) under [`doc`](doc). To preview the documentation with a local server and reload it as source files change, run:

```bash
pdoc ./src
```

Then open the localhost URL printed by `pdoc` in a browser. The generated landing page is also available at [`doc/index.html`](doc/index.html).

## 🤝 Contributing

Contributions are welcome! Fork this repository and submit a pull request 🚀

