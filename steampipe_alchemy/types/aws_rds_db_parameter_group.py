
import typing
from typing import ForwardRef


    
Parameters = typing.TypedDict('Parameters',
    {'parameters': typing.List[ForwardRef('dict')]}
)

TagsSrc = typing.TypedDict('TagsSrc',
    {'tags_src': 'Any'}
)

Tags = typing.TypedDict('Tags',
    {'tags': 'Any'}
)

Akas = typing.TypedDict('Akas',
    {'akas': typing.List[ForwardRef('str')]}
)
