from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGuarddutyDetector(Base, FormatMixins):
    __tablename__ = 'aws_guardduty_detector'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    data_sources = Column('data_sources', JSON, nullable=True)
    features = Column('features', JSON, nullable=True)
    master_account = Column('master_account', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    finding_publishing_frequency = Column('finding_publishing_frequency', Text, nullable=True)
    service_role = Column('service_role', Text, nullable=True)
    detector_id = Column('detector_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)