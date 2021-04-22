from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsGuarddutyDetector(Base):
    __tablename__ = 'aws_guardduty_detector'
    detector_id = Column('detector_id', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    finding_publishing_frequency = Column('finding_publishing_frequency', Text, nullable=True)
    service_role = Column('service_role', Text, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    data_sources = Column('data_sources', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)