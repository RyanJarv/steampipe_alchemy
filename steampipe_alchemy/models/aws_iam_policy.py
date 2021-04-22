from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamPolicy(Base):
    __tablename__ = 'aws_iam_policy'
    name = Column('name', Text, nullable=True)
    policy_id = Column('policy_id', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    is_aws_managed = Column('is_aws_managed', Boolean, nullable=True)
    is_attachable = Column('is_attachable', Boolean, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    update_date = Column('update_date', TIMESTAMP, nullable=True)
    attachment_count = Column('attachment_count', BigInteger, nullable=True)
    default_version_id = Column('default_version_id', Text, nullable=True)
    permissions_boundary_usage_count = Column('permissions_boundary_usage_count', BigInteger, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)