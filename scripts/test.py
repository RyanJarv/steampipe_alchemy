#!/usr/bin/env python3

from steampipe_alchemy import query, start, install, update_config
from steampipe_alchemy.models import AwsVpc

install(['aws'])
update_config(aws={
    'plugin': 'aws',
    'regions': ['us-east-1', 'us-east-2', 'us-west-2', 'us-west-1']
})
start()

for i in query(AwsVpc).limit(2):
    print(i.vpc_id + ':')
    print('  CIDR: ' + i.cidr_block)
    print('  Region: ' + i.region)

first_vpc = query(AwsVpc).first().to_dict()
print('\nCIDR (first vpc): ' + first_vpc['cidr_block'])
