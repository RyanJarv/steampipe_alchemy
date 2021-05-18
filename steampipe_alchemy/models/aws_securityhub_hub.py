from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsSecurityhubHub(Base, FormatMixins):
    __tablename__ = 'aws_securityhub_hub'
    hub_arn = Column('hub_arn', Text, nullable=True)
    auto_enable_controls = Column('auto_enable_controls', Boolean, nullable=True)
    subscribed_at = Column('subscribed_at', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsSecurityhubHubLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_securityhub_hub_local'
    hub_arn = Column('hub_arn', Text, nullable=True)
    auto_enable_controls = Column('auto_enable_controls', Boolean, nullable=True)
    subscribed_at = Column('subscribed_at', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsSecurityhubHub).select_from(AwsSecurityhubHub)
create_materialized_view('aws_securityhub_hub_local', cache, db.metadata_materialized)
