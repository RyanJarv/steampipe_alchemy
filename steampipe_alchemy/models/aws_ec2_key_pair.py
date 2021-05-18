from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsEc2KeyPair(Base, FormatMixins):
    __tablename__ = 'aws_ec2_key_pair'
    key_name = Column('key_name', Text, nullable=True)
    key_pair_id = Column('key_pair_id', Text, nullable=True)
    key_fingerprint = Column('key_fingerprint', Text, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsEc2KeyPairLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_ec2_key_pair_local'
    key_name = Column('key_name', Text, nullable=True)
    key_pair_id = Column('key_pair_id', Text, nullable=True)
    key_fingerprint = Column('key_fingerprint', Text, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsEc2KeyPair).select_from(AwsEc2KeyPair)
create_materialized_view('aws_ec2_key_pair_local', cache, db.metadata_materialized)
