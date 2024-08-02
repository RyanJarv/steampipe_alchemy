from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2LaunchTemplate(Base, FormatMixins):
    __tablename__ = 'aws_ec2_launch_template'
    _ctx = Column('_ctx', JSON, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    default_version_number = Column('default_version_number', BigInteger, nullable=True)
    latest_version_number = Column('latest_version_number', BigInteger, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    launch_template_id = Column('launch_template_id', Text, nullable=True)
    launch_template_name = Column('launch_template_name', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)