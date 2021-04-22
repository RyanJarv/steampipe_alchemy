import json
import sys
import typing
from ctypes import Union
from pathlib import Path
from typing import List, Any

import psycopg2.errors
import sqlalchemy.exc
from sqlalchemy import MetaData, create_engine, text

metadata = MetaData()
engine = create_engine("postgresql://steampipe:a4eb-4e8b-b0f8@localhost:9193/steampipe?sslmode=disable", echo=True,
                       future=True)


def convert_types(d: dict) -> dict:
    new = {}
    for k, v in d.items():
        if type(v) is dict:
            # If it's a dict recurse and return the subtypes
            new[k] = convert_types(v)
        elif type(v) is list:
            # Lists are a List of a single type or a Union of all types in the list
            types_ = set([type(i).__name__ for i in v])
            if len(types_) == 0:
                # List has no types, probably because this resource doesn't exist at the moment
                # just need to rerun when it does.
                #
                # For now set as Any
                new[k] = 'Any'
            elif len(types_) == 1:
                type_ = list(types_)[0]

                # Same as above
                if type_ is type(None):
                    type_ = 'Any'

                new[k] = List[type_]
            else:
                types_ = filter(lambda t: t is None, types_)
                new[k] = List[Union[tuple(types_)]]
        elif type(v) is str:
            # Any other type just gets added
            new[k] = 'str'
        elif type(v) is bool:
            # Any other type just gets added
            new[k] = 'bool'
        elif v is None:
            # Same as above, no resources so can't determine type.
            new[k] = 'Any'
        else:
            UserWarning(f"Unknown type: {type(v)}")
    return new


with engine.connect() as conn:
    tables = conn.execute(text("""
        select table_name
            from information_schema.tables
            where table_catalog = 'steampipe'
                and table_schema = 'aws'
    """))

    tables = tables.all()


table_columns = {}
for table in tables:
    table_types = '''
import typing
from typing import ForwardRef


    '''
    table = table[0]

    with engine.connect() as conn:
        try:
            columns = conn.execute(text(f"""
                    select column_name from
                        information_schema.columns
                        where table_catalog = 'steampipe'
                            and table_name = '{table}'
                            and data_type = 'jsonb'
                """))
        except sqlalchemy.exc.InternalError as e:
            # Not sure what is causing this, print and continue on
            print(f"[ERROR] {e}", file=sys.stderr)
            continue
        except Exception as e:
            try:
                psycopg2.errors.lookup(e)
                # Not sure what is causing this, print and continue on
                print(f"[ERROR] {e}", file=sys.stderr)
                continue
            except Exception:
                raise e


        found_types = False

        for column in columns.all():
            column = column[0]

            try:
                result = conn.execute(text(f"""
                    select {column} from {table}
                """)).first()
            except sqlalchemy.exc.OperationalError as e:
                if 'hydrate' in str(e.orig):
                    print("[ERROR] " + str(e.orig))
                    continue
                elif "call requires an '='" in str(e.orig):
                    print("[ERROR] " + str(e.orig))
                    continue
                else:
                    import pdb;

                    pdb.set_trace()
                    raise e

            # Likely no resources of this type in the account. Will need to rerun this when this resource exists.
            if not result:
                continue

            f = Path('steampipe_alchemy') / 'models' / f"{table}.py"
            name = ''.join([s.capitalize() for s in column.split('_')])
            f.write_text(f.read_text().replace(f"{column} = ", f"{column}: {name} = "))

            type_ = convert_types(dict(result))

            table_types += f"""
{name} = typing.TypedDict('{name}',
    {type_}
)
"""
            found_types = True

    if found_types:
        f = Path('steampipe_alchemy') / 'types' / f"{table}.py"
        f.write_text(table_types)
