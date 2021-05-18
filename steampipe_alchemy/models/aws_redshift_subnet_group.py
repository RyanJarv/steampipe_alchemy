from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsRedshiftSubnetGroup(Base, FormatMixins):
    __tablename__ = 'aws_redshift_subnet_group'
    cluster_subnet_group_name = Column('cluster_subnet_group_name', Text, nullable=True)
    subnet_group_status = Column('subnet_group_status', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    subnets = Column('subnets', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsRedshiftSubnetGroupLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_redshift_subnet_group_local'
    cluster_subnet_group_name = Column('cluster_subnet_group_name', Text, nullable=True)
    subnet_group_status = Column('subnet_group_status', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    subnets = Column('subnets', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsRedshiftSubnetGroup).select_from(AwsRedshiftSubnetGroup)
create_materialized_view('aws_redshift_subnet_group_local', cache, db.metadata_materialized)
