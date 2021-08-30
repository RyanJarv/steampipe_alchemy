from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsmManagedInstanceCompliance(Base, FormatMixins):
    __tablename__ = 'aws_ssm_managed_instance_compliance'
    execution_summary = Column('execution_summary', JSON, nullable=True)
    details = Column('details', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    status = Column('status', Text, nullable=True)
    compliance_type = Column('compliance_type', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    severity = Column('severity', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)