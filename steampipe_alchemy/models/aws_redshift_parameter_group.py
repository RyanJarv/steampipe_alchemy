from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRedshiftParameterGroup(Base):
    __tablename__ = 'aws_redshift_parameter_group'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    description = Column(Text, name='description', nullable=True)
    family = Column(Text, name='family', nullable=True)
    parameters = Column(JSON, name='parameters', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)