from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSsmParameter(Base):
    __tablename__ = 'aws_ssm_parameter'
    name = Column(Text, name='name', nullable=True)
    type = Column(Text, name='type', nullable=True)
    value = Column(Text, name='value', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    data_type = Column(Text, name='data_type', nullable=True)
    key_id = Column(Text, name='key_id', nullable=True)
    last_modified_date = Column(TIMESTAMP, name='last_modified_date', nullable=True)
    last_modified_user = Column(Text, name='last_modified_user', nullable=True)
    version = Column(BigInteger, name='version', nullable=True)
    selector = Column(Text, name='selector', nullable=True)
    source_result = Column(Text, name='source_result', nullable=True)
    tier = Column(Text, name='tier', nullable=True)
    policies = Column(JSON, name='policies', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)