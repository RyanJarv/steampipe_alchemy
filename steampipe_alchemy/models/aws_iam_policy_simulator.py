from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamPolicySimulator(Base):
    __tablename__ = 'aws_iam_policy_simulator'
    principal_arn = Column(name='principal_arn', type_=Text, primary_key=True, nullable=True)
    action = Column(name='action', type_=Text, nullable=True)
    resource_arn = Column(name='resource_arn', type_=Text, nullable=True)
    decision = Column(name='decision', type_=Text, nullable=True)
    decision_details = Column(name='decision_details', type_=JSON, nullable=True)
    matched_statements = Column(name='matched_statements', type_=JSON, nullable=True)
    missing_context_values = Column(name='missing_context_values', type_=JSON, nullable=True)
    resource_specific_results = Column(name='resource_specific_results', type_=JSON, nullable=True)
    organizations_decision_detail = Column(name='organizations_decision_detail', type_=JSON, nullable=True)
    permissions_boundary_decision_detail = Column(name='permissions_boundary_decision_detail', type_=JSON, nullable=True)