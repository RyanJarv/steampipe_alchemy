from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamPolicy(Base):
    __tablename__ = 'aws_iam_policy'
    name = Column(Text, name='name', nullable=True)
    policy_id = Column(Text, name='policy_id', nullable=True)
    path = Column(Text, name='path', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    is_aws_managed = Column(Boolean, name='is_aws_managed', nullable=True)
    is_attachable = Column(Boolean, name='is_attachable', nullable=True)
    create_date = Column(TIMESTAMP, name='create_date', nullable=True)
    update_date = Column(TIMESTAMP, name='update_date', nullable=True)
    attachment_count = Column(BigInteger, name='attachment_count', nullable=True)
    default_version_id = Column(Text, name='default_version_id', nullable=True)
    permissions_boundary_usage_count = Column(BigInteger, name='permissions_boundary_usage_count', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)