from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSecurityhubHub(Base):
    __tablename__ = 'aws_securityhub_hub'
    hub_arn = Column(Text, name='hub_arn', nullable=True)
    auto_enable_controls = Column(Boolean, name='auto_enable_controls', nullable=True)
    subscribed_at = Column(TIMESTAMP, name='subscribed_at', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)