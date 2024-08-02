from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGuarddutyPublishingDestination(Base, FormatMixins):
    __tablename__ = 'aws_guardduty_publishing_destination'
    publishing_failure_start_timestamp = Column('publishing_failure_start_timestamp', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    destination_type = Column('destination_type', Text, nullable=True)
    kms_key_arn = Column('kms_key_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    destination_id = Column('destination_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    detector_id = Column('detector_id', Text, nullable=True)
    destination_arn = Column('destination_arn', Text, nullable=True)