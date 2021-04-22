
import typing
from typing import ForwardRef


    
InlinePolicies = typing.TypedDict('InlinePolicies',
    {'inline_policies': typing.List[ForwardRef('dict')]}
)

InlinePoliciesStd = typing.TypedDict('InlinePoliciesStd',
    {'inline_policies_std': typing.List[ForwardRef('dict')]}
)

AttachedPolicyArns = typing.TypedDict('AttachedPolicyArns',
    {'attached_policy_arns': typing.List[ForwardRef('str')]}
)

Users = typing.TypedDict('Users',
    {'users': 'Any'}
)

Akas = typing.TypedDict('Akas',
    {'akas': typing.List[ForwardRef('str')]}
)
