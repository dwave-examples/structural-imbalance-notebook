# Structural Imbalance Jupyter Notebook

This notebook explains the quantum processing unit (QPU) programming model used for
calculating structural imbalance in signed social networks, and shows how to implement
it using D-Wave Ocean's stack of tools.

By the end of this notebook you will have experienced using Ocean's graphic tools
to submit a problem to the D-Wave system and be able to modify the code to experiment
with different data sets and parameters.

## Usage

To enable notebook extensions[^1]:

```bash
jupyter contrib nbextension install --sys-prefix
jupyter nbextension enable toc2/main
jupyter nbextension enable exercise/main
jupyter nbextension enable exercise2/main
jupyter nbextension enable python-markdown/main

```

To run the notebook:

```bash
jupyter notebook
```

[^1]: Leap's IDE, which runs VS Code, does not support all notebook extensions.
      Also, using the `matplotlib` package in interactive mode (with the
      `%matplotlib ipympl` code line) can degrade performance; it is recommended
      you switch that line to `%matplotlib inline` where noted in the notebook.

## License

Released under the Apache License 2.0. See LICENSE file.
