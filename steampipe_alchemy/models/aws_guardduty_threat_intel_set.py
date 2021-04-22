from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsGuarddutyThreatIntelSet(Base):
    __tablename__ = 'aws_guardduty_threat_intel_set'
    name = Column('name', Text, primary_key=True, nullable=True)
    threat_intel_set_id = Column('threat_intel_set_id', Text, nullable=True)
    detector_id = Column('detector_id', Text, nullable=True)
    format = Column('format', Text, nullable=True)
    location = Column('location', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)