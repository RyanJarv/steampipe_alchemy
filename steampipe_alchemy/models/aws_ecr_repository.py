from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEcrRepository(Base, FormatMixins):
    __tablename__ = 'aws_ecr_repository'
    _ctx = Column('_ctx', JSON, nullable=True)
    repository_scanning_configuration = Column('repository_scanning_configuration', JSON, nullable=True)
    image_scanning_configuration = Column('image_scanning_configuration', JSON, nullable=True)
    image_scanning_findings = Column('image_scanning_findings', JSON, nullable=True)
    lifecycle_policy = Column('lifecycle_policy', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    last_evaluated_at = Column('last_evaluated_at', TIMESTAMP, nullable=True)
    max_results = Column('max_results', BigInteger, nullable=True)
    encryption_configuration = Column('encryption_configuration', JSON, nullable=True)
    image_details = Column('image_details', JSON, nullable=True)
    registry_id = Column('registry_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    repository_uri = Column('repository_uri', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    image_tag_mutability = Column('image_tag_mutability', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    repository_name = Column('repository_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)