from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDmsCertificate(Base, FormatMixins):
    __tablename__ = 'aws_dms_certificate'
    _ctx = Column('_ctx', JSON, nullable=True)
    certificate_creation_date = Column('certificate_creation_date', TIMESTAMP, nullable=True)
    key_length = Column('key_length', BigInteger, nullable=True)
    valid_from_date = Column('valid_from_date', TIMESTAMP, nullable=True)
    valid_to_date = Column('valid_to_date', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    certificate_owner = Column('certificate_owner', Text, nullable=True)
    certificate_pem = Column('certificate_pem', Text, nullable=True)
    certificate_wallet = Column('certificate_wallet', Text, nullable=True)
    certificate_identifier = Column('certificate_identifier', Text, nullable=True)
    signing_algorithm = Column('signing_algorithm', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)