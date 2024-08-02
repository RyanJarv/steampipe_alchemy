from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRedshiftserverlessWorkgroup(Base, FormatMixins):
    __tablename__ = 'aws_redshiftserverless_workgroup'
    _ctx = Column('_ctx', JSON, nullable=True)
    enhanced_vpc_routing = Column('enhanced_vpc_routing', Boolean, nullable=True)
    publicly_accessible = Column('publicly_accessible', Boolean, nullable=True)
    config_parameters = Column('config_parameters', JSON, nullable=True)
    endpoint = Column('endpoint', JSON, nullable=True)
    security_group_ids = Column('security_group_ids', JSON, nullable=True)
    subnet_ids = Column('subnet_ids', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    base_capacity = Column('base_capacity', BigInteger, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    workgroup_id = Column('workgroup_id', Text, nullable=True)
    workgroup_arn = Column('workgroup_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    namespace_name = Column('namespace_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    workgroup_name = Column('workgroup_name', Text, nullable=True)