from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEksAddonVersion(Base, FormatMixins):
    __tablename__ = 'aws_eks_addon_version'
    _ctx = Column('_ctx', JSON, nullable=True)
    addon_configuration = Column('addon_configuration', JSON, nullable=True)
    architecture = Column('architecture', JSON, nullable=True)
    compatibilities = Column('compatibilities', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    addon_name = Column('addon_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    addon_version = Column('addon_version', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)