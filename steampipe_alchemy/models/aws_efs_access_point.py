from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEfsAccessPoint(Base):
    __tablename__ = 'aws_efs_access_point'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    access_point_id = Column(name='access_point_id', type_=Text, nullable=True)
    access_point_arn = Column(name='access_point_arn', type_=Text, nullable=True)
    life_cycle_state = Column(name='life_cycle_state', type_=Text, nullable=True)
    file_system_id = Column(name='file_system_id', type_=Text, nullable=True)
    client_token = Column(name='client_token', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    posix_user = Column(name='posix_user', type_=JSON, nullable=True)
    root_directory = Column(name='root_directory', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)