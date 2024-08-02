from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsServicecatalogProduct(Base, FormatMixins):
    __tablename__ = 'aws_servicecatalog_product'
    akas = Column('akas', JSON, nullable=True)
    budgets = Column('budgets', JSON, nullable=True)
    launch_paths = Column('launch_paths', JSON, nullable=True)
    provisioning_artifacts = Column('provisioning_artifacts', JSON, nullable=True)
    has_default_path = Column('has_default_path', Boolean, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    owner = Column('owner', Text, nullable=True)
    short_description = Column('short_description', Text, nullable=True)
    support_description = Column('support_description', Text, nullable=True)
    support_email = Column('support_email', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    support_url = Column('support_url', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    product_id = Column('product_id', Text, nullable=True)
    source_product_id = Column('source_product_id', Text, nullable=True)
    distributor = Column('distributor', Text, nullable=True)
    accept_language = Column('accept_language', Text, nullable=True)
    full_text_search = Column('full_text_search', Text, nullable=True)