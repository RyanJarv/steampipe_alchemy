from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRamResourceAssociation(Base, FormatMixins):
    __tablename__ = 'aws_ram_resource_association'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    external = Column('external', Boolean, nullable=True)
    last_updated_time = Column('last_updated_time', TIMESTAMP, nullable=True)
    resource_share_permission = Column('resource_share_permission', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    resource_share_name = Column('resource_share_name', Text, nullable=True)
    resource_share_arn = Column('resource_share_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    associated_entity = Column('associated_entity', Text, nullable=True)
    association_type = Column('association_type', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)