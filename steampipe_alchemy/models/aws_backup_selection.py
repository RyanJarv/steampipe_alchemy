from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsBackupSelection(Base, FormatMixins):
    __tablename__ = 'aws_backup_selection'
    akas = Column('akas', JSON, nullable=True)
    list_of_tags = Column('list_of_tags', JSON, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    creator_request_id = Column('creator_request_id', Text, nullable=True)
    iam_role_arn = Column('iam_role_arn', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    selection_name = Column('selection_name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    selection_id = Column('selection_id', Text, nullable=True)
    backup_plan_id = Column('backup_plan_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)