from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamAccountPasswordPolicy(Base):
    __tablename__ = 'aws_iam_account_password_policy'
    allow_users_to_change_password = Column(Boolean, name='allow_users_to_change_password', nullable=True)
    expire_passwords = Column(Boolean, name='expire_passwords', nullable=True)
    hard_expiry = Column(Boolean, name='hard_expiry', nullable=True)
    max_password_age = Column(BigInteger, name='max_password_age', nullable=True)
    minimum_password_length = Column(BigInteger, name='minimum_password_length', nullable=True)
    password_reuse_prevention = Column(BigInteger, name='password_reuse_prevention', nullable=True)
    require_lowercase_characters = Column(Boolean, name='require_lowercase_characters', nullable=True)
    require_numbers = Column(Boolean, name='require_numbers', nullable=True)
    require_symbols = Column(Boolean, name='require_symbols', nullable=True)
    require_uppercase_characters = Column(Boolean, name='require_uppercase_characters', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', primary_key=True, nullable=True)