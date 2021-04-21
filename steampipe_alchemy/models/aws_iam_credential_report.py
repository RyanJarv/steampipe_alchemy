from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamCredentialReport(Base):
    __tablename__ = 'aws_iam_credential_report'
    user_name = Column(name='user_name', type_=Text, nullable=True)
    user_arn = Column(name='user_arn', type_=Text, primary_key=True, nullable=True)
    user_creation_time = Column(name='user_creation_time', type_=TIMESTAMP, nullable=True)
    generated_time = Column(name='generated_time', type_=TIMESTAMP, nullable=True)
    access_key_1_active = Column(name='access_key_1_active', type_=Boolean, nullable=True)
    access_key_1_last_rotated = Column(name='access_key_1_last_rotated', type_=TIMESTAMP, nullable=True)
    access_key_1_last_used_date = Column(name='access_key_1_last_used_date', type_=TIMESTAMP, nullable=True)
    access_key_1_last_used_region = Column(name='access_key_1_last_used_region', type_=Text, nullable=True)
    access_key_1_last_used_service = Column(name='access_key_1_last_used_service', type_=Text, nullable=True)
    access_key_2_active = Column(name='access_key_2_active', type_=Boolean, nullable=True)
    access_key_2_last_rotated = Column(name='access_key_2_last_rotated', type_=TIMESTAMP, nullable=True)
    access_key_2_last_used_date = Column(name='access_key_2_last_used_date', type_=TIMESTAMP, nullable=True)
    access_key_2_last_used_region = Column(name='access_key_2_last_used_region', type_=Text, nullable=True)
    access_key_2_last_used_service = Column(name='access_key_2_last_used_service', type_=Text, nullable=True)
    cert_1_active = Column(name='cert_1_active', type_=Boolean, nullable=True)
    cert_1_last_rotated = Column(name='cert_1_last_rotated', type_=TIMESTAMP, nullable=True)
    cert_2_active = Column(name='cert_2_active', type_=Boolean, nullable=True)
    cert_2_last_rotated = Column(name='cert_2_last_rotated', type_=TIMESTAMP, nullable=True)
    mfa_active = Column(name='mfa_active', type_=Boolean, nullable=True)
    password_enabled = Column(name='password_enabled', type_=Boolean, nullable=True)
    password_last_changed = Column(name='password_last_changed', type_=TIMESTAMP, nullable=True)
    password_last_used = Column(name='password_last_used', type_=TIMESTAMP, nullable=True)
    password_status = Column(name='password_status', type_=Text, nullable=True)
    password_next_rotation = Column(name='password_next_rotation', type_=TIMESTAMP, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)