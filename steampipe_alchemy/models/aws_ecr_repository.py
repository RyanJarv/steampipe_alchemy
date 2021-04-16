from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEcrRepository(Base):
    __tablename__ = 'aws_ecr_repository'
    repository_name = Column(Text, name='repository_name', nullable=True)
    registry_id = Column(Text, name='registry_id', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    repository_uri = Column(Text, name='repository_uri', nullable=True)
    created_at = Column(TIMESTAMP, name='created_at', nullable=True)
    image_tag_mutability = Column(Text, name='image_tag_mutability', nullable=True)
    last_evaluated_at = Column(TIMESTAMP, name='last_evaluated_at', nullable=True)
    max_results = Column(BigInteger, name='max_results', nullable=True)
    encryption_configuration = Column(JSON, name='encryption_configuration', nullable=True)
    image_details = Column(JSON, name='image_details', nullable=True)
    image_scanning_configuration = Column(JSON, name='image_scanning_configuration', nullable=True)
    lifecycle_policy = Column(JSON, name='lifecycle_policy', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)