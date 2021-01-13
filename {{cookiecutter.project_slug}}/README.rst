{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Project Structure
-----------------
.. example-code::
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
        └── {project_slug} -------------- python package to distribute / import
            ├── __init__.py
            ├── cli.py
            ├── config.py --------------- read configs / load dot-env file
            ├── helpers.py
            └── {project_slug}.py


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `kazimsanlav/ds-project-template`_ 
project template, forked from `audreyr/cookiecutter-pypackage`_ 

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`kazimsanlav/ds-project-template`: https://github.com/kazimsanlav/ds-project-template
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage