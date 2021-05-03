=================
steampipe-alchemy
=================


.. image:: https://img.shields.io/pypi/v/steampipe_alchemy.svg
        :target: https://pypi.python.org/pypi/steampipe_alchemy

.. image:: https://github.com/RyanJarv/steampipe_alchemy/actions/workflows/main_tests.yml/badge.svg
        :target: https://github.com/RyanJarv/steampipe_alchemy/actions/workflows/main_tests.yml

.. image:: https://github.com/RyanJarv/steampipe_alchemy/actions/workflows/publish.yml/badge.svg
        :target: https://github.com/RyanJarv/steampipe_alchemy/actions/workflows/publish.yml

.. image:: https://readthedocs.org/projects/steampipe-alchemy/badge/?version=latest
        :target: https://steampipe-alchemy.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A simple `SQLAlchemy <https://www.sqlalchemy.org/>`_ wrapper around `Steampipe <https://steampipe.io/>`_.

Currently this is a work in progress. Models exist for the AWS plugin, others will be added in the future.

* Free software: BSD license
* Documentation: [WIP] https://steampipe-alchemy.readthedocs.io.


Features
--------

Install, setup, and start steampipe with the aws plugin.

.. code-block:: python

    # We're assuming the the AWS credentials are set in the environment here.
    from steampipe_alchemy as sa

    sa.install(['aws'])  # Downloads and installs steampipe with the aws plugin.
    sa.update_config(aws={ #  Modifies ~/.local/share/steampipe_alchemy/config/aws.spc
        "plugin": "aws",
        "regions": ['us-east-1', 'us-west-1', 'us-west-2']
    })
    sa.start()  # Steampipe will be stopped when the script exits or when stop() is called.

We can then use the SQLAlchemy models to query AWS.

.. code-block:: python

    from steampipe_alchemy import query
    from steampipe_alchemy.models import AwsVpc


    for i in query(AwsVpc).limit(2):
        print(i.vpc_id + ':')
        print('  CIDR: ' + i.cidr_block)
        print('  Region: ' + i.region)

Which will produce something like:

.. code-block:: python

    vpc-c65487a0
      CIDR: 172.31.0.0/16
      Region: us-west-1
    vpc-0a2a5413bab086b36
      CIDR: 172.31.0.0/16
      Region: us-east-2

The models also have to_json and to_dict mixins:

.. code-block:: python

    first_vpc = query(AwsVpc).first().to_dict()
    print(first_vpc['cidr_block'])


The function steampipe_alchemy.query is a small wrapper around sqlalchemy.orm.Query. It is setup to use the steampipe sqlalchemy session and has type annotations which enable IDE completion on both the Model results and the Query class.


.. image:: https://raw.githubusercontent.com/RyanJarv/steampipe_alchemy/main/docs/images/completion.png

Models are located in ``steampipe_alchemy.models`` and are automatically generated with ``./scripts/generate_models.py``.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
