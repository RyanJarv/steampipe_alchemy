from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCognitoUserPool(Base, FormatMixins):
    __tablename__ = 'aws_cognito_user_pool'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    device_configuration = Column('device_configuration', JSON, nullable=True)
    email_configuration = Column('email_configuration', JSON, nullable=True)
    estimated_number_of_users = Column('estimated_number_of_users', BigInteger, nullable=True)
    lambda_config = Column('lambda_config', JSON, nullable=True)
    last_modified_date = Column('last_modified_date', TIMESTAMP, nullable=True)
    policies = Column('policies', JSON, nullable=True)
    schema_attributes = Column('schema_attributes', JSON, nullable=True)
    sms_configuration = Column('sms_configuration', JSON, nullable=True)
    user_attribute_update_settings = Column('user_attribute_update_settings', JSON, nullable=True)
    user_pool_add_ons = Column('user_pool_add_ons', JSON, nullable=True)
    username_attributes = Column('username_attributes', JSON, nullable=True)
    username_configuration = Column('username_configuration', JSON, nullable=True)
    verification_message_template = Column('verification_message_template', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_recovery_setting = Column('account_recovery_setting', JSON, nullable=True)
    admin_create_user_config = Column('admin_create_user_config', JSON, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sms_authentication_message = Column('sms_authentication_message', Text, nullable=True)
    alias_attributes = Column('alias_attributes', Text, nullable=True)
    auto_verified_attributes = Column('auto_verified_attributes', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    custom_domain = Column('custom_domain', Text, nullable=True)
    deletion_protection = Column('deletion_protection', Text, nullable=True)
    sms_configuration_failure = Column('sms_configuration_failure', Text, nullable=True)
    domain = Column('domain', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    mfa_configuration = Column('mfa_configuration', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    region = Column('region', Text, nullable=True)