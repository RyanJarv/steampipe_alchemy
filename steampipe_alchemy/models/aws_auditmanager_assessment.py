from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAuditmanagerAssessment(Base, FormatMixins):
    __tablename__ = 'aws_auditmanager_assessment'
    framework = Column('framework', JSON, nullable=True)
    scope = Column('scope', JSON, nullable=True)
    roles = Column('roles', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    last_updated = Column('last_updated', TIMESTAMP, nullable=True)
    aws_account = Column('aws_account', JSON, nullable=True)
    delegations = Column('delegations', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    compliance_type = Column('compliance_type', Text, nullable=True)
    assessment_report_destination = Column('assessment_report_destination', Text, nullable=True)
    assessment_report_destination_type = Column('assessment_report_destination_type', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    title = Column('title', Text, nullable=True)