from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsEcrpublicRepository(Base, FormatMixins):
    __tablename__ = 'aws_ecrpublic_repository'
    repository_name = Column('repository_name', Text, nullable=True)
    registry_id = Column('registry_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    repository_uri = Column('repository_uri', Text, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    image_details = Column('image_details', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsEcrpublicRepositoryLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_ecrpublic_repository_local'
    repository_name = Column('repository_name', Text, nullable=True)
    registry_id = Column('registry_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    repository_uri = Column('repository_uri', Text, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    image_details = Column('image_details', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsEcrpublicRepository).select_from(AwsEcrpublicRepository)
create_materialized_view('aws_ecrpublic_repository_local', cache, db.metadata_materialized)
