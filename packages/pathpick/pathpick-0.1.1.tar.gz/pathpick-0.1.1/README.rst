
.. image:: https://readthedocs.org/projects/pathpick/badge/?version=latest
    :target: https://pathpick.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/pathpick-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/pathpick-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/pathpick-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/pathpick-project

.. image:: https://img.shields.io/pypi/v/pathpick.svg
    :target: https://pypi.python.org/pypi/pathpick

.. image:: https://img.shields.io/pypi/l/pathpick.svg
    :target: https://pypi.python.org/pypi/pathpick

.. image:: https://img.shields.io/pypi/pyversions/pathpick.svg
    :target: https://pypi.python.org/pypi/pathpick

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/pathpick-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/pathpick-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://pathpick.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://pathpick.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/pathpick-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/pathpick-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/pathpick-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/pathpick#files


Welcome to ``pathpick`` Documentation
==============================================================================
.. image:: https://pathpick.readthedocs.io/en/latest/_static/pathpick-logo.png
    :target: https://pathpick.readthedocs.io/en/latest/

``pathpick`` is a Python library that makes it easy to filter files and directories using familiar `glob-style patterns inspired by .gitignore <https://git-scm.com/docs/gitignore>`_. It supports both include and exclude rules, giving you fine-grained control over which paths are selected. Under the hood, it uses the powerful pathspec library and supports Git's WildMatchPattern syntax.

A path is included if it matches any of the include patterns and does not match any of the exclude patterns. If include patterns are empty, then include everything by default. If exclude patterns are empty, the we don't exclude anything. This logic is ideal for projects that involve scanning files, building file manifests, cleaning directories, or deploying selected content.


Usage Examples
------------------------------------------------------------------------------
First, read `this document <https://git-scm.com/docs/gitignore>`_ to get basic understanding about the include / exclude pattern syntax.

1. Include all Python files

.. code-block:: python

    from pathpick.api import PathPick

    pick = PathPick.new(include=["**/*.py"], exclude=[])

    pick.is_match("main.py")                # True
    pick.is_match("utils/helper.py")        # True
    pick.is_match("README.md")              # False

2. Include all files, but exclude logs and temporary files

.. code-block:: python

    pick = PathPick.new(
        include=["**/*"],
        exclude=["**/*.log", "**/*.tmp"]
    )

    pick.is_match("report.csv")             # True
    pick.is_match("debug.log")              # False
    pick.is_match("backup/data.tmp")        # False

3. Include files in specific folders

.. code-block:: python

    pick = PathPick.new(
        include=["src/**/*.py", "docs/**/*.md"],
        exclude=[]
    )

    pick.is_match("src/main.py")            # True
    pick.is_match("docs/intro.md")          # True
    pick.is_match("test/test_main.py")      # False

4. Exclude test files even if they match the include pattern

.. code-block:: python

    pick = PathPick.new(
        include=["**/*.py"],
        exclude=["**/test_*.py", "**/tests/*"]
    )

    pick.is_match("src/module.py")          # True
    pick.is_match("tests/test_module.py")   # False
    pick.is_match("src/test_utils.py")      # False


.. _install:

Install
------------------------------------------------------------------------------

``pathpick`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install pathpick

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade pathpick
