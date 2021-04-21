from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSecurityhubHub(Base):
    __tablename__ = 'aws_securityhub_hub'
    hub_arn = Column(name='hub_arn', type_=Text, nullable=True)
    auto_enable_controls = Column(name='auto_enable_controls', type_=Boolean, nullable=True)
    subscribed_at = Column(name='subscribed_at', type_=TIMESTAMP, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)