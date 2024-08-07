from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2RegionalSettings(Base, FormatMixins):
    __tablename__ = 'aws_ec2_regional_settings'
    default_ebs_encryption_enabled = Column('default_ebs_encryption_enabled', Boolean, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    default_ebs_encryption_key = Column('default_ebs_encryption_key', Text, nullable=True)
    snapshot_block_public_access_state = Column('snapshot_block_public_access_state', Text, nullable=True)