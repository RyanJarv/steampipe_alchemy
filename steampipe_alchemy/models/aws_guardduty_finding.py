from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGuarddutyFinding(Base, FormatMixins):
    __tablename__ = 'aws_guardduty_finding'
    _ctx = Column('_ctx', JSON, nullable=True)
    severity = Column('severity', psql.DOUBLE_PRECISION, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    confidence = Column('confidence', psql.DOUBLE_PRECISION, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    resource = Column('resource', JSON, nullable=True)
    service = Column('service', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    type = Column('type', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    detector_id = Column('detector_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    schema_version = Column('schema_version', Text, nullable=True)