from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcEipAddressTransfer(Base, FormatMixins):
    __tablename__ = 'aws_vpc_eip_address_transfer'
    transfer_offer_expiration_timestamp = Column('transfer_offer_expiration_timestamp', TIMESTAMP, nullable=True)
    transfer_offer_accepted_timestamp = Column('transfer_offer_accepted_timestamp', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    allocation_id = Column('allocation_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    address_transfer_status = Column('address_transfer_status', Text, nullable=True)
    public_ip = Column('public_ip', Text, nullable=True)
    transfer_account_id = Column('transfer_account_id', Text, nullable=True)