from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEfsAccessPoint(Base):
    __tablename__ = 'aws_efs_access_point'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    access_point_id = Column(Text, name='access_point_id', nullable=True)
    access_point_arn = Column(Text, name='access_point_arn', nullable=True)
    life_cycle_state = Column(Text, name='life_cycle_state', nullable=True)
    file_system_id = Column(Text, name='file_system_id', nullable=True)
    client_token = Column(Text, name='client_token', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    posix_user = Column(JSON, name='posix_user', nullable=True)
    root_directory = Column(JSON, name='root_directory', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)