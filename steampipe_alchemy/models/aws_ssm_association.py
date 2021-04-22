from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSsmAssociation(Base):
    __tablename__ = 'aws_ssm_association'
    association_id = Column('association_id', Text, nullable=True)
    association_name = Column('association_name', Text, nullable=True)
    document_name = Column('document_name', Text, nullable=True)
    date = Column('date', TIMESTAMP, nullable=True)
    association_version = Column('association_version', Text, nullable=True)
    document_version = Column('document_version', Text, nullable=True)
    instance_id = Column('instance_id', Text, nullable=True)
    last_execution_date = Column('last_execution_date', TIMESTAMP, nullable=True)
    overview = Column('overview', JSON, nullable=True)
    schedule_expression = Column('schedule_expression', Text, nullable=True)
    targets = Column('targets', JSON, nullable=True)
    compliance_severity = Column('compliance_severity', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)