
import typing
from typing import ForwardRef


    
RecordingGroup = typing.TypedDict('RecordingGroup',
    {'recording_group': {'AllSupported': 'bool', 'ResourceTypes': 'Any', 'IncludeGlobalResourceTypes': 'bool'}}
)

Status = typing.TypedDict('Status',
    {'status': {'Name': 'str', 'Recording': 'bool', 'LastStatus': 'str', 'LastStopTime': 'Any', 'LastErrorCode': 'Any', 'LastStartTime': 'str', 'LastErrorMessage': 'Any', 'LastStatusChangeTime': 'str'}}
)

Akas = typing.TypedDict('Akas',
    {'akas': typing.List[ForwardRef('str')]}
)
