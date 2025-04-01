# This is an auto-generated file. Do not change it manually
#
# fmt: off
from ..resource_type_helpers import ResourceTypeDescriptor
from typing import Annotated, Optional


class snow_energy_loss_fraction(ResourceTypeDescriptor):
    """The ratio between snow energy losses with and without snow aggregated over some time. """


    standard = ResourceTypeDescriptor.make_attrs(
        resource_type='snow_energy_loss_fraction',
        to_unit='fraction',
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
            resource_type='snow_energy_loss_fraction',
            to_unit=to_unit,
            set_unit=set_unit,
            to_freq=to_freq,
        )
