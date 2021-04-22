from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEfsAccessPoint(Base):
    __tablename__ = 'aws_efs_access_point'
    name = Column('name', Text, primary_key=True, nullable=True)
    access_point_id = Column('access_point_id', Text, nullable=True)
    access_point_arn = Column('access_point_arn', Text, nullable=True)
    life_cycle_state = Column('life_cycle_state', Text, nullable=True)
    file_system_id = Column('file_system_id', Text, nullable=True)
    client_token = Column('client_token', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    posix_user = Column('posix_user', JSON, nullable=True)
    root_directory = Column('root_directory', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)