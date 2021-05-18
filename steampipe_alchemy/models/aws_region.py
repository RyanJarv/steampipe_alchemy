from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsRegion(Base, FormatMixins):
    __tablename__ = 'aws_region'
    name = Column('name', Text, primary_key=True, nullable=True)
    opt_in_status = Column('opt_in_status', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsRegionLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_region_local'
    name = Column('name', Text, primary_key=True, nullable=True)
    opt_in_status = Column('opt_in_status', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsRegion).select_from(AwsRegion)
create_materialized_view('aws_region_local', cache, db.metadata_materialized)
