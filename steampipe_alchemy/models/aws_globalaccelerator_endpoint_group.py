from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlobalacceleratorEndpointGroup(Base, FormatMixins):
    __tablename__ = 'aws_globalaccelerator_endpoint_group'
    _ctx = Column('_ctx', JSON, nullable=True)
    endpoint_descriptions = Column('endpoint_descriptions', JSON, nullable=True)
    health_check_interval_seconds = Column('health_check_interval_seconds', BigInteger, nullable=True)
    health_check_port = Column('health_check_port', BigInteger, nullable=True)
    port_overrides = Column('port_overrides', JSON, nullable=True)
    threshold_count = Column('threshold_count', BigInteger, nullable=True)
    traffic_dial_percentage = Column('traffic_dial_percentage', psql.DOUBLE_PRECISION, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    listener_arn = Column('listener_arn', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    endpoint_group_region = Column('endpoint_group_region', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    health_check_path = Column('health_check_path', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    health_check_protocol = Column('health_check_protocol', Text, nullable=True)
    region = Column('region', Text, nullable=True)