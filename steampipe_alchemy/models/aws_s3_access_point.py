from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsS3AccessPoint(Base, FormatMixins):
    __tablename__ = 'aws_s3_access_point'
    access_point_policy_is_public = Column('access_point_policy_is_public', Boolean, nullable=True)
    block_public_acls = Column('block_public_acls', Boolean, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    block_public_policy = Column('block_public_policy', Boolean, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    ignore_public_acls = Column('ignore_public_acls', Boolean, nullable=True)
    restrict_public_buckets = Column('restrict_public_buckets', Boolean, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    access_point_arn = Column('access_point_arn', Text, nullable=True)
    bucket_name = Column('bucket_name', Text, nullable=True)
    network_origin = Column('network_origin', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)