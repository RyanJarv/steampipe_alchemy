from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAccountAlternateContact(Base, FormatMixins):
    __tablename__ = 'aws_account_alternate_contact'
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    email_address = Column('email_address', Text, nullable=True)
    phone_number = Column('phone_number', Text, nullable=True)
    contact_title = Column('contact_title', Text, nullable=True)
    linked_account_id = Column('linked_account_id', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    contact_type = Column('contact_type', Text, nullable=True)