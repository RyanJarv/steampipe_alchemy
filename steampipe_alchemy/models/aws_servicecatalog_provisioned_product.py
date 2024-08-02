from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsServicecatalogProvisionedProduct(Base, FormatMixins):
    __tablename__ = 'aws_servicecatalog_provisioned_product'
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    cloud_watch_dashboards = Column('cloud_watch_dashboards', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    last_record_id = Column('last_record_id', Text, nullable=True)
    last_successful_provisioning_record_id = Column('last_successful_provisioning_record_id', Text, nullable=True)
    launch_role_arn = Column('launch_role_arn', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    product_id = Column('product_id', Text, nullable=True)
    provisioning_artifact_id = Column('provisioning_artifact_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    idempotency_token = Column('idempotency_token', Text, nullable=True)
    last_provisioning_record_id = Column('last_provisioning_record_id', Text, nullable=True)
    accept_language = Column('accept_language', Text, nullable=True)