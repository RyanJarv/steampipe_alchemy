from steampipe_alchemy import query, start, install, update_config
from steampipe_alchemy.models import AwsVpc

install(['aws'])
update_config(aws={
    "plugin": "aws",
    "regions": ['us-east-1', 'us-east-2', 'us-west-2', 'us-west-1']
})
start()

for b in query(AwsVpc):
    print(b.region)
