from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRdsDbRecommendation(Base, FormatMixins):
    __tablename__ = 'aws_rds_db_recommendation'
    updated_time = Column('updated_time', TIMESTAMP, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    issue_details = Column('issue_details', JSON, nullable=True)
    links = Column('links', JSON, nullable=True)
    recommended_actions = Column('recommended_actions', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    reason = Column('reason', Text, nullable=True)
    recommendation = Column('recommendation', Text, nullable=True)
    severity = Column('severity', Text, nullable=True)
    source = Column('source', Text, nullable=True)
    recommendation_id = Column('recommendation_id', Text, nullable=True)
    type_id = Column('type_id', Text, nullable=True)
    type_recommendation = Column('type_recommendation', Text, nullable=True)
    additional_info = Column('additional_info', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    type_detection = Column('type_detection', Text, nullable=True)
    resource_arn = Column('resource_arn', Text, nullable=True)
    category = Column('category', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    detection = Column('detection', Text, nullable=True)
    impact = Column('impact', Text, nullable=True)