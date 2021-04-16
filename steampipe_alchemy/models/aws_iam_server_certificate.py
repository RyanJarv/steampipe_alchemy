from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamServerCertificate(Base):
    __tablename__ = 'aws_iam_server_certificate'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    server_certificate_id = Column(Text, name='server_certificate_id', nullable=True)
    expiration = Column(TIMESTAMP, name='expiration', nullable=True)
    certificate_body = Column(Text, name='certificate_body', nullable=True)
    certificate_chain = Column(Text, name='certificate_chain', nullable=True)
    path = Column(Text, name='path', nullable=True)
    upload_date = Column(TIMESTAMP, name='upload_date', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)