#!/usr/bin/env python

"""Tests for `steampipe_alchemy` package."""

import pytest

from steampipe_alchemy import query, start, install, update_config
from steampipe_alchemy.models import AwsVpc


@pytest.fixture
def setup():
    install(['aws'])
    update_config(aws={
        "plugin": "aws",
        "regions": ['us-east-1', 'us-east-2', 'us-west-2', 'us-west-1']
    })
    start()


def test_this(setup):
    print(query(AwsVpc))
