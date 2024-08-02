from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWellarchitectedLens(Base, FormatMixins):
    __tablename__ = 'aws_wellarchitected_lens'
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    lens_version = Column('lens_version', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    lens_name = Column('lens_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    share_invitation_id = Column('share_invitation_id', Text, nullable=True)
    lens_alias = Column('lens_alias', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    lens_status = Column('lens_status', Text, nullable=True)
    lens_type = Column('lens_type', Text, nullable=True)