from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamCredentialReport(Base):
    __tablename__ = 'aws_iam_credential_report'
    user_name = Column(Text, name='user_name', nullable=True)
    user_arn = Column(Text, name='user_arn', primary_key=True, nullable=True)
    user_creation_time = Column(TIMESTAMP, name='user_creation_time', nullable=True)
    generated_time = Column(TIMESTAMP, name='generated_time', nullable=True)
    access_key_1_active = Column(Boolean, name='access_key_1_active', nullable=True)
    access_key_1_last_rotated = Column(TIMESTAMP, name='access_key_1_last_rotated', nullable=True)
    access_key_1_last_used_date = Column(TIMESTAMP, name='access_key_1_last_used_date', nullable=True)
    access_key_1_last_used_region = Column(Text, name='access_key_1_last_used_region', nullable=True)
    access_key_1_last_used_service = Column(Text, name='access_key_1_last_used_service', nullable=True)
    access_key_2_active = Column(Boolean, name='access_key_2_active', nullable=True)
    access_key_2_last_rotated = Column(TIMESTAMP, name='access_key_2_last_rotated', nullable=True)
    access_key_2_last_used_date = Column(TIMESTAMP, name='access_key_2_last_used_date', nullable=True)
    access_key_2_last_used_region = Column(Text, name='access_key_2_last_used_region', nullable=True)
    access_key_2_last_used_service = Column(Text, name='access_key_2_last_used_service', nullable=True)
    cert_1_active = Column(Boolean, name='cert_1_active', nullable=True)
    cert_1_last_rotated = Column(TIMESTAMP, name='cert_1_last_rotated', nullable=True)
    cert_2_active = Column(Boolean, name='cert_2_active', nullable=True)
    cert_2_last_rotated = Column(TIMESTAMP, name='cert_2_last_rotated', nullable=True)
    mfa_active = Column(Boolean, name='mfa_active', nullable=True)
    password_enabled = Column(Boolean, name='password_enabled', nullable=True)
    password_last_changed = Column(TIMESTAMP, name='password_last_changed', nullable=True)
    password_last_used = Column(TIMESTAMP, name='password_last_used', nullable=True)
    password_status = Column(Text, name='password_status', nullable=True)
    password_next_rotation = Column(TIMESTAMP, name='password_next_rotation', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)