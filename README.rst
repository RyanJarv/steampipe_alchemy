=================
steampipe-alchemy
=================


.. image:: https://img.shields.io/pypi/v/steampipe_alchemy.svg
        :target: https://pypi.python.org/pypi/steampipe_alchemy

.. image:: https://img.shields.io/travis/RyanJarv/steampipe_alchemy.svg
        :target: https://travis-ci.com/RyanJarv/steampipe_alchemy

.. image:: https://readthedocs.org/projects/steampipe-alchemy/badge/?version=latest
        :target: https://steampipe-alchemy.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Python Boilerplate contains all the boilerplate you need to create a Python package.


* Free software: BSD license
* Documentation: https://steampipe-alchemy.readthedocs.io.


Features
--------

.. code-block:: python

    from steampipe_alchemy import query
    from steampipe_alchemy.models import AwsS3Bucket
    
    for b in query(AwsS3Bucket).limit(3):
        print(b.name)
        print("  Region: " + b.region)
        print("  Owner: " + str(b.acl['Owner']['DisplayName']))


Will produce the following output:

.. code-block::

    example-bucket-1234
      Region: us-east-1
      Owner: example-prod-account
    example-bucket-2345
      Region: us-east-2
      Owner: example-prod-account
    example-bucket-3456
      Region: us-west-1
      Owner: example-prod-account

Models are located in `steampipe_alchemy.models` and are automatically generated with `./scripts/generate_models.py`.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
