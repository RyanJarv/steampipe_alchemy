from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamPolicySimulator(Base):
    __tablename__ = 'aws_iam_policy_simulator'
    principal_arn = Column('principal_arn', Text, primary_key=True, nullable=True)
    action = Column('action', Text, nullable=True)
    resource_arn = Column('resource_arn', Text, nullable=True)
    decision = Column('decision', Text, nullable=True)
    decision_details = Column('decision_details', JSON, nullable=True)
    matched_statements = Column('matched_statements', JSON, nullable=True)
    missing_context_values = Column('missing_context_values', JSON, nullable=True)
    resource_specific_results = Column('resource_specific_results', JSON, nullable=True)
    organizations_decision_detail = Column('organizations_decision_detail', JSON, nullable=True)
    permissions_boundary_decision_detail = Column('permissions_boundary_decision_detail', JSON, nullable=True)