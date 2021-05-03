from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsElasticsearchDomain(Base, FormatMixins):
    __tablename__ = 'aws_elasticsearch_domain'
    domain_name = Column('domain_name', Text, nullable=True)
    domain_id = Column('domain_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    elasticsearch_version = Column('elasticsearch_version', Text, nullable=True)
    endpoint = Column('endpoint', Text, nullable=True)
    created = Column('created', Boolean, nullable=True)
    deleted = Column('deleted', Boolean, nullable=True)
    processing = Column('processing', Boolean, nullable=True)
    upgrade_processing = Column('upgrade_processing', Boolean, nullable=True)
    enabled = Column('enabled', Boolean, nullable=True)
    access_policies = Column('access_policies', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    ebs_options = Column('ebs_options', JSON, nullable=True)
    advanced_options = Column('advanced_options', JSON, nullable=True)
    advanced_security_options = Column('advanced_security_options', JSON, nullable=True)
    auto_tune_options = Column('auto_tune_options', JSON, nullable=True)
    cognito_options = Column('cognito_options', JSON, nullable=True)
    domain_endpoint_options = Column('domain_endpoint_options', JSON, nullable=True)
    elasticsearch_cluster_config = Column('elasticsearch_cluster_config', JSON, nullable=True)
    encryption_at_rest_options = Column('encryption_at_rest_options', JSON, nullable=True)
    service_software_options = Column('service_software_options', JSON, nullable=True)
    snapshot_options = Column('snapshot_options', JSON, nullable=True)
    vpc_options = Column('vpc_options', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)