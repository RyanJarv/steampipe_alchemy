from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSecuritylakeDataLake(Base, FormatMixins):
    __tablename__ = 'aws_securitylake_data_lake'
    _ctx = Column('_ctx', JSON, nullable=True)
    replication_configuration = Column('replication_configuration', JSON, nullable=True)
    lifecycle_configuration = Column('lifecycle_configuration', JSON, nullable=True)
    update_status = Column('update_status', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    create_status = Column('create_status', Text, nullable=True)
    replication_role_arn = Column('replication_role_arn', Text, nullable=True)
    s3_bucket_arn = Column('s3_bucket_arn', Text, nullable=True)
    region = Column('region', Text, nullable=True)