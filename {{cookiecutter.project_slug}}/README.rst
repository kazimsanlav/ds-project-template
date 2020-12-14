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

| {{ cookiecutter.project_slug }}
| ├── cache       -> .pkl files
| ├── data        -> all data goes here
| │   ├── final   -> read to fit a model
| │   └── raw     -> coming from db
| ├── docs        -> can be created with :code:`$ make docs`
| ├── jobs        -> .sh files for cron jobs
| ├── keys        -> secret keys (slack, db keys etc.)
| ├── logs        -> log files
| ├── models      -> model binaries / coefs
| ├── notebooks   -> notebooks goes here, suggested naming: *01-kzm-InitalEDA.ipynb*
| │   ├── adhoc   -> just to get a quick result
| │   └── utils   -> used frequently, for a specific need
| ├── src         -> all the source code goes here
| │   └── {{ cookiecutter.project_slug }} -> python package to distribute / import 
| ├── tests       -> tests for the package
| ├── requirements_dev.txt -> development packages (for testing, formating etc.)
| ├── settings.py -> settings for the project
| ├── setup.py    -> to make this package pip installable. 
| ├── Makefile    -> convenient utilitis, :code:`$ make` for help
| ├── .env        -> env variables
| ├── .gitignore  -> to exclude files/folders from version control 
| └── README.rst  -> project Readme file


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