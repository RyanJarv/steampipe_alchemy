"""Main module."""
from sqlalchemy import select

from models import aws_vpc
from base import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine, future=True)

select(aws_vpc.AwsVpc.account_id)

