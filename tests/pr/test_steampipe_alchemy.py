#!/usr/bin/env python
"""
Tests for `steampipe_alchemy` package that run on opened PR's.

Any testing that doesn't require access to any AWS credentials goes here.
"""

import pytest
from tests.main.test_steampipe_alchemy import *

regions = ['us-east-1', 'us-east-2', 'us-west-2', 'us-west-1']


def test_query(steam):
    print(steam.query)


def test_query_deprecated(query_deprecated):
    print(query_deprecated)
