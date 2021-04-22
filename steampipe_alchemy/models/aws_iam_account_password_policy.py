from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamAccountPasswordPolicy(Base):
    __tablename__ = 'aws_iam_account_password_policy'
    allow_users_to_change_password = Column('allow_users_to_change_password', Boolean, nullable=True)
    expire_passwords = Column('expire_passwords', Boolean, nullable=True)
    hard_expiry = Column('hard_expiry', Boolean, nullable=True)
    max_password_age = Column('max_password_age', BigInteger, nullable=True)
    minimum_password_length = Column('minimum_password_length', BigInteger, nullable=True)
    password_reuse_prevention = Column('password_reuse_prevention', BigInteger, nullable=True)
    require_lowercase_characters = Column('require_lowercase_characters', Boolean, nullable=True)
    require_numbers = Column('require_numbers', Boolean, nullable=True)
    require_symbols = Column('require_symbols', Boolean, nullable=True)
    require_uppercase_characters = Column('require_uppercase_characters', Boolean, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, primary_key=True, nullable=True)