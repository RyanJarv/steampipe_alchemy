from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamPolicy(Base):
    __tablename__ = 'aws_iam_policy'
    name = Column(name='name', type_=Text, nullable=True)
    policy_id = Column(name='policy_id', type_=Text, nullable=True)
    path = Column(name='path', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    is_aws_managed = Column(name='is_aws_managed', type_=Boolean, nullable=True)
    is_attachable = Column(name='is_attachable', type_=Boolean, nullable=True)
    create_date = Column(name='create_date', type_=TIMESTAMP, nullable=True)
    update_date = Column(name='update_date', type_=TIMESTAMP, nullable=True)
    attachment_count = Column(name='attachment_count', type_=BigInteger, nullable=True)
    default_version_id = Column(name='default_version_id', type_=Text, nullable=True)
    permissions_boundary_usage_count = Column(name='permissions_boundary_usage_count', type_=BigInteger, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)