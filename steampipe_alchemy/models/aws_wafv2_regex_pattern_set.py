from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsWafv2RegexPatternSet(Base, FormatMixins):
    __tablename__ = 'aws_wafv2_regex_pattern_set'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    id = Column('id', Text, nullable=True)
    scope = Column('scope', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    lock_token = Column('lock_token', Text, nullable=True)
    regular_expressions = Column('regular_expressions', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsWafv2RegexPatternSetLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_wafv2_regex_pattern_set_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    id = Column('id', Text, nullable=True)
    scope = Column('scope', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    lock_token = Column('lock_token', Text, nullable=True)
    regular_expressions = Column('regular_expressions', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsWafv2RegexPatternSet).select_from(AwsWafv2RegexPatternSet)
create_materialized_view('aws_wafv2_regex_pattern_set_local', cache, db.metadata_materialized)
