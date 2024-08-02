from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsmManagedInstancePatchState(Base, FormatMixins):
    __tablename__ = 'aws_ssm_managed_instance_patch_state'
    _ctx = Column('_ctx', JSON, nullable=True)
    failed_count = Column('failed_count', BigInteger, nullable=True)
    installed_count = Column('installed_count', BigInteger, nullable=True)
    installed_other_count = Column('installed_other_count', BigInteger, nullable=True)
    installed_pending_reboot_count = Column('installed_pending_reboot_count', BigInteger, nullable=True)
    installed_rejected_count = Column('installed_rejected_count', BigInteger, nullable=True)
    last_no_reboot_install_operation_time = Column('last_no_reboot_install_operation_time', TIMESTAMP, nullable=True)
    missing_count = Column('missing_count', BigInteger, nullable=True)
    not_applicable_count = Column('not_applicable_count', BigInteger, nullable=True)
    other_non_compliant_count = Column('other_non_compliant_count', BigInteger, nullable=True)
    security_non_compliant_count = Column('security_non_compliant_count', BigInteger, nullable=True)
    unreported_not_applicable_count = Column('unreported_not_applicable_count', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    operation_end_time = Column('operation_end_time', TIMESTAMP, nullable=True)
    operation_start_time = Column('operation_start_time', TIMESTAMP, nullable=True)
    critical_non_compliant_count = Column('critical_non_compliant_count', BigInteger, nullable=True)
    baseline_id = Column('baseline_id', Text, nullable=True)
    operation = Column('operation', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    patch_group = Column('patch_group', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    owner_information = Column('owner_information', Text, nullable=True)
    reboot_option = Column('reboot_option', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    snapshot_id = Column('snapshot_id', Text, nullable=True)
    instance_id = Column('instance_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)