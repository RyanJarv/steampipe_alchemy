from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSsmAssociation(Base):
    __tablename__ = 'aws_ssm_association'
    association_id = Column(name='association_id', type_=Text, nullable=True)
    association_name = Column(name='association_name', type_=Text, nullable=True)
    document_name = Column(name='document_name', type_=Text, nullable=True)
    date = Column(name='date', type_=TIMESTAMP, nullable=True)
    association_version = Column(name='association_version', type_=Text, nullable=True)
    document_version = Column(name='document_version', type_=Text, nullable=True)
    instance_id = Column(name='instance_id', type_=Text, nullable=True)
    last_execution_date = Column(name='last_execution_date', type_=TIMESTAMP, nullable=True)
    overview = Column(name='overview', type_=JSON, nullable=True)
    schedule_expression = Column(name='schedule_expression', type_=Text, nullable=True)
    targets = Column(name='targets', type_=JSON, nullable=True)
    compliance_severity = Column(name='compliance_severity', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)