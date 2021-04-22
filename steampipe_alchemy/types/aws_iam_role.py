
import typing
from typing import ForwardRef


    
InstanceProfileArns = typing.TypedDict('InstanceProfileArns',
    {'instance_profile_arns': 'Any'}
)

TagsSrc = typing.TypedDict('TagsSrc',
    {'tags_src': 'Any'}
)

InlinePolicies = typing.TypedDict('InlinePolicies',
    {'inline_policies': 'Any'}
)

InlinePoliciesStd = typing.TypedDict('InlinePoliciesStd',
    {'inline_policies_std': 'Any'}
)

AttachedPolicyArns = typing.TypedDict('AttachedPolicyArns',
    {'attached_policy_arns': typing.List[ForwardRef('str')]}
)

AssumeRolePolicy = typing.TypedDict('AssumeRolePolicy',
    {'assume_role_policy': {'Version': 'str', 'Statement': typing.List[ForwardRef('dict')]}}
)

AssumeRolePolicyStd = typing.TypedDict('AssumeRolePolicyStd',
    {'assume_role_policy_std': {'Version': 'str', 'Statement': typing.List[ForwardRef('dict')]}}
)

Tags = typing.TypedDict('Tags',
    {'tags': 'Any'}
)

Akas = typing.TypedDict('Akas',
    {'akas': typing.List[ForwardRef('str')]}
)
