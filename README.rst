======================
ds-project-template
======================

Cookiecutter_ template for a Python Data Science Project.

* GitHub repo: https://github.com/kazimsanlav/ds-project-template
* Free software: BSD license

Features
--------
* Full stack data science project coverage
* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.5, 3.6, 3.7, 3.8
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Project Structure
-----------------

.. code-block:: sql

    .
    ├── AUTHORS.rst
    ├── CONTRIBUTING.rst
    ├── HISTORY.rst
    ├── LICENSE
    ├── MANIFEST.in
    ├── Makefile -------------------- convenient utilities, :code:`$ make` for help  
    ├── README.rst
    ├── cache ----------------------- .pkl files
    ├── configs --------------------- config files
    │   ├── config.yaml
    │   └── logging.yaml
    ├── data ------------------------ data
    │   ├── final
    │   └── raw
    ├── docs ------------------------ docs can be created with :code:`$ make docs`
    ├── jobs ------------------------ .sh files for cron jobs
    ├── logs ------------------------ logs files
    ├── models ---------------------- models ready to use
    ├── notebooks ------------------- notebooks goes here, suggested naming: *01-kzm-InitalEDA.ipynb*
    │   ├── adhoc
    │   └── utils
    ├── requirements.txt ------------ project requirements
    ├── requirements_dev.txt -------- dev requirements
    ├── settings.py
    ├── setup.cfg
    ├── setup.py -------------------- make this package pip installable  
    ├── tests
    ├── tox.ini
    ├── .env ------------------------ storing env variables
    └── {project_slug} -------------- python package to distribute / import
        ├── __init__.py
        ├── cli.py
        ├── config.py --------------- read configs / load dot-env file
        ├── helpers.py
        └── {project_slug}.py


Quickstart
-----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python Data Science Project::

    cookiecutter https://github.com/kazimsanlav/ds-project-template.git

Then:

* Create a repo and put it there.
* *(optional)* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* *(optional)* Register_ your project with PyPI.
* *(optional)* Run the Travis CLI command ``travis encrypt --add deploy.password`` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* *(optional)* Add the repo to your `Read the Docs`_ account + turn on the Read the Docs service hook.
* *(optional)* Release your package by pushing a new tag to master.
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* *(optional)* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html


Credits
-------

This package is forked from `audreyr/cookiecutter-pypackage`_ 

.. _`kazimsanlav/ds-project-template`: https://github.com/kazimsanlav/ds-project-template
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _Punch: https://github.com/lgiordani/punch
.. _Poetry: https://python-poetry.org/
.. _PyPi: https://pypi.python.org/pypi
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
