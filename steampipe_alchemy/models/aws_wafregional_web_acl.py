from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWafregionalWebAcl(Base, FormatMixins):
    __tablename__ = 'aws_wafregional_web_acl'
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    rules = Column('rules', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    logging_configuration = Column('logging_configuration', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    web_acl_id = Column('web_acl_id', Text, nullable=True)
    default_action = Column('default_action', Text, nullable=True)
    metric_name = Column('metric_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)