"""
Estimate the inverter power output.
"""

from typing import Annotated
import pvlib
import pandas as pd
from ...pv.design import ArrayDesign
from ...modeling.decorators import standard_resource_type
from ...modeling import R


@standard_resource_type(R.available_inverter_power, override_unit=True)
def available_inverter_power_pvlib_pvwatts(
    available_dc_power: Annotated[pd.Series, R.available_dc_power],
    array: ArrayDesign,
    reference_inverter_efficiency: float = 0.9637,
) -> pd.Series:
    """
    This simplified model describes all inverters as one big inverter connected to the all dc modules.
    """
    inverter = array.inverter
    available_inverter_power = pvlib.inverter.pvwatts(
        pdc=available_dc_power,
        pdc0=array.rated_ac_power,
        eta_inv_nom=inverter.nominal_efficiency,
        eta_inv_ref=reference_inverter_efficiency,
    )
    return available_inverter_power
