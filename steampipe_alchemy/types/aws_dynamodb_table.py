
import typing
from typing import ForwardRef


    
ArchivalSummary = typing.TypedDict('ArchivalSummary',
    {'archival_summary': 'Any'}
)

AttributeDefinitions = typing.TypedDict('AttributeDefinitions',
    {'attribute_definitions': typing.List[ForwardRef('dict')]}
)

KeySchema = typing.TypedDict('KeySchema',
    {'key_schema': typing.List[ForwardRef('dict')]}
)

SseDescription = typing.TypedDict('SseDescription',
    {'sse_description': 'Any'}
)

PointInTimeRecoveryDescription = typing.TypedDict('PointInTimeRecoveryDescription',
    {'point_in_time_recovery_description': {'LatestRestorableDateTime': 'Any', 'PointInTimeRecoveryStatus': 'str', 'EarliestRestorableDateTime': 'Any'}}
)

TagsSrc = typing.TypedDict('TagsSrc',
    {'tags_src': 'Any'}
)

Tags = typing.TypedDict('Tags',
    {'tags': {}}
)

Akas = typing.TypedDict('Akas',
    {'akas': typing.List[ForwardRef('str')]}
)
