from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSsmParameter(Base):
    __tablename__ = 'aws_ssm_parameter'
    name = Column('name', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    value = Column('value', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    data_type = Column('data_type', Text, nullable=True)
    key_id = Column('key_id', Text, nullable=True)
    last_modified_date = Column('last_modified_date', TIMESTAMP, nullable=True)
    last_modified_user = Column('last_modified_user', Text, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    selector = Column('selector', Text, nullable=True)
    source_result = Column('source_result', Text, nullable=True)
    tier = Column('tier', Text, nullable=True)
    policies = Column('policies', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)