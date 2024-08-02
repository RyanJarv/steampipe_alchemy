from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEmrInstance(Base, FormatMixins):
    __tablename__ = 'aws_emr_instance'
    _ctx = Column('_ctx', JSON, nullable=True)
    private_ip_address = Column('private_ip_address', psql.INET, nullable=True)
    public_ip_address = Column('public_ip_address', psql.INET, nullable=True)
    ebs_volumes = Column('ebs_volumes', JSON, nullable=True)
    state_change_reason = Column('state_change_reason', JSON, nullable=True)
    status_timeline = Column('status_timeline', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    private_dns_name = Column('private_dns_name', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    public_dns_name = Column('public_dns_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    cluster_id = Column('cluster_id', Text, nullable=True)
    ec2_instance_id = Column('ec2_instance_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    instance_fleet_id = Column('instance_fleet_id', Text, nullable=True)
    instance_group_id = Column('instance_group_id', Text, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    market = Column('market', Text, nullable=True)