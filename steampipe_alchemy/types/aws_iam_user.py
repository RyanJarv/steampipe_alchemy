
import typing
from typing import ForwardRef


    
MfaDevices = typing.TypedDict('MfaDevices',
    {'mfa_devices': 'Any'}
)

Groups = typing.TypedDict('Groups',
    {'groups': 'Any'}
)

InlinePolicies = typing.TypedDict('InlinePolicies',
    {'inline_policies': typing.List[ForwardRef('dict')]}
)

InlinePoliciesStd = typing.TypedDict('InlinePoliciesStd',
    {'inline_policies_std': typing.List[ForwardRef('dict')]}
)

AttachedPolicyArns = typing.TypedDict('AttachedPolicyArns',
    {'attached_policy_arns': typing.List[ForwardRef('str')]}
)

TagsSrc = typing.TypedDict('TagsSrc',
    {'tags_src': typing.List[ForwardRef('dict')]}
)

Tags = typing.TypedDict('Tags',
    {'tags': {'Name': 'str', 'Stack': 'str', 'Scenario': 'str'}}
)

Akas = typing.TypedDict('Akas',
    {'akas': typing.List[ForwardRef('str')]}
)
