from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEmrInstanceGroup(Base, FormatMixins):
    __tablename__ = 'aws_emr_instance_group'
    running_instance_count = Column('running_instance_count', BigInteger, nullable=True)
    autoscaling_policy = Column('autoscaling_policy', JSON, nullable=True)
    configurations = Column('configurations', JSON, nullable=True)
    ebs_block_devices = Column('ebs_block_devices', JSON, nullable=True)
    last_successfully_applied_configurations = Column('last_successfully_applied_configurations', JSON, nullable=True)
    shrink_policy = Column('shrink_policy', JSON, nullable=True)
    state_change_reason = Column('state_change_reason', JSON, nullable=True)
    status_timeline = Column('status_timeline', JSON, nullable=True)
    ebs_optimized = Column('ebs_optimized', Boolean, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    last_successfully_applied_configurations_version = Column('last_successfully_applied_configurations_version', BigInteger, nullable=True)
    configurations_version = Column('configurations_version', BigInteger, nullable=True)
    requested_instance_count = Column('requested_instance_count', BigInteger, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cluster_id = Column('cluster_id', Text, nullable=True)
    instance_group_type = Column('instance_group_type', Text, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    bid_price = Column('bid_price', Text, nullable=True)
    market = Column('market', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)