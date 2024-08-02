from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIotFleetMetric(Base, FormatMixins):
    __tablename__ = 'aws_iot_fleet_metric'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    last_modified_date = Column('last_modified_date', TIMESTAMP, nullable=True)
    period = Column('period', BigInteger, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    aggregation_type_values = Column('aggregation_type_values', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    query_version = Column('query_version', Text, nullable=True)
    unit = Column('unit', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    index_name = Column('index_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    aggregation_field = Column('aggregation_field', Text, nullable=True)
    aggregation_type_name = Column('aggregation_type_name', Text, nullable=True)
    metric_name = Column('metric_name', Text, nullable=True)
    query_string = Column('query_string', Text, nullable=True)