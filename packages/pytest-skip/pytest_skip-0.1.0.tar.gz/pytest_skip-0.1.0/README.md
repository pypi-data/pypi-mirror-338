pytest-skip
=============

This is a [pytest](https://pytest.org) plugin which allows to (de-)select or skip tests by name from a list loaded from a file.

pytest-skip expands upon the capabilities of the original [pytest-select](https://github.com/ulope/pytest-select) plugin
by adding
- `--skip-from-file` option to skip tests instead of deselecting
- support to (de-)select or skip parametrized tests without needing to specify test instance qualifiers
- support for blank and comment lines in the selection files
- better integration with the `pytest-xdist`, plugin warning and error messages are passed to the master node with proper stdout or stderr outputs


Usage
-----

This plugin adds new command line options to pytest:

- ``--select-from-file``
- ``--deselect-from-file``
- ``--skip-from-file``
- ``--select-fail-on-missing``

The first three expect an argument that resolves to a UTF-8 encoded text file containing one test name per
line. Text file may contain blank and comment lines (starts from `#`),

The fourth one changes the behaviour in case (de-)selected or skipped test names are missing from the to-be executed tests.
By default a warning is emitted and the remaining selected tests are executed as normal.
By using the ``--select-fail-on-missing`` flag this behaviour can be changed to instead abort execution in that case.

Test names are expected in the same format as seen in the output of
``pytest --collect-only --quiet`` for example.

Both plain test names or complete node ids (e.g. ``test_file.py::test_name``) are accepted.

Example::

    $~ cat selection.txt
    test_something
    test_parametrized[1]
    test_parametrized
    tests/test_foo.py::test_other

    $~ pytest --select-from-file selection.txt
    $~ pytest --deselect-from-file selection.txt
    $~ pytest --skip-from-file selection.txt


Install from source
-------------------

```bash
git clone --recursive https://github.com/vlad-penkin/pytest-skip
# Run this command from the pytest-skip directory after cloning the source code using the command above
pip install .
```

Install in development mode
---------------------------

To install plugin in development mode run::

```bash
pip install -e .
```

Questions
---------

Why not use pytest's builtin ``-k`` option
******************************************

The ``-k`` selection mechanism is (currently) unable to deal with selecting multiple parametrized
tests and is also a bit fragile since it matches more than just the test name.
Additionally, depending on the number of tests, giving test names on the command line can overflow
the maximum command length.

Version History
---------------

- ``v0.1.0`` - 4/4/2025:
    - Initial release
