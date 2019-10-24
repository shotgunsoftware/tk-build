[![Python 2.7 3.7](https://img.shields.io/badge/python-2.7%20%7C%203.7-blue.svg)](https://www.python.org/)
[![codecov](https://codecov.io/gh/shotgunsoftware/tk-toolchain/branch/master/graph/badge.svg)](https://codecov.io/gh/shotgunsoftware/tk-toolchain)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# Toolkit Build tools

The Toolkit Build tools will help developers of Toolkit-based applications in their day to day development tasks. It is meant
to be installed as a pip package and can be used both locally or on a continuous integration service to validate their code
and documentation.

# What can it do?

Here are the tools that the library offers:

`pytest_tank_test`: This is a `pytest` plugin that allows to easily run Toolkit tests written with `tk-core`'s `TankTestBase`
regardless of the repository. It also provides a collection of environment variables and a test engine to help application
developers to write tests.

`tk_docs_preview`: This tool allows to preview the documentation in the `docs` folder of a Toolkit application.

# Pre-requisites

These tools assume that all your Toolkit-based repositories are in the same folder. For example:

```
/home/yourlogin/git-repos/tk-core
/home/yourlogin/git-repos/tk-multi-publish2
/home/yourlogin/git-repos/tk-framework-shotgunutils
...
```

This allows the tools to quickly find other repositories they might need to run.

# How can I run these tools?

First, you need to install them. Simply type `python -m pip install https://github.com/shotgunsoftware/tk-toolchain.git` and all the required modules will be installed for you.

Then, type `pytest` to run the unit tests inside a Toolkit repository or `tk-docs-preview` to preview the documentation in the `docs` folder of your Toolkit application's repository.

# `pytest_tank_test`

This `pytest` plugins offers a collection of services that will help a Toolkit developer to write tests and run them with `pytest`. It removes the need for custom shell scripts that use the `run_tests.sh/run_tests.bat` scripts from `tk-core` and of it's test runner.

The plugin offers the following services:

##### Adds the Toolkit core to the `PYTHONPATH`

The Toolkit core will be added at the front of the `PYTHONPATH`, assuming it is installed a sibling folder to your current reposiroty as explained [above](#pre-requisites).

##### Exposes the common folder for all your repositories

The folder in which all your repositories have been cloned will be exposed via the `SHOTGUN_REPOS_ROOT` environment variable. In the [above](#pre-requisites) example, the common folder for all the repositories is `/home/yourlogin/git-repos`.

This can be used to quickly reference any Toolkit bundle that your configuration will require during testing. For example:

```yaml
tk-framework-qtwidgets_v2.x.x:
    location:
        type: dev
        path: $SHOTGUN_REPOS_ROOT/tk-framework-qtwidgets
tk-framework-shotgunutils_v5.x.x:
    location:
        type: dev
        path: $SHOTGUN_REPOS_ROOT/tk-framework-shotgunutils
```

This would allow your tests to run wherever the repositories have been cloned, as long as they are next to each other
on your filesystem.

##### Adds any python modules for your tests into the `PYTHONPATH`

If your repository contains a folder named `tests/python`, it will be added at the front of the `PYTHONPATH`. This
allows your tests modules to share common building blocks.

##### Configures a Toolkit log file for your tests

The Toolkit log for your tests will be written out in the standard Toolkit log file location under the name `tk-test.log`. Unless `SHOTGUN_HOME` [has been set](http://developer.shotgunsoftware.com/tk-core/utils.html?highlight=logmanager#sgtk.util.LocalFileStorageManager), the logs will be found under

| Platform | Location                                     |
| -------- | -------------------------------------------- |
| macOs    | `~/Library/Logs/Shotgun/tk-test.log`         |
| Windows  | `%APPDATA%\Roaming\Shotgun\Logs\tk-test.log` |
| Linux    | `~/.shotgun/logs/tk-test.log`                |

##### Provides a test engine

A bare-bones implementation of a Toolkit engine is provided and can be referenced in your configurations via the `SHOTGUN_TEST_ENGINE` environment variable. This can replace the need to use a fully-featured engine like `tk-shell` or `tk-maya` to run your tests. `sgtk.platform.qt` and `sgtk.platform.qt5` will be initialized as expected.

You can refer to this engine in the configuration file for your tests like this:

```yaml
tk-testengine:
    location:
        type: dev
        path: $SHOTGUN_TEST_ENGINE
```

# `tk-docs-preview`

This tools allows to build the documentation for a Toolkit of the Python API repository. Just like the `pytest` plugin, it [assumes](#pre-requisites) the folder structure on disk to make it as simple as typing `tk-docs-preview` on the command line to build the documentation and get a preview in the browser.

Here's the `--help` output.

```
Usage: tk-docs-preview OPTIONS (run with --help for more options)

This tool previews sphinx documentation for a Toolkit bundle or the Shotgun
Python API. It script generates sphinx doc for a repository you have locally
on disk. This is useful for in-progress doc generation and when you want a
quick turnaround.

Options:
  -h, --help            show this help message and exit
  -v, --verbose         Enable verbose logging
  -c CORE, --core=CORE  Path to Toolkit Core. Only needed for apps, engines
                        and frameworks. Defaults to the folder next to the
                        current repository.
  -b BUNDLE, --bundle=BUNDLE
                        Path to the app/engine/fw you want to process.
                        Defaults to the current repository location.

Examples:

Shotgun API:       tk-docs-preview --bundle=/path/to/shotgun/python-api
Toolkit Core API:  tk-docs-preview --bundle=/path/to/tk-core
Toolkit Framework: tk-docs-preview --bundle=/path/to/tk-framework-xyz --core=/path/to/tk-core

For all of these examples, if your folder hierarchy is similar to

    /home/you/gitrepos/tk-core
    /home/you/gitrepos/python-api
    /home/you/gitrepos/tk-multi-toolkitapp

then the tool will find all the required folders on it's own and you will only need
to type "tk-docs-preview" to preview the documentation
```
