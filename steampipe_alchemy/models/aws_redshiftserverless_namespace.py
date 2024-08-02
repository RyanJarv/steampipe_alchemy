from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRedshiftserverlessNamespace(Base, FormatMixins):
    __tablename__ = 'aws_redshiftserverless_namespace'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    iam_roles = Column('iam_roles', JSON, nullable=True)
    log_exports = Column('log_exports', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    namespace_id = Column('namespace_id', Text, nullable=True)
    namespace_arn = Column('namespace_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    admin_username = Column('admin_username', Text, nullable=True)
    namespace_name = Column('namespace_name', Text, nullable=True)
    db_name = Column('db_name', Text, nullable=True)
    default_iam_role_arn = Column('default_iam_role_arn', Text, nullable=True)