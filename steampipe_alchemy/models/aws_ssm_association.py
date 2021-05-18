from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsSsmAssociation(Base, FormatMixins):
    __tablename__ = 'aws_ssm_association'
    association_id = Column('association_id', Text, nullable=True)
    association_name = Column('association_name', Text, nullable=True)
    document_name = Column('document_name', Text, nullable=True)
    date = Column('date', TIMESTAMP, nullable=True)
    compliance_severity = Column('compliance_severity', Text, nullable=True)
    apply_only_at_cron_interval = Column('apply_only_at_cron_interval', Boolean, nullable=True)
    association_version = Column('association_version', Text, nullable=True)
    automation_target_parameter_name = Column('automation_target_parameter_name', Text, nullable=True)
    document_version = Column('document_version', Text, nullable=True)
    instance_id = Column('instance_id', Text, nullable=True)
    last_execution_date = Column('last_execution_date', TIMESTAMP, nullable=True)
    last_successful_execution_date = Column('last_successful_execution_date', TIMESTAMP, nullable=True)
    last_update_association_date = Column('last_update_association_date', TIMESTAMP, nullable=True)
    schedule_expression = Column('schedule_expression', Text, nullable=True)
    max_concurrency = Column('max_concurrency', Text, nullable=True)
    max_errors = Column('max_errors', Text, nullable=True)
    sync_compliance = Column('sync_compliance', Text, nullable=True)
    overview = Column('overview', JSON, nullable=True)
    output_location = Column('output_location', JSON, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    status = Column('status', JSON, nullable=True)
    targets = Column('targets', JSON, nullable=True)
    target_locations = Column('target_locations', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsSsmAssociationLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_ssm_association_local'
    association_id = Column('association_id', Text, nullable=True)
    association_name = Column('association_name', Text, nullable=True)
    document_name = Column('document_name', Text, nullable=True)
    date = Column('date', TIMESTAMP, nullable=True)
    compliance_severity = Column('compliance_severity', Text, nullable=True)
    apply_only_at_cron_interval = Column('apply_only_at_cron_interval', Boolean, nullable=True)
    association_version = Column('association_version', Text, nullable=True)
    automation_target_parameter_name = Column('automation_target_parameter_name', Text, nullable=True)
    document_version = Column('document_version', Text, nullable=True)
    instance_id = Column('instance_id', Text, nullable=True)
    last_execution_date = Column('last_execution_date', TIMESTAMP, nullable=True)
    last_successful_execution_date = Column('last_successful_execution_date', TIMESTAMP, nullable=True)
    last_update_association_date = Column('last_update_association_date', TIMESTAMP, nullable=True)
    schedule_expression = Column('schedule_expression', Text, nullable=True)
    max_concurrency = Column('max_concurrency', Text, nullable=True)
    max_errors = Column('max_errors', Text, nullable=True)
    sync_compliance = Column('sync_compliance', Text, nullable=True)
    overview = Column('overview', JSON, nullable=True)
    output_location = Column('output_location', JSON, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    status = Column('status', JSON, nullable=True)
    targets = Column('targets', JSON, nullable=True)
    target_locations = Column('target_locations', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsSsmAssociation).select_from(AwsSsmAssociation)
create_materialized_view('aws_ssm_association_local', cache, db.metadata_materialized)
