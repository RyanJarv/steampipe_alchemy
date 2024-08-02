from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53Domain(Base, FormatMixins):
    __tablename__ = 'aws_route53_domain'
    registrant_contact = Column('registrant_contact', JSON, nullable=True)
    status_list = Column('status_list', JSON, nullable=True)
    tech_contact = Column('tech_contact', JSON, nullable=True)
    admin_contact = Column('admin_contact', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    admin_privacy = Column('admin_privacy', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    auto_renew = Column('auto_renew', Boolean, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    expiration_date = Column('expiration_date', TIMESTAMP, nullable=True)
    tech_privacy = Column('tech_privacy', Boolean, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    transfer_lock = Column('transfer_lock', Boolean, nullable=True)
    updated_date = Column('updated_date', TIMESTAMP, nullable=True)
    registrant_privacy = Column('registrant_privacy', Boolean, nullable=True)
    nameservers = Column('nameservers', JSON, nullable=True)
    who_is_server = Column('who_is_server', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    abuse_contact_email = Column('abuse_contact_email', Text, nullable=True)
    abuse_contact_phone = Column('abuse_contact_phone', Text, nullable=True)
    registrar_name = Column('registrar_name', Text, nullable=True)
    registrar_url = Column('registrar_url', Text, nullable=True)
    registry_domain_id = Column('registry_domain_id', Text, nullable=True)
    reseller = Column('reseller', Text, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)