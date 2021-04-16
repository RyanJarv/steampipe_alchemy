from sqlalchemy import create_engine, MetaData
from sqlalchemy.future import Engine

from sqlalchemy.ext.declarative import declarative_base

DATABASE_CONNECTION_PATH = 'postgresql://steampipe:a4eb-4e8b-b0f8@localhost:9193/steampipe?sslmode=disable'
engine: Engine = create_engine(DATABASE_CONNECTION_PATH)

metadata = MetaData()

Base = declarative_base(metadata=metadata)
