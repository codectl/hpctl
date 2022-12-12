*****
hpctl
*****

.. image:: https://github.com/rena2damas/hpctl/actions/workflows/ci.yaml/badge.svg
    :target: https://github.com/rena2damas/hpctl/actions/workflows/ci.yaml
    :alt: CI
.. image:: https://codecov.io/gh/rena2damas/hpctl/branch/master/graph/badge.svg
    :target: https://app.codecov.io/gh/rena2damas/hpctl/branch/master
    :alt: codecov
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: code style: black
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: license: MIT

A CLI utility tool for interacting and managing an HPC computer cluster.

Setup 🔧
=====
The project uses `poetry <https://python-poetry.org/>`__ for dependency management
. Therefore to set up the project, one would do:

.. code-block:: bash

    # ensure poetry is installed
    $ poetry env use python3
    $ poetry install

That will configure a virtual environment for the project and install the respective
dependencies, which is particular useful during development stage.

Run 🚀
====
Since it is a CLI program, the list of available operations is given by running the command:

.. code-block:: bash

    $ hpctl
    > ...

Tests & linting 🚥
===============
Run tests with ``tox``:

.. code-block:: bash

    # ensure tox is installed
    $ tox

Run linter only:

.. code-block:: bash

    $ tox -e lint

Optionally, run coverage as well with:

.. code-block:: bash

    $ tox -e coverage

License
=======
MIT licensed. See `LICENSE <LICENSE>`__.
