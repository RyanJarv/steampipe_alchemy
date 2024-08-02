from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEmrSecurityConfiguration(Base, FormatMixins):
    __tablename__ = 'aws_emr_security_configuration'
    encryption_configuration = Column('encryption_configuration', JSON, nullable=True)
    instance_metadata_service_configuration = Column('instance_metadata_service_configuration', JSON, nullable=True)
    security_configuration = Column('security_configuration', JSON, nullable=True)
    creation_date_time = Column('creation_date_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)