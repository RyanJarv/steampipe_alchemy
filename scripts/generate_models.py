#!/usr/bin/env python3

from pathlib import Path

from sqlalchemy import MetaData, text, create_engine

metadata = MetaData()
engine = create_engine("postgresql://steampipe:a4eb-4e8b-b0f8@localhost:9193/steampipe?sslmode=disable", echo=True, future=True)

type_mapping = {
    'jsonb': 'JSON',
    'text': 'Text',
    'boolean': 'Boolean',
    'timestamp without time zone': 'TIMESTAMP',
    'bigint': 'BigInteger',
    'cidr': 'psql.CIDR',
    'double precision': 'psql.DOUBLE_PRECISION',
    'inet': 'psql.INET',
}

primary_keys = {
    'aws_iam_action': 'action',
    'aws_iam_account_summary': 'account_id',
    'aws_iam_policy_simulator': 'principal_arn',
    'aws_iam_credential_report': 'user_arn',
    'aws_iam_access_advisor': 'principal_arn',
    'aws_iam_account_password_policy': 'account_id',
}

RootDir = Path(__file__).parent.parent
ModelsDir = (RootDir/Path('steampipe_alchemy/models'))
ModelsDir.mkdir(exist_ok=True)


def normalize_attr(name: str):
    name = name.replace('-', '_')
    if name == 'class':
        name = '_class'
    return name


def snake_case(s: str) -> str:
    return ''.join(map(lambda p: p.capitalize(), s.split('_')))


with engine.connect() as conn:
    result = conn.execute(text("""
        select table_name
            from information_schema.tables
            where table_schema = 'aws'
    """))
    tables = list(map(lambda i: str(i[0]), result.all()))

    init_template = ""
    for table in tables:
        init_template += f"from steampipe_alchemy.models.{table} import {snake_case(table)}\n"

    (ModelsDir/'__init__.py').write_text(init_template)

    for table in tables:
        template = f"""
from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class {snake_case(table)}(Base):
    __tablename__ = '{table}'
        """.rstrip('\n\t ').lstrip('\n\t ')

        result = conn.execute(text(f"""
            select column_name, data_type, is_nullable
                from information_schema.columns
                where table_catalog = 'steampipe'
                    and table_name = '{table}'
        """))

        columns = result.all()
        names = list(map(lambda r: r[0], columns))

        fq_resource_name = '_'.join(table.split('_')[1:])

        # This won't be accurate in cases where steampipe splits the aws service name into several parts. That's
        # ok since we'll be following back to the explicit primary key mappings anyways.
        resource_name = '_'.join(fq_resource_name.split('_')[1:])

        # Also check one less in case it's split into two
        alt_resource_name = '_'.join(resource_name.split('_')[1:])

        # Split up based on priority

        primary_key = None
        for postfix in ['id', 'arn']:
            if f"{fq_resource_name}_{postfix}" in names:
                primary_key = f"{fq_resource_name}_{postfix}"
            elif f"{resource_name}_{postfix}" in names:
                primary_key = f"{resource_name}_{postfix}"
            elif f"{alt_resource_name}_{postfix}" in names:
                primary_key = f"{alt_resource_name}_{postfix}"

        if 'title' in names:
            primary_key = 'title'
        if 'name' in names:
            primary_key = 'name'
        if 'id' in names:
            primary_key = 'id'
        if 'arn' in names:
            primary_key = 'arn'

        # This is checked last to avoid adding extra entries to the primary_keys map
        if not primary_key:
            primary_key = primary_keys[table]

        for name, type, _ in columns:
            if name == primary_key or ((primary_key is list) and primary_key in list):
                row = f"""
    {normalize_attr(name)} = Column('{name}', {type_mapping[type]}, primary_key=True, nullable=True)
                """
            else:
                row = f"""
    {normalize_attr(name)} = Column('{name}', {type_mapping[type]}, nullable=True)
                """

            template += row.lstrip('\t ').rstrip('\n\t ')
        f = (ModelsDir/Path(f'{table}.py'))
        f.write_text(template)
