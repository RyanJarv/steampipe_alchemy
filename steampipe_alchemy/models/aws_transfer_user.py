from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsTransferUser(Base, FormatMixins):
    __tablename__ = 'aws_transfer_user'
    _ctx = Column('_ctx', JSON, nullable=True)
    home_directory_mappings = Column('home_directory_mappings', JSON, nullable=True)
    ssh_public_key_count = Column('ssh_public_key_count', BigInteger, nullable=True)
    ssh_public_keys = Column('ssh_public_keys', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    server_id = Column('server_id', Text, nullable=True)
    user_name = Column('user_name', Text, nullable=True)
    home_directory = Column('home_directory', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    home_directory_type = Column('home_directory_type', Text, nullable=True)
    role = Column('role', Text, nullable=True)