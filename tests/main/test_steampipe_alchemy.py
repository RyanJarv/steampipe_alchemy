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
def steam_class() -> steampipe_alchemy.SteamPipe:
    return steampipe_alchemy.SteamPipe()


@pytest.fixture(scope='module')
def steam(steam_class) -> steampipe_alchemy.SteamPipe:
    steam_class.install(['aws'])
    steam_class.update_config(aws={
        "plugin": "aws",
        "regions": regions,
    })
    status: steampipe_alchemy.ServiceStatus = steam_class.start()
    assert status.state == status.state.RUNNING
    return steam_class


@pytest.fixture(scope='module')
def steam_install_plugin(steam_class) -> steampipe_alchemy.SteamPipe:
    steam_class.install()
    steam_class.install_plugin('aws')
    steam_class.update_config(aws={
        "plugin": "aws",
        "regions": regions,
    })
    status: steampipe_alchemy.ServiceStatus = steam_class.start()
    assert status.state == status.state.RUNNING
    return steam_class


def test_steam_install_plugin(steam_install_plugin):
    for i in steam_install_plugin.query(AwsVpc.vpc_id):
        print(i)


@pytest.fixture(scope='module')
def query_deprecated() -> steampipe_alchemy.query:
    steampipe_alchemy.install(['aws'])
    steampipe_alchemy.update_config(aws={
        "plugin": "aws",
        "regions": regions,
    })
    status: steampipe_alchemy.ServiceStatus = steampipe_alchemy.start()
    assert status.state == steampipe_alchemy.ServiceState.RUNNING
    return steampipe_alchemy.query


@pytest.fixture(scope='module')
def vpc_ids_deprecated(query_deprecated: steampipe_alchemy.query):
    for i in query_deprecated(AwsVpc.vpc_id):
        print(i)
    return [vpc_id for (vpc_id,) in query_deprecated(AwsVpc.vpc_id)]


@pytest.mark.parametrize("region", regions)
def test_this_deprecated(region, vpc_ids_deprecated):
    for vpc in boto3.resource('ec2', region_name=region).vpcs.all():
        assert vpc.id in sorted(vpc_ids_deprecated)


@pytest.fixture(scope='module')
def vpc_ids(steam: steampipe_alchemy.SteamPipe):
    return [vpc_id for (vpc_id,) in steam.query(AwsVpc.vpc_id)]


@pytest.mark.parametrize("region", regions)
def test_this(region, vpc_ids):
    for vpc in boto3.resource('ec2', region_name=region).vpcs.all():
        assert vpc.id in sorted(vpc_ids)


def test_deprecated_function_prints_warning():
    steampipe_alchemy.query(AwsVpc.vpc_id)

# TODO:
# def test_status_configures_dbconn_when_postgres_is_running()
# def test_status_does_not_configure_dbconn_when_postgres_is_stopped()
# def test_status_does_not_configure_dbconn_when_postgres_is_in_unknown_state()
