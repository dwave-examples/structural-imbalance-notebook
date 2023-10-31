[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-examples/structural-imbalance-notebook?quickstart=1)
[![Linux/Mac/Windows build status](
  https://circleci.com/gh/dwave-examples/structural-imbalance-notebook.svg?style=shield)](
  https://circleci.com/gh/dwave-examples/structural-imbalance-notebook)

# Structural Imbalance 

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

You can run this example without installation in cloud-based IDEs that support 
the [Development Containers specification](https://containers.dev/supporting)
(aka "devcontainers").

For development environments that do not support ``devcontainers``, install 
requirements:

    pip install -r requirements.txt

If you are cloning the repo to your local system, working in a 
[virtual environment](https://docs.python.org/3/library/venv.html) is 
recommended.

## Usage

Your development environment should be configured to 
[access Leap’s Solvers](https://docs.ocean.dwavesys.com/en/stable/overview/sapi.html).
You can see information about supported IDEs and authorizing access to your 
Leap account [here](https://docs.dwavesys.com/docs/latest/doc_leap_dev_env.html).  

The notebook can be opened by clicking on the 
``01-structural-imbalance-overview.ipynb`` file in VS Code-based IDEs. 

To run a locally installed notebook:

```bash
jupyter notebook
```

## License

Released under the Apache License 2.0. See LICENSE file.
