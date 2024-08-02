from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWellarchitectedShareInvitation(Base, FormatMixins):
    __tablename__ = 'aws_wellarchitected_share_invitation'
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    permission_type = Column('permission_type', Text, nullable=True)
    share_invitation_id = Column('share_invitation_id', Text, nullable=True)
    share_resource_type = Column('share_resource_type', Text, nullable=True)
    shared_by = Column('shared_by', Text, nullable=True)
    shared_with = Column('shared_with', Text, nullable=True)
    workload_name = Column('workload_name', Text, nullable=True)
    lens_arn = Column('lens_arn', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    workload_id = Column('workload_id', Text, nullable=True)
    lens_name = Column('lens_name', Text, nullable=True)