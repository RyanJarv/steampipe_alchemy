from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSsmAssociation(Base):
    __tablename__ = 'aws_ssm_association'
    association_id = Column(Text, name='association_id', nullable=True)
    association_name = Column(Text, name='association_name', nullable=True)
    document_name = Column(Text, name='document_name', nullable=True)
    date = Column(TIMESTAMP, name='date', nullable=True)
    association_version = Column(Text, name='association_version', nullable=True)
    document_version = Column(Text, name='document_version', nullable=True)
    instance_id = Column(Text, name='instance_id', nullable=True)
    last_execution_date = Column(TIMESTAMP, name='last_execution_date', nullable=True)
    overview = Column(JSON, name='overview', nullable=True)
    schedule_expression = Column(Text, name='schedule_expression', nullable=True)
    targets = Column(JSON, name='targets', nullable=True)
    compliance_severity = Column(Text, name='compliance_severity', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)