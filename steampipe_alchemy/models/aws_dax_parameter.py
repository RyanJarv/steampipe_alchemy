from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDaxParameter(Base, FormatMixins):
    __tablename__ = 'aws_dax_parameter'
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    parameter_value = Column('parameter_value', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    allowed_values = Column('allowed_values', Text, nullable=True)
    change_type = Column('change_type', Text, nullable=True)
    data_type = Column('data_type', Text, nullable=True)
    is_modifiable = Column('is_modifiable', Text, nullable=True)
    parameter_name = Column('parameter_name', Text, nullable=True)
    source = Column('source', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    parameter_type = Column('parameter_type', Text, nullable=True)
    parameter_group_name = Column('parameter_group_name', Text, nullable=True)