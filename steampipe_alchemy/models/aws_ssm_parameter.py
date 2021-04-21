from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSsmParameter(Base):
    __tablename__ = 'aws_ssm_parameter'
    name = Column(name='name', type_=Text, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    value = Column(name='value', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    data_type = Column(name='data_type', type_=Text, nullable=True)
    key_id = Column(name='key_id', type_=Text, nullable=True)
    last_modified_date = Column(name='last_modified_date', type_=TIMESTAMP, nullable=True)
    last_modified_user = Column(name='last_modified_user', type_=Text, nullable=True)
    version = Column(name='version', type_=BigInteger, nullable=True)
    selector = Column(name='selector', type_=Text, nullable=True)
    source_result = Column(name='source_result', type_=Text, nullable=True)
    tier = Column(name='tier', type_=Text, nullable=True)
    policies = Column(name='policies', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)