# Structural Imbalance Jupyter Notebook

This notebook explains the quantum processing unit (QPU) programming model used for
calculating structural imbalance in signed social networks, and shows how to implement
it.

The notebook has the following sections:

1. **What is Structural Imbalance?** defines and explains the structural imbalance
   problem.
2. **Formulating the Problem** shows how such optimization problems can be
   formulated for solution on a quantum computer.
3. **A Toy Example** codes a small structural imbalance problem to demonstrate the
   solution technique.
4. **A Real-World Example** applies the solution to the data sets of the Stanford
   Militants Mapping Project.

## What is Structural Imbalance?

*Social networks* map relationships between people or organizations onto graphs,
with the people/organizations as nodes and relationships as edges; for example,
friends form a social network. *Signed social networks* map both friendly
and hostile relationships by assigning to edges either positive or negative values.
Such networks are said to be *structurally balanced* when they can be cleanly
divided into two sets, with each set containing only friends, and all relations
between these sets are hostile. The measure of *structural imbalance* or
*frustration* for a signed social network, when it cannot be cleanly divided, is
the minimum number of edges that violate the social rule, “the enemy of my friend
is my enemy."

Finding a division that minimizes frustration is an NP-hard graph problem (it can
be viewed as an expansion of the well-known
[maximum cut](https://en.wikipedia.org/wiki/Maximum_cut) problem). This is an
example of a broad class of optimization problems well-suited to solution on
D-Wave systems. Other
[examples](https://docs.dwavesys.com/docs/latest/c_handbook_2.html) include protein
folding, traffic flow optimization, job-shop scheduling, and many more.

![imbalance](images/Romeo.png)

## Installation

You can run this example
[in the Leap IDE](https://ide.dwavesys.io/#https://github.com/dwave-examples/structural-imbalance-notebook).

Alternatively, install requirements locally (ideally, in a virtual environment):

    pip install -r requirements.txt

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
