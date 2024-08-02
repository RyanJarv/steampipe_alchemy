from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSesDomainIdentity(Base, FormatMixins):
    __tablename__ = 'aws_ses_domain_identity'
    identity_mail_from_domain_attributes = Column('identity_mail_from_domain_attributes', JSON, nullable=True)
    notification_attributes = Column('notification_attributes', JSON, nullable=True)
    dkim_attributes = Column('dkim_attributes', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    verification_status = Column('verification_status', Text, nullable=True)
    verification_token = Column('verification_token', Text, nullable=True)
    identity = Column('identity', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)