from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRedshiftParameterGroup(Base):
    __tablename__ = 'aws_redshift_parameter_group'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    family = Column(name='family', type_=Text, nullable=True)
    parameters = Column(name='parameters', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)