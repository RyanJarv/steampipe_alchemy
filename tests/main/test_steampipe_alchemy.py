#!/usr/bin/env python
"""
Tests for `steampipe_alchemy` package.

For testing we grab lists of values via boto3 and compare that to what we get from steampipe-alchemy. This requires AWS
credentials to be set in the environment, because of this these tests only run when merged.

The credentials used for https://github.com/RyanJarv/steampipe_alchemy are limited to only the permissions required here
and run in an isolated account. If anything is added these permissions need to be updated.
"""

import pytest
import boto3

import steampipe_alchemy
from steampipe_alchemy.models import AwsVpc

regions = ['us-east-1', 'us-east-2', 'us-west-2', 'us-west-1']


@pytest.fixture(scope='module')
def query():
    steampipe_alchemy.install(['aws'])
    steampipe_alchemy.update_config(aws={
        "plugin": "aws",
        "regions": regions,
    })
    steampipe_alchemy.start()
    return steampipe_alchemy.query


@pytest.fixture(scope='module')
def vpc_ids(query):
    return [vpc_id for (vpc_id,) in query(AwsVpc.vpc_id)]


@pytest.mark.parametrize("region", regions)
def test_this(region, vpc_ids):
    for vpc in boto3.resource('ec2', region_name=region).vpcs.all():
        assert vpc.id in sorted(vpc_ids)
