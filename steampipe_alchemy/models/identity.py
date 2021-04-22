import datetime
from typing import TYPE_CHECKING

from typing import List

import sqlalchemy as sa  # type: ignore
from sqlalchemy import TIMESTAMP
from sqlalchemy_utils import JSONType  # type: ignore

from steampipe_alchemy import Base

if TYPE_CHECKING:
    import mypy_boto3_iam
    import mypy_boto3_iam.type_defs

class Identity(Base):
    def __init__(self, resp):
        super().__init__(**resp)

    __tablename__ = "identity"

    path: str = sa.Column(sa.String)
    arn: str = sa.Column(sa.String, primary_key=True)
    create_date: datetime.datetime = sa.Column(TIMESTAMP)
    tags: List[mypy_boto3_iam.type_defs.TagTypeDef] = sa.Column(JSONType)
    tags_src: List[mypy_boto3_iam.type_defs.TagTypeDef] = sa.Column(JSONType)

    # attached_policies = relationship("Policy", secondary=policy_attachments)

    type: str = sa.Column(sa.String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'identity'
    }
