from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodestarNotificationRule(Base, FormatMixins):
    __tablename__ = 'aws_codestar_notification_rule'
        _ctx = Column('_ctx', JSON, nullable=True)
        created_timestamp = Column('created_timestamp', TIMESTAMP, nullable=True)
        last_modified_timestamp = Column('last_modified_timestamp', TIMESTAMP, nullable=True)
        event_types = Column('event_types', JSON, nullable=True)
        targets = Column('targets', JSON, nullable=True)
        tags = Column('tags', JSON, nullable=True)
        akas = Column('akas', JSON, nullable=True)
        sp_ctx = Column('sp_ctx', JSON, nullable=True)
        target_address = Column('target_address', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
        partition = Column('partition', Text, nullable=True)
        region = Column('region', Text, nullable=True)
        account_id = Column('account_id', Text, nullable=True)
        title = Column('title', Text, nullable=True)
        sp_connection_name = Column('sp_connection_name', Text, nullable=True)
        id = Column('id', Text, nullable=True)
        name = Column('name', Text, nullable=True)
        resource = Column('resource', Text, nullable=True)
        detail_type = Column('detail_type', Text, nullable=True)
        status = Column('status', Text, nullable=True)
        created_by = Column('created_by', Text, nullable=True)
        event_type_id = Column('event_type_id', Text, nullable=True)