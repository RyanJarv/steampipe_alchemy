from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlobalacceleratorListener(Base, FormatMixins):
    __tablename__ = 'aws_globalaccelerator_listener'
    _ctx = Column('_ctx', JSON, nullable=True)
    port_ranges = Column('port_ranges', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    protocol = Column('protocol', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    accelerator_arn = Column('accelerator_arn', Text, nullable=True)
    client_affinity = Column('client_affinity', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)