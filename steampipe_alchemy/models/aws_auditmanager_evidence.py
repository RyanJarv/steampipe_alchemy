from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAuditmanagerEvidence(Base, FormatMixins):
    __tablename__ = 'aws_auditmanager_evidence'
    akas = Column('akas', JSON, nullable=True)
    attributes = Column('attributes', JSON, nullable=True)
    resources_included = Column('resources_included', JSON, nullable=True)
    time = Column('time', TIMESTAMP, nullable=True)
    evidence_folder_id = Column('evidence_folder_id', Text, nullable=True)
    assessment_report_selection = Column('assessment_report_selection', Text, nullable=True)
    aws_account_id = Column('aws_account_id', Text, nullable=True)
    aws_organization = Column('aws_organization', Text, nullable=True)
    compliance_check = Column('compliance_check', Text, nullable=True)
    data_source = Column('data_source', Text, nullable=True)
    event_name = Column('event_name', Text, nullable=True)
    event_source = Column('event_source', Text, nullable=True)
    evidence_aws_account_id = Column('evidence_aws_account_id', Text, nullable=True)
    evidence_by_type = Column('evidence_by_type', Text, nullable=True)
    iam_id = Column('iam_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    assessment_id = Column('assessment_id', Text, nullable=True)
    control_set_id = Column('control_set_id', Text, nullable=True)