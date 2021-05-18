from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsRdsDbClusterParameterGroup(Base, FormatMixins):
    __tablename__ = 'aws_rds_db_cluster_parameter_group'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    db_parameter_group_family = Column('db_parameter_group_family', Text, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsRdsDbClusterParameterGroupLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_rds_db_cluster_parameter_group_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    db_parameter_group_family = Column('db_parameter_group_family', Text, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsRdsDbClusterParameterGroup).select_from(AwsRdsDbClusterParameterGroup)
create_materialized_view('aws_rds_db_cluster_parameter_group_local', cache, db.metadata_materialized)
