from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamAccountSummary(Base):
    __tablename__ = 'aws_iam_account_summary'
    access_keys_per_user_quota = Column(name='access_keys_per_user_quota', type_=BigInteger, nullable=True)
    account_access_keys_present = Column(name='account_access_keys_present', type_=BigInteger, nullable=True)
    account_mfa_enabled = Column(name='account_mfa_enabled', type_=Boolean, nullable=True)
    account_signing_certificates_present = Column(name='account_signing_certificates_present', type_=BigInteger, nullable=True)
    assume_role_policy_size_quota = Column(name='assume_role_policy_size_quota', type_=BigInteger, nullable=True)
    attached_policies_per_group_quota = Column(name='attached_policies_per_group_quota', type_=BigInteger, nullable=True)
    attached_policies_per_role_quota = Column(name='attached_policies_per_role_quota', type_=BigInteger, nullable=True)
    attached_policies_per_user_quota = Column(name='attached_policies_per_user_quota', type_=BigInteger, nullable=True)
    global_endpoint_token_version = Column(name='global_endpoint_token_version', type_=BigInteger, nullable=True)
    group_policy_size_quota = Column(name='group_policy_size_quota', type_=BigInteger, nullable=True)
    groups = Column(name='groups', type_=BigInteger, nullable=True)
    groups_per_user_quota = Column(name='groups_per_user_quota', type_=BigInteger, nullable=True)
    groups_quota = Column(name='groups_quota', type_=BigInteger, nullable=True)
    instance_profiles = Column(name='instance_profiles', type_=BigInteger, nullable=True)
    instance_profiles_quota = Column(name='instance_profiles_quota', type_=BigInteger, nullable=True)
    mfa_devices = Column(name='mfa_devices', type_=BigInteger, nullable=True)
    mfa_devices_in_use = Column(name='mfa_devices_in_use', type_=BigInteger, nullable=True)
    policies = Column(name='policies', type_=BigInteger, nullable=True)
    policies_quota = Column(name='policies_quota', type_=BigInteger, nullable=True)
    policy_size_quota = Column(name='policy_size_quota', type_=BigInteger, nullable=True)
    policy_versions_in_use = Column(name='policy_versions_in_use', type_=BigInteger, nullable=True)
    policy_versions_in_use_quota = Column(name='policy_versions_in_use_quota', type_=BigInteger, nullable=True)
    providers = Column(name='providers', type_=BigInteger, nullable=True)
    role_policy_size_quota = Column(name='role_policy_size_quota', type_=BigInteger, nullable=True)
    roles = Column(name='roles', type_=BigInteger, nullable=True)
    roles_quota = Column(name='roles_quota', type_=BigInteger, nullable=True)
    server_certificates = Column(name='server_certificates', type_=BigInteger, nullable=True)
    server_certificates_quota = Column(name='server_certificates_quota', type_=BigInteger, nullable=True)
    signing_certificates_per_user_quota = Column(name='signing_certificates_per_user_quota', type_=BigInteger, nullable=True)
    user_policy_size_quota = Column(name='user_policy_size_quota', type_=BigInteger, nullable=True)
    users = Column(name='users', type_=BigInteger, nullable=True)
    users_quota = Column(name='users_quota', type_=BigInteger, nullable=True)
    versions_per_policy_quota = Column(name='versions_per_policy_quota', type_=BigInteger, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, primary_key=True, nullable=True)