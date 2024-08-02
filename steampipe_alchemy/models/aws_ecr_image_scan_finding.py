from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEcrImageScanFinding(Base, FormatMixins):
    __tablename__ = 'aws_ecr_image_scan_finding'
    vulnerability_source_updated_at = Column('vulnerability_source_updated_at', TIMESTAMP, nullable=True)
    attributes = Column('attributes', JSON, nullable=True)
    image_scan_completed_at = Column('image_scan_completed_at', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    description = Column('description', Text, nullable=True)
    uri = Column('uri', Text, nullable=True)
    image_scan_status = Column('image_scan_status', Text, nullable=True)
    repository_name = Column('repository_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    image_scan_status_description = Column('image_scan_status_description', Text, nullable=True)
    image_tag = Column('image_tag', Text, nullable=True)
    image_digest = Column('image_digest', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    severity = Column('severity', Text, nullable=True)