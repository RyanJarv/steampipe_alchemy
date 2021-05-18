from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsGuarddutyIpset(Base, FormatMixins):
    __tablename__ = 'aws_guardduty_ipset'
    name = Column('name', Text, primary_key=True, nullable=True)
    detector_id = Column('detector_id', Text, nullable=True)
    ipset_id = Column('ipset_id', Text, nullable=True)
    format = Column('format', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    location = Column('location', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsGuarddutyIpsetLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_guardduty_ipset_local'
    name = Column('name', Text, primary_key=True, nullable=True)
    detector_id = Column('detector_id', Text, nullable=True)
    ipset_id = Column('ipset_id', Text, nullable=True)
    format = Column('format', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    location = Column('location', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsGuarddutyIpset).select_from(AwsGuarddutyIpset)
create_materialized_view('aws_guardduty_ipset_local', cache, db.metadata_materialized)
