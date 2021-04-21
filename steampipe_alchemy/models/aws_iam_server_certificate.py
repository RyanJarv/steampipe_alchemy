from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamServerCertificate(Base):
    __tablename__ = 'aws_iam_server_certificate'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    server_certificate_id = Column(name='server_certificate_id', type_=Text, nullable=True)
    expiration = Column(name='expiration', type_=TIMESTAMP, nullable=True)
    certificate_body = Column(name='certificate_body', type_=Text, nullable=True)
    certificate_chain = Column(name='certificate_chain', type_=Text, nullable=True)
    path = Column(name='path', type_=Text, nullable=True)
    upload_date = Column(name='upload_date', type_=TIMESTAMP, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)