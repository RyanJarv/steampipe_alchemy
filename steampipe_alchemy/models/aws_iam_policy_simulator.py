from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamPolicySimulator(Base):
    __tablename__ = 'aws_iam_policy_simulator'
    principal_arn = Column(Text, name='principal_arn', primary_key=True, nullable=True)
    action = Column(Text, name='action', nullable=True)
    resource_arn = Column(Text, name='resource_arn', nullable=True)
    decision = Column(Text, name='decision', nullable=True)
    decision_details = Column(JSON, name='decision_details', nullable=True)
    matched_statements = Column(JSON, name='matched_statements', nullable=True)
    missing_context_values = Column(JSON, name='missing_context_values', nullable=True)
    resource_specific_results = Column(JSON, name='resource_specific_results', nullable=True)
    organizations_decision_detail = Column(JSON, name='organizations_decision_detail', nullable=True)
    permissions_boundary_decision_detail = Column(JSON, name='permissions_boundary_decision_detail', nullable=True)