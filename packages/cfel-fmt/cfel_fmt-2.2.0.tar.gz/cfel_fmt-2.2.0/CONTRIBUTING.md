
# Guidelines for Contributors

The project is hosted at the [GitLab instance](https://git.xfel.eu) of European XFEL.
Contributions to the project are welcome.
Please feel free to submit a [merge request](https://docs.gitlab.com/ee/user/project/merge_requests/)
to <https://git.xfel.eu/dataAnalysis/cfel_fmt#>.

## Version Control

`cfel_fmt` is developed using the [Git](https://git-scm.com) version control system.

## Continuous Integration

Gitlab provides Continuous Integration (CI) and
automatically runs unit tests and package builds.

## Python

`cfel_fmt` is developed in [Python](https://www.python.org).

- From CFELPyUtils version 2.0 Python 2.7 is no longer supported.
- All code in the library must run with the currently supported
    versions of Python 3. At the time of this writing this is:
    - Python 3
        - 3.6
        - 3.7
        - 3.8
        - 3.9
- [Pylint](https://www.pylint.org) should be run on the code before
  submission, as stated in the Google Python Coding Style Guide. In
  the root folder of the CFELPyUtils repository, contributors can find
  a \'pylintrc\' file with the settings that should be applied when
  linting the code. Please see
  [here](http://pylint.pycqa.org/en/latest/user_guide/run.html?highlight=pylintrc)
  how to use the pylintrc file.
- The [Black](https://github.com/psf/black) Python code formatter
  should be run on the code before submission.
