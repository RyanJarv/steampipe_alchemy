from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamAccountSummary(Base):
    __tablename__ = 'aws_iam_account_summary'
    access_keys_per_user_quota = Column('access_keys_per_user_quota', BigInteger, nullable=True)
    account_access_keys_present = Column('account_access_keys_present', BigInteger, nullable=True)
    account_mfa_enabled = Column('account_mfa_enabled', Boolean, nullable=True)
    account_signing_certificates_present = Column('account_signing_certificates_present', BigInteger, nullable=True)
    assume_role_policy_size_quota = Column('assume_role_policy_size_quota', BigInteger, nullable=True)
    attached_policies_per_group_quota = Column('attached_policies_per_group_quota', BigInteger, nullable=True)
    attached_policies_per_role_quota = Column('attached_policies_per_role_quota', BigInteger, nullable=True)
    attached_policies_per_user_quota = Column('attached_policies_per_user_quota', BigInteger, nullable=True)
    global_endpoint_token_version = Column('global_endpoint_token_version', BigInteger, nullable=True)
    group_policy_size_quota = Column('group_policy_size_quota', BigInteger, nullable=True)
    groups = Column('groups', BigInteger, nullable=True)
    groups_per_user_quota = Column('groups_per_user_quota', BigInteger, nullable=True)
    groups_quota = Column('groups_quota', BigInteger, nullable=True)
    instance_profiles = Column('instance_profiles', BigInteger, nullable=True)
    instance_profiles_quota = Column('instance_profiles_quota', BigInteger, nullable=True)
    mfa_devices = Column('mfa_devices', BigInteger, nullable=True)
    mfa_devices_in_use = Column('mfa_devices_in_use', BigInteger, nullable=True)
    policies = Column('policies', BigInteger, nullable=True)
    policies_quota = Column('policies_quota', BigInteger, nullable=True)
    policy_size_quota = Column('policy_size_quota', BigInteger, nullable=True)
    policy_versions_in_use = Column('policy_versions_in_use', BigInteger, nullable=True)
    policy_versions_in_use_quota = Column('policy_versions_in_use_quota', BigInteger, nullable=True)
    providers = Column('providers', BigInteger, nullable=True)
    role_policy_size_quota = Column('role_policy_size_quota', BigInteger, nullable=True)
    roles = Column('roles', BigInteger, nullable=True)
    roles_quota = Column('roles_quota', BigInteger, nullable=True)
    server_certificates = Column('server_certificates', BigInteger, nullable=True)
    server_certificates_quota = Column('server_certificates_quota', BigInteger, nullable=True)
    signing_certificates_per_user_quota = Column('signing_certificates_per_user_quota', BigInteger, nullable=True)
    user_policy_size_quota = Column('user_policy_size_quota', BigInteger, nullable=True)
    users = Column('users', BigInteger, nullable=True)
    users_quota = Column('users_quota', BigInteger, nullable=True)
    versions_per_policy_quota = Column('versions_per_policy_quota', BigInteger, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, primary_key=True, nullable=True)