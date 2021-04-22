from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsAcmCertificate(Base):
    __tablename__ = 'aws_acm_certificate'
    certificate_arn = Column('certificate_arn', Text, nullable=True)
    certificate = Column('certificate', Text, nullable=True)
    certificate_chain = Column('certificate_chain', Text, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    certificate_transparency_logging_preference = Column('certificate_transparency_logging_preference', Text, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    subject = Column('subject', Text, nullable=True)
    imported_at = Column('imported_at', TIMESTAMP, nullable=True)
    issuer = Column('issuer', Text, nullable=True)
    signature_algorithm = Column('signature_algorithm', Text, nullable=True)
    failure_reason = Column('failure_reason', Text, nullable=True)
    issued_at = Column('issued_at', TIMESTAMP, nullable=True)
    status = Column('status', Text, nullable=True)
    key_algorithm = Column('key_algorithm', Text, nullable=True)
    not_after = Column('not_after', TIMESTAMP, nullable=True)
    not_before = Column('not_before', TIMESTAMP, nullable=True)
    renewal_eligibility = Column('renewal_eligibility', Text, nullable=True)
    revocation_reason = Column('revocation_reason', Text, nullable=True)
    revoked_at = Column('revoked_at', TIMESTAMP, nullable=True)
    serial = Column('serial', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    domain_validation_options = Column('domain_validation_options', JSON, nullable=True)
    in_use_by = Column('in_use_by', JSON, nullable=True)
    subject_alternative_names = Column('subject_alternative_names', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)