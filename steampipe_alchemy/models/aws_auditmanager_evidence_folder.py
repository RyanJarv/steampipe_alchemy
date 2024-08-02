from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAuditmanagerEvidenceFolder(Base, FormatMixins):
    __tablename__ = 'aws_auditmanager_evidence_folder'
    _ctx = Column('_ctx', JSON, nullable=True)
    assessment_report_selection_count = Column('assessment_report_selection_count', BigInteger, nullable=True)
    date = Column('date', TIMESTAMP, nullable=True)
    evidence_aws_service_source_count = Column('evidence_aws_service_source_count', BigInteger, nullable=True)
    evidence_by_type_compliance_check_count = Column('evidence_by_type_compliance_check_count', BigInteger, nullable=True)
    evidence_by_type_compliance_check_issues_count = Column('evidence_by_type_compliance_check_issues_count', BigInteger, nullable=True)
    evidence_by_type_configuration_data_count = Column('evidence_by_type_configuration_data_count', BigInteger, nullable=True)
    evidence_by_type_manual_count = Column('evidence_by_type_manual_count', BigInteger, nullable=True)
    evidence_by_type_user_activity_count = Column('evidence_by_type_user_activity_count', BigInteger, nullable=True)
    evidence_resources_included_count = Column('evidence_resources_included_count', BigInteger, nullable=True)
    total_evidence = Column('total_evidence', BigInteger, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    assessment_id = Column('assessment_id', Text, nullable=True)
    control_set_id = Column('control_set_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    author = Column('author', Text, nullable=True)
    control_id = Column('control_id', Text, nullable=True)
    control_name = Column('control_name', Text, nullable=True)
    data_source = Column('data_source', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)