from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRdsDbSnapshot(Base):
    __tablename__ = 'aws_rds_db_snapshot'
    db_snapshot_identifier = Column(name='db_snapshot_identifier', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    create_time = Column(name='create_time', type_=TIMESTAMP, nullable=True)
    allocated_storage = Column(name='allocated_storage', type_=BigInteger, nullable=True)
    availability_zone = Column(name='availability_zone', type_=Text, nullable=True)
    db_instance_identifier = Column(name='db_instance_identifier', type_=Text, nullable=True)
    dbi_resource_id = Column(name='dbi_resource_id', type_=Text, nullable=True)
    encrypted = Column(name='encrypted', type_=Boolean, nullable=True)
    engine = Column(name='engine', type_=Text, nullable=True)
    engine_version = Column(name='engine_version', type_=Text, nullable=True)
    iam_database_authentication_enabled = Column(name='iam_database_authentication_enabled', type_=Boolean, nullable=True)
    instance_create_time = Column(name='instance_create_time', type_=TIMESTAMP, nullable=True)
    iops = Column(name='iops', type_=BigInteger, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    license_model = Column(name='license_model', type_=Text, nullable=True)
    master_user_name = Column(name='master_user_name', type_=Text, nullable=True)
    option_group_name = Column(name='option_group_name', type_=Text, nullable=True)
    percent_progress = Column(name='percent_progress', type_=BigInteger, nullable=True)
    port = Column(name='port', type_=BigInteger, nullable=True)
    source_db_snapshot_identifier = Column(name='source_db_snapshot_identifier', type_=Text, nullable=True)
    source_region = Column(name='source_region', type_=Text, nullable=True)
    storage_type = Column(name='storage_type', type_=Text, nullable=True)
    tde_credential_arn = Column(name='tde_credential_arn', type_=Text, nullable=True)
    timezone = Column(name='timezone', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    db_snapshot_attributes = Column(name='db_snapshot_attributes', type_=JSON, nullable=True)
    processor_features = Column(name='processor_features', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)