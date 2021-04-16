
from steampipe_alchemy import query
from steampipe_alchemy.models import AwsS3Bucket

for b in query(AwsS3Bucket).limit(3):
    print(b.name)
    print("  Region: " + b.region)
    print("  Owner: " + str(b.acl['Owner']['DisplayName']))
