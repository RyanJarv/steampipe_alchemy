from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamAccountPasswordPolicy(Base):
    __tablename__ = 'aws_iam_account_password_policy'
    allow_users_to_change_password = Column(name='allow_users_to_change_password', type_=Boolean, nullable=True)
    expire_passwords = Column(name='expire_passwords', type_=Boolean, nullable=True)
    hard_expiry = Column(name='hard_expiry', type_=Boolean, nullable=True)
    max_password_age = Column(name='max_password_age', type_=BigInteger, nullable=True)
    minimum_password_length = Column(name='minimum_password_length', type_=BigInteger, nullable=True)
    password_reuse_prevention = Column(name='password_reuse_prevention', type_=BigInteger, nullable=True)
    require_lowercase_characters = Column(name='require_lowercase_characters', type_=Boolean, nullable=True)
    require_numbers = Column(name='require_numbers', type_=Boolean, nullable=True)
    require_symbols = Column(name='require_symbols', type_=Boolean, nullable=True)
    require_uppercase_characters = Column(name='require_uppercase_characters', type_=Boolean, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, primary_key=True, nullable=True)