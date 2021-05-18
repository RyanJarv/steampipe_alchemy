import sqlalchemy.exc
from sqlalchemy_utils.view import compile_create_materialized_view
from sqlalchemy_utils.view import CreateView
from sqlalchemy.ext import compiler

from steampipe_alchemy.db import status, query, metadata_materialized
from steampipe_alchemy.models.aws_vpc import AwsVpcLocal


@compiler.compiles(CreateView)
def compile_create_materialized_view(element, compiler, **kw):
    return "CREATE {}VIEW IF NOT EXISTS {} AS {}".format(
        "MATERIALIZED " if element.materialized else "",
        element.name,
        compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


_, _, engine = status()

# metadata_materialized.drop_all(bind=engine, checkfirst=True)
metadata_materialized.create_all(bind=engine, checkfirst=True)

for i in query(AwsVpcLocal).limit(3):
    print(i.to_dict())

