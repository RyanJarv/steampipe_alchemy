from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsSagemakerModel(Base, FormatMixins):
    __tablename__ = 'aws_sagemaker_model'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    enable_network_isolation = Column('enable_network_isolation', Boolean, nullable=True)
    execution_role_arn = Column('execution_role_arn', Text, nullable=True)
    containers = Column('containers', JSON, nullable=True)
    inference_execution_config = Column('inference_execution_config', JSON, nullable=True)
    primary_container = Column('primary_container', JSON, nullable=True)
    vpc_config = Column('vpc_config', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsSagemakerModelLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_sagemaker_model_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    enable_network_isolation = Column('enable_network_isolation', Boolean, nullable=True)
    execution_role_arn = Column('execution_role_arn', Text, nullable=True)
    containers = Column('containers', JSON, nullable=True)
    inference_execution_config = Column('inference_execution_config', JSON, nullable=True)
    primary_container = Column('primary_container', JSON, nullable=True)
    vpc_config = Column('vpc_config', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsSagemakerModel).select_from(AwsSagemakerModel)
create_materialized_view('aws_sagemaker_model_local', cache, db.metadata_materialized)
