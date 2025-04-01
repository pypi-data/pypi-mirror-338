"""
Estimate the output of a PV module at Maximum-Power-Point (MPP) conditions.
"""

from typing import Annotated
import pvlib
import pandas as pd
from ...pv.design import ArrayDesign
from ...modeling.decorators import standard_resource_type
from ...modeling import R


@standard_resource_type(R.available_dc_power, override_unit=True)
def available_dc_power_pvlib_pvwatts(
    effective_poa_irradiance: Annotated[pd.Series, R.effective_poa_irradiance],
    cell_temperature: Annotated[pd.Series, R.cell_temperature],
    array: ArrayDesign,
    reference_temperature=25.0,
) -> pd.Series:
    module = array.module
    power_one_module = pvlib.pvsystem.pvwatts_dc(
        g_poa_effective=effective_poa_irradiance,
        temp_cell=cell_temperature,
        pdc0=module.rated_power,
        gamma_pdc=module.temperature_coefficient_power,
        temp_ref=reference_temperature,
    )
    available_dc_power = power_one_module / module.rated_power * array.rated_dc_power
    return available_dc_power
