from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsRedshiftParameterGroup(Base, FormatMixins):
    __tablename__ = 'aws_redshift_parameter_group'
    name = Column('name', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    family = Column('family', Text, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsRedshiftParameterGroupLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_redshift_parameter_group_local'
    name = Column('name', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    family = Column('family', Text, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsRedshiftParameterGroup).select_from(AwsRedshiftParameterGroup)
create_materialized_view('aws_redshift_parameter_group_local', cache, db.metadata_materialized)
