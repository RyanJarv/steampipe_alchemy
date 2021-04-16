
from steampipe_alchemy import query
from steampipe_alchemy.models import *

for i in query(AwsS3Bucket):
    print(i.name)
