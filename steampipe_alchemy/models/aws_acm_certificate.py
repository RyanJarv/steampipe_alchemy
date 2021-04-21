from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsAcmCertificate(Base):
    __tablename__ = 'aws_acm_certificate'
    certificate_arn = Column(name='certificate_arn', type_=Text, nullable=True)
    certificate = Column(name='certificate', type_=Text, nullable=True)
    certificate_chain = Column(name='certificate_chain', type_=Text, nullable=True)
    domain_name = Column(name='domain_name', type_=Text, nullable=True)
    certificate_transparency_logging_preference = Column(name='certificate_transparency_logging_preference', type_=Text, nullable=True)
    created_at = Column(name='created_at', type_=TIMESTAMP, nullable=True)
    subject = Column(name='subject', type_=Text, nullable=True)
    imported_at = Column(name='imported_at', type_=TIMESTAMP, nullable=True)
    issuer = Column(name='issuer', type_=Text, nullable=True)
    signature_algorithm = Column(name='signature_algorithm', type_=Text, nullable=True)
    failure_reason = Column(name='failure_reason', type_=Text, nullable=True)
    issued_at = Column(name='issued_at', type_=TIMESTAMP, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    key_algorithm = Column(name='key_algorithm', type_=Text, nullable=True)
    not_after = Column(name='not_after', type_=TIMESTAMP, nullable=True)
    not_before = Column(name='not_before', type_=TIMESTAMP, nullable=True)
    renewal_eligibility = Column(name='renewal_eligibility', type_=Text, nullable=True)
    revocation_reason = Column(name='revocation_reason', type_=Text, nullable=True)
    revoked_at = Column(name='revoked_at', type_=TIMESTAMP, nullable=True)
    serial = Column(name='serial', type_=Text, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    domain_validation_options = Column(name='domain_validation_options', type_=JSON, nullable=True)
    in_use_by = Column(name='in_use_by', type_=JSON, nullable=True)
    subject_alternative_names = Column(name='subject_alternative_names', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)