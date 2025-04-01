# This is an auto-generated file. Do not change it manually
#
# fmt: off
from ..resource_type_helpers import ResourceTypeDescriptor
from typing import Annotated, Optional


class effective_poa_irradiance(ResourceTypeDescriptor):
    

    standard = ResourceTypeDescriptor.make_attrs(
        resource_type='effective_poa_irradiance',
        to_unit='W/m^2',
        agg='mean',
    )

    def __init__(
        self,
        *,
        to_unit: Annotated[Optional[str], 'convert to unit'] = None,
        set_unit: Annotated[Optional[str], 'override unit'] = None,
        to_freq: Annotated[Optional[str], 'resample result using new freq'] = None,
    ):
        self._instance_attrs = ResourceTypeDescriptor.make_attrs(
            resource_type='effective_poa_irradiance',
            to_unit=to_unit,
            set_unit=set_unit,
            to_freq=to_freq,
        )
