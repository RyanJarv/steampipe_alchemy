from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRdsDbProxy(Base, FormatMixins):
    __tablename__ = 'aws_rds_db_proxy'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    debug_logging = Column('debug_logging', Boolean, nullable=True)
    idle_client_timeout = Column('idle_client_timeout', BigInteger, nullable=True)
    require_tls = Column('require_tls', Boolean, nullable=True)
    updated_date = Column('updated_date', TIMESTAMP, nullable=True)
    auth = Column('auth', JSON, nullable=True)
    vpc_security_group_ids = Column('vpc_security_group_ids', JSON, nullable=True)
    vpc_subnet_ids = Column('vpc_subnet_ids', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    db_proxy_arn = Column('db_proxy_arn', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    endpoint = Column('endpoint', Text, nullable=True)
    engine_family = Column('engine_family', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    db_proxy_name = Column('db_proxy_name', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)