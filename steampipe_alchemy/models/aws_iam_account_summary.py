from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamAccountSummary(Base):
    __tablename__ = 'aws_iam_account_summary'
    access_keys_per_user_quota = Column(BigInteger, name='access_keys_per_user_quota', nullable=True)
    account_access_keys_present = Column(BigInteger, name='account_access_keys_present', nullable=True)
    account_mfa_enabled = Column(Boolean, name='account_mfa_enabled', nullable=True)
    account_signing_certificates_present = Column(BigInteger, name='account_signing_certificates_present', nullable=True)
    assume_role_policy_size_quota = Column(BigInteger, name='assume_role_policy_size_quota', nullable=True)
    attached_policies_per_group_quota = Column(BigInteger, name='attached_policies_per_group_quota', nullable=True)
    attached_policies_per_role_quota = Column(BigInteger, name='attached_policies_per_role_quota', nullable=True)
    attached_policies_per_user_quota = Column(BigInteger, name='attached_policies_per_user_quota', nullable=True)
    global_endpoint_token_version = Column(BigInteger, name='global_endpoint_token_version', nullable=True)
    group_policy_size_quota = Column(BigInteger, name='group_policy_size_quota', nullable=True)
    groups = Column(BigInteger, name='groups', nullable=True)
    groups_per_user_quota = Column(BigInteger, name='groups_per_user_quota', nullable=True)
    groups_quota = Column(BigInteger, name='groups_quota', nullable=True)
    instance_profiles = Column(BigInteger, name='instance_profiles', nullable=True)
    instance_profiles_quota = Column(BigInteger, name='instance_profiles_quota', nullable=True)
    mfa_devices = Column(BigInteger, name='mfa_devices', nullable=True)
    mfa_devices_in_use = Column(BigInteger, name='mfa_devices_in_use', nullable=True)
    policies = Column(BigInteger, name='policies', nullable=True)
    policies_quota = Column(BigInteger, name='policies_quota', nullable=True)
    policy_size_quota = Column(BigInteger, name='policy_size_quota', nullable=True)
    policy_versions_in_use = Column(BigInteger, name='policy_versions_in_use', nullable=True)
    policy_versions_in_use_quota = Column(BigInteger, name='policy_versions_in_use_quota', nullable=True)
    providers = Column(BigInteger, name='providers', nullable=True)
    role_policy_size_quota = Column(BigInteger, name='role_policy_size_quota', nullable=True)
    roles = Column(BigInteger, name='roles', nullable=True)
    roles_quota = Column(BigInteger, name='roles_quota', nullable=True)
    server_certificates = Column(BigInteger, name='server_certificates', nullable=True)
    server_certificates_quota = Column(BigInteger, name='server_certificates_quota', nullable=True)
    signing_certificates_per_user_quota = Column(BigInteger, name='signing_certificates_per_user_quota', nullable=True)
    user_policy_size_quota = Column(BigInteger, name='user_policy_size_quota', nullable=True)
    users = Column(BigInteger, name='users', nullable=True)
    users_quota = Column(BigInteger, name='users_quota', nullable=True)
    versions_per_policy_quota = Column(BigInteger, name='versions_per_policy_quota', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', primary_key=True, nullable=True)