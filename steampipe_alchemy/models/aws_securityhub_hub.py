from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSecurityhubHub(Base):
    __tablename__ = 'aws_securityhub_hub'
    hub_arn = Column('hub_arn', Text, nullable=True)
    auto_enable_controls = Column('auto_enable_controls', Boolean, nullable=True)
    subscribed_at = Column('subscribed_at', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)