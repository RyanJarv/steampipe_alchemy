from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEmrBlockPublicAccessConfiguration(Base, FormatMixins):
    __tablename__ = 'aws_emr_block_public_access_configuration'
    block_public_security_group_rules = Column('block_public_security_group_rules', Boolean, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, primary_key=True, nullable=True)
    permitted_public_security_group_rule_ranges = Column('permitted_public_security_group_rule_ranges', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    classification = Column('classification', Text, nullable=True)
    created_by_arn = Column('created_by_arn', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)