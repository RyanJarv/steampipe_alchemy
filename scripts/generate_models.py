#!/usr/bin/env python3

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from os import environ
from steampipe_alchemy import AwsConfig, SteamPipe
from sqlalchemy import MetaData, text, create_engine


metadata = MetaData()
steam = SteamPipe()
steam.install(['aws'])
steam.update_config(aws=AwsConfig(
    profile=environ.get('AWS_PROFILE', 'default'),
    regions=['us-east-1'],
))
steam.start()

type_mapping = {
    'jsonb': 'JSON',
    'text': 'Text',
    'boolean': 'Boolean',
    'timestamp without time zone': 'TIMESTAMP',
    'timestamp with time zone': 'TIMESTAMP',
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
    'aws_iam_policy_attachment': 'policy_arn',
    'aws_emr_block_public_access_configuration': 'creation_date',
    'aws_ecr_image': ['repository_name', 'image_digest'],
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


with steam.engine.connect() as conn:
    result = conn.execute(text("""
        select table_name
            from information_schema.tables
            where table_schema = 'aws'
    """))
    tables = list(map(lambda i: str(i[0]), result.all()))

    # import pdb; pdb.set_trace()
    tables = [
        t for t in tables
        if ('_metric_' not in t)
           and ('_cost_' not in t)
           and ('statistics' not in t)
           and ('notification' not in t)
           and ('_report' not in t)
           and (t not in ['aws_vpc_flow_log_event', 'aws_pricing_product'])
    ]

    # table_map = {
    #     f'"{snake_case(table).removeprefix("Aws")}"': snake_case(table)
    #     for table in tables
    # }
    table_list = [f'  "{snake_case(t).removeprefix("Aws")}": {snake_case(t)},' for t in tables[:-1]]
    table_list.append(f'  "{snake_case(tables[-1]).removeprefix("Aws")}": {snake_case(tables[-1])}')
    table_list = '\n'.join(table_list)

    # (ModelsDir / Path(f'all.py')).write_text( )

    init_template = ""
    for table in tables:
        init_template += f"from steampipe_alchemy.models.{table} import {snake_case(table)}\n"
    init_template += f"""

all = {{
{table_list}
}}
        """


    (ModelsDir/'__init__.py').write_text(init_template)


    for table in tables:
        print(table, end=': ')
        template = f"""
from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class {snake_case(table)}(Base, FormatMixins):
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
            try:
                primary_key = primary_keys[table]
            except KeyError:
                print(f"Need to add primary key for: {table}")
                continue

        for name, type, _ in columns:
            if name == primary_key or ((primary_key is list) and primary_key in list):
                row = f"""
    {normalize_attr(name)} = Column('{name}', {type_mapping[type]}, primary_key=True, nullable=True)
                """
            else:
                try:
                    row = f"""
    {normalize_attr(name)} = Column('{name}', {type_mapping[type]}, nullable=True)
                    """
                except KeyError:
                    print(f"Need to add type mapping for: {type} in {table}")
                    continue


            template += row.lstrip('\t ').rstrip('\n\t ')
        f = (ModelsDir/Path(f'{table}.py'))
        f.write_text(template)
        print('done')


#subprocess.check_output(['git', 'apply', './patches/models.diff'])
