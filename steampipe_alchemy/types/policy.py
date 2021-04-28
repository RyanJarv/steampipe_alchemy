from typing import List
from typing_extensions import TypedDict


# {'Sid': 'VisualEditor0', 'Action': ['ec2:*'], 'Effect': 'Allow', 'Resource': ['*']}
class Statement(TypedDict):
    Sid: str
    Action: List[str]
    Effect: str
    Resource: List[str]


class Document(TypedDict):
    Version: str
    Statement: List[Statement]


class Policy(TypedDict):
    PolicyName: str
    PolicyDocument: Document
