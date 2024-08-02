from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAccountContact(Base, FormatMixins):
    __tablename__ = 'aws_account_contact'
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    address_line_2 = Column('address_line_2', Text, nullable=True)
    address_line_3 = Column('address_line_3', Text, nullable=True)
    company_name = Column('company_name', Text, nullable=True)
    city = Column('city', Text, nullable=True)
    country_code = Column('country_code', Text, nullable=True)
    district_or_county = Column('district_or_county', Text, nullable=True)
    phone_number = Column('phone_number', Text, nullable=True)
    postal_code = Column('postal_code', Text, nullable=True)
    full_name = Column('full_name', Text, nullable=True)
    website_url = Column('website_url', Text, nullable=True)
    linked_account_id = Column('linked_account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    state_or_region = Column('state_or_region', Text, nullable=True)
    address_line_1 = Column('address_line_1', Text, nullable=True)