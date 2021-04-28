#!/usr/bin/env python
"""
Tests for `steampipe_alchemy` package that run on opened PR's.

Any testing that doesn't require access to any AWS credentials goes here.
"""

import pytest
import steampipe_alchemy

regions = ['us-east-1', 'us-east-2', 'us-west-2', 'us-west-1']


@pytest.fixture(scope='module')
def query():
    steampipe_alchemy.install(['aws'])
    steampipe_alchemy.update_config(aws={
        "plugin": "aws",
        "regions": regions,
    })
    steampipe_alchemy.start()


def test_query(query):
    print(query)
