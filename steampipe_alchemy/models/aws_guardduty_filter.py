from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGuarddutyFilter(Base, FormatMixins):
    __tablename__ = 'aws_guardduty_filter'
    _ctx = Column('_ctx', JSON, nullable=True)
    rank = Column('rank', BigInteger, nullable=True)
    finding_criteria = Column('finding_criteria', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    detector_id = Column('detector_id', Text, nullable=True)
    action = Column('action', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)