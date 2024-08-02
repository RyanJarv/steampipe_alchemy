from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsInspector2Coverage(Base, FormatMixins):
    __tablename__ = 'aws_inspector2_coverage'
    _ctx = Column('_ctx', JSON, nullable=True)
    ec2_platform = Column('ec2_platform', JSON, nullable=True)
    ec2_instance_tags = Column('ec2_instance_tags', JSON, nullable=True)
    ecr_image_tags = Column('ecr_image_tags', JSON, nullable=True)
    lambda_function_tags = Column('lambda_function_tags', JSON, nullable=True)
    lambda_function_layers = Column('lambda_function_layers', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    ecr_repository_scan_frequency = Column('ecr_repository_scan_frequency', Text, nullable=True)
    lambda_function_name = Column('lambda_function_name', Text, nullable=True)
    lambda_function_runtime = Column('lambda_function_runtime', Text, nullable=True)
    scan_status_reason = Column('scan_status_reason', Text, nullable=True)
    scan_status_code = Column('scan_status_code', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    source_account_id = Column('source_account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    scan_type = Column('scan_type', Text, nullable=True)
    ec2_ami_id = Column('ec2_ami_id', Text, nullable=True)
    ecr_image_tag = Column('ecr_image_tag', Text, nullable=True)
    ecr_repository_name = Column('ecr_repository_name', Text, nullable=True)