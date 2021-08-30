from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2RegionalSettings(Base, FormatMixins):
    __tablename__ = 'aws_ec2_regional_settings'
    default_ebs_encryption_enabled = Column('default_ebs_encryption_enabled', Boolean, nullable=True)
    default_ebs_encryption_key = Column('default_ebs_encryption_key', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)