from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlueCrawler(Base, FormatMixins):
    __tablename__ = 'aws_glue_crawler'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    crawl_elapsed_time = Column('crawl_elapsed_time', BigInteger, nullable=True)
    last_updated = Column('last_updated', TIMESTAMP, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    classifiers = Column('classifiers', JSON, nullable=True)
    configuration = Column('configuration', JSON, nullable=True)
    last_crawl = Column('last_crawl', JSON, nullable=True)
    schedule = Column('schedule', JSON, nullable=True)
    schema_change_policy = Column('schema_change_policy', JSON, nullable=True)
    targets = Column('targets', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    database_name = Column('database_name', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    role = Column('role', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    crawler_lineage_settings = Column('crawler_lineage_settings', Text, nullable=True)
    crawler_security_configuration = Column('crawler_security_configuration', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    recrawl_behavior = Column('recrawl_behavior', Text, nullable=True)
    table_prefix = Column('table_prefix', Text, nullable=True)