from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAcmpcaCertificateAuthority(Base, FormatMixins):
    __tablename__ = 'aws_acmpca_certificate_authority'
    certificate_authority_configuration = Column('certificate_authority_configuration', JSON, nullable=True)
    revocation_configuration = Column('revocation_configuration', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    restorable_until = Column('restorable_until', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    last_state_change_at = Column('last_state_change_at', TIMESTAMP, nullable=True)
    not_after = Column('not_after', TIMESTAMP, nullable=True)
    not_before = Column('not_before', TIMESTAMP, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    usage_mode = Column('usage_mode', Text, nullable=True)
    failure_reason = Column('failure_reason', Text, nullable=True)
    key_storage_security_standard = Column('key_storage_security_standard', Text, nullable=True)
    owner_account = Column('owner_account', Text, nullable=True)
    serial = Column('serial', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)