from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsAcmCertificate(Base):
    __tablename__ = 'aws_acm_certificate'
    certificate_arn = Column(Text, name='certificate_arn', nullable=True)
    certificate = Column(Text, name='certificate', nullable=True)
    certificate_chain = Column(Text, name='certificate_chain', nullable=True)
    domain_name = Column(Text, name='domain_name', nullable=True)
    certificate_transparency_logging_preference = Column(Text, name='certificate_transparency_logging_preference', nullable=True)
    created_at = Column(TIMESTAMP, name='created_at', nullable=True)
    subject = Column(Text, name='subject', nullable=True)
    imported_at = Column(TIMESTAMP, name='imported_at', nullable=True)
    issuer = Column(Text, name='issuer', nullable=True)
    signature_algorithm = Column(Text, name='signature_algorithm', nullable=True)
    failure_reason = Column(Text, name='failure_reason', nullable=True)
    issued_at = Column(TIMESTAMP, name='issued_at', nullable=True)
    status = Column(Text, name='status', nullable=True)
    key_algorithm = Column(Text, name='key_algorithm', nullable=True)
    not_after = Column(TIMESTAMP, name='not_after', nullable=True)
    not_before = Column(TIMESTAMP, name='not_before', nullable=True)
    renewal_eligibility = Column(Text, name='renewal_eligibility', nullable=True)
    revocation_reason = Column(Text, name='revocation_reason', nullable=True)
    revoked_at = Column(TIMESTAMP, name='revoked_at', nullable=True)
    serial = Column(Text, name='serial', nullable=True)
    type = Column(Text, name='type', nullable=True)
    domain_validation_options = Column(JSON, name='domain_validation_options', nullable=True)
    in_use_by = Column(JSON, name='in_use_by', nullable=True)
    subject_alternative_names = Column(JSON, name='subject_alternative_names', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)