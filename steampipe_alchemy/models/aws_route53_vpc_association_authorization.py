from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53VpcAssociationAuthorization(Base, FormatMixins):
    __tablename__ = 'aws_route53_vpc_association_authorization'
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    vpc_region = Column('vpc_region', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    hosted_zone_id = Column('hosted_zone_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)