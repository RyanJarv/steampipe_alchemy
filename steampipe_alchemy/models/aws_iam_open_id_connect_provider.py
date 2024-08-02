from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamOpenIdConnectProvider(Base, FormatMixins):
    __tablename__ = 'aws_iam_open_id_connect_provider'
    _ctx = Column('_ctx', JSON, nullable=True)
    client_id_list = Column('client_id_list', JSON, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    thumbprint_list = Column('thumbprint_list', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    url = Column('url', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)