from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEcrImage(Base, FormatMixins):
    __tablename__ = 'aws_ecr_image'
    _ctx = Column('_ctx', JSON, nullable=True)
    image_pushed_at = Column('image_pushed_at', TIMESTAMP, nullable=True)
    image_size_in_bytes = Column('image_size_in_bytes', BigInteger, nullable=True)
    last_recorded_pull_time = Column('last_recorded_pull_time', TIMESTAMP, nullable=True)
    image_scan_findings_summary = Column('image_scan_findings_summary', JSON, nullable=True)
    image_scan_status = Column('image_scan_status', JSON, nullable=True)
    image_tags = Column('image_tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    registry_id = Column('registry_id', Text, nullable=True, primary_key=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    artifact_media_type = Column('artifact_media_type', Text, nullable=True)
    image_digest = Column('image_digest', Text, nullable=True, primary_key=True)
    image_uri = Column('image_uri', Text, nullable=True)
    image_manifest_media_type = Column('image_manifest_media_type', Text, nullable=True)
    repository_name = Column('repository_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
