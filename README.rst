=================
steampipe-alchemy
=================


.. image:: https://img.shields.io/pypi/v/steampipe_alchemy.svg
        :target: https://pypi.python.org/pypi/steampipe_alchemy

.. image:: https://github.com/RyanJarv/steampipe_alchemy/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/RyanJarv/steampipe_alchemy/actions/workflows/tests.yml

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
    from steampipe_alchemy.models import AwsS3Bucket

    for b in query(AwsS3Bucket).limit(3):
        print(b.name)
        print("  Region: " + b.region)
        print("  Owner: " + str(b.acl['Owner']['DisplayName']))


Which will produce something like:

.. code-block:: python

    example-bucket-1234
      Region: us-east-1
      Owner: example-prod-account
    example-bucket-2345
      Region: us-west-1
      Owner: example-prod-account
    example-bucket-3456
      Region: us-west-2
      Owner: example-prod-account


The function steampipe_alchemy.query is a small wrapper around sqlalchemy.orm.Query. It is setup to use the steampipe sqlalchemy session and has type annotations which enable IDE completion on both the Model results and the Query class.


.. image:: https://raw.githubusercontent.com/RyanJarv/steampipe_alchemy/main/docs/images/completion.png

Models are located in ``steampipe_alchemy.models`` and are automatically generated with ``./scripts/generate_models.py``.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
