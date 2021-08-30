from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2SslPolicy(Base, FormatMixins):
    __tablename__ = 'aws_ec2_ssl_policy'
    ssl_protocols = Column('ssl_protocols', JSON, nullable=True)
    ciphers = Column('ciphers', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)