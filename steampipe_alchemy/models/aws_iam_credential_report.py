from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamCredentialReport(Base):
    __tablename__ = 'aws_iam_credential_report'
    user_name = Column('user_name', Text, nullable=True)
    user_arn = Column('user_arn', Text, primary_key=True, nullable=True)
    user_creation_time = Column('user_creation_time', TIMESTAMP, nullable=True)
    generated_time = Column('generated_time', TIMESTAMP, nullable=True)
    access_key_1_active = Column('access_key_1_active', Boolean, nullable=True)
    access_key_1_last_rotated = Column('access_key_1_last_rotated', TIMESTAMP, nullable=True)
    access_key_1_last_used_date = Column('access_key_1_last_used_date', TIMESTAMP, nullable=True)
    access_key_1_last_used_region = Column('access_key_1_last_used_region', Text, nullable=True)
    access_key_1_last_used_service = Column('access_key_1_last_used_service', Text, nullable=True)
    access_key_2_active = Column('access_key_2_active', Boolean, nullable=True)
    access_key_2_last_rotated = Column('access_key_2_last_rotated', TIMESTAMP, nullable=True)
    access_key_2_last_used_date = Column('access_key_2_last_used_date', TIMESTAMP, nullable=True)
    access_key_2_last_used_region = Column('access_key_2_last_used_region', Text, nullable=True)
    access_key_2_last_used_service = Column('access_key_2_last_used_service', Text, nullable=True)
    cert_1_active = Column('cert_1_active', Boolean, nullable=True)
    cert_1_last_rotated = Column('cert_1_last_rotated', TIMESTAMP, nullable=True)
    cert_2_active = Column('cert_2_active', Boolean, nullable=True)
    cert_2_last_rotated = Column('cert_2_last_rotated', TIMESTAMP, nullable=True)
    mfa_active = Column('mfa_active', Boolean, nullable=True)
    password_enabled = Column('password_enabled', Boolean, nullable=True)
    password_last_changed = Column('password_last_changed', TIMESTAMP, nullable=True)
    password_last_used = Column('password_last_used', TIMESTAMP, nullable=True)
    password_status = Column('password_status', Text, nullable=True)
    password_next_rotation = Column('password_next_rotation', TIMESTAMP, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)