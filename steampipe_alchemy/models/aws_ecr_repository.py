from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEcrRepository(Base):
    __tablename__ = 'aws_ecr_repository'
    repository_name = Column(name='repository_name', type_=Text, nullable=True)
    registry_id = Column(name='registry_id', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    repository_uri = Column(name='repository_uri', type_=Text, nullable=True)
    created_at = Column(name='created_at', type_=TIMESTAMP, nullable=True)
    image_tag_mutability = Column(name='image_tag_mutability', type_=Text, nullable=True)
    last_evaluated_at = Column(name='last_evaluated_at', type_=TIMESTAMP, nullable=True)
    max_results = Column(name='max_results', type_=BigInteger, nullable=True)
    encryption_configuration = Column(name='encryption_configuration', type_=JSON, nullable=True)
    image_details = Column(name='image_details', type_=JSON, nullable=True)
    image_scanning_configuration = Column(name='image_scanning_configuration', type_=JSON, nullable=True)
    lifecycle_policy = Column(name='lifecycle_policy', type_=JSON, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)