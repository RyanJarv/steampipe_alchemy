
import typing
from typing import ForwardRef


    
Associations = typing.TypedDict('Associations',
    {'associations': typing.List[ForwardRef('dict')]}
)

Routes = typing.TypedDict('Routes',
    {'routes': typing.List[ForwardRef('dict')]}
)

PropagatingVgws = typing.TypedDict('PropagatingVgws',
    {'propagating_vgws': 'Any'}
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
