from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsIamServerCertificate(Base, FormatMixins):
    __tablename__ = 'aws_iam_server_certificate'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    server_certificate_id = Column('server_certificate_id', Text, nullable=True)
    expiration = Column('expiration', TIMESTAMP, nullable=True)
    certificate_body = Column('certificate_body', Text, nullable=True)
    certificate_chain = Column('certificate_chain', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    upload_date = Column('upload_date', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsIamServerCertificateLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_iam_server_certificate_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    server_certificate_id = Column('server_certificate_id', Text, nullable=True)
    expiration = Column('expiration', TIMESTAMP, nullable=True)
    certificate_body = Column('certificate_body', Text, nullable=True)
    certificate_chain = Column('certificate_chain', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    upload_date = Column('upload_date', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsIamServerCertificate).select_from(AwsIamServerCertificate)
create_materialized_view('aws_iam_server_certificate_local', cache, db.metadata_materialized)
