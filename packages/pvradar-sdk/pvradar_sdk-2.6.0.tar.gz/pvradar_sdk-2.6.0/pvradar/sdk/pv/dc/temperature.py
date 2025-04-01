"""
Estimate the temperature of the PV module back surface ('module') or photovoltaic cells ('cell') during operation.
"""

from ...modeling.decorators import standard_resource_type
from ...modeling import R

from typing import Annotated
import pandas as pd
from pydantic import Field

from pvlib.temperature import (
    sapm_module,
    sapm_cell_from_module,
    pvsyst_cell,
)


### --- CELL TEMPERATURE --- ###


@standard_resource_type(R.cell_temperature, override_unit=True)
def cell_temperature_pvlib_sapm(
    module_temperature: Annotated[pd.Series, R.module_temperature, Field()],
    poa_global: Annotated[pd.Series, R.global_poa_irradiance, Field()],
    sapm_temperature_model_param_deltaT: float = 3,
) -> pd.Series:
    """
    Wrapper around the PVLIB implementation of the Sandia Array Performance Model (SAPM) cell temperature model.
    """
    cell_temperature = sapm_cell_from_module(
        module_temperature=module_temperature,
        poa_global=poa_global,
        deltaT=sapm_temperature_model_param_deltaT,
    )
    return cell_temperature


@standard_resource_type(R.cell_temperature, override_unit=True)
def cell_temperature_pvlib_pvsyst(
    poa_global: Annotated[pd.Series, R.global_poa_irradiance, Field()],
    temp_air: Annotated[pd.Series, R.air_temperature, Field()],
    wind_speed: Annotated[pd.Series, R.wind_speed, Field()],
    pvsyst_temperature_model_param_u_c: float = 29,
    pvsyst_temperature_model_param_u_v: float = 0,
    pvsyst_temperature_model_param_module_efficiency: float = 0.1,
    pvsyst_temperature_model_param_alpha_absorption: float = 0.9,
) -> pd.Series:
    """
    Wrapper around the PVLIB implementation of the PVSYST cell temperature model.
    """
    cell_temperature = pvsyst_cell(
        poa_global=poa_global,
        temp_air=temp_air,
        wind_speed=wind_speed,  # type: ignore - can be both float and pd.Series although typehint asks for float
        u_c=pvsyst_temperature_model_param_u_c,
        u_v=pvsyst_temperature_model_param_u_v,
        module_efficiency=pvsyst_temperature_model_param_module_efficiency,
        alpha_absorption=pvsyst_temperature_model_param_alpha_absorption,
    )
    return cell_temperature


### --- MODULE TEMPERATURE --- ###


@standard_resource_type(R.module_temperature, override_unit=True)
def module_temperature_pvlib_sapm(
    poa_global: Annotated[pd.Series, R.global_poa_irradiance, Field()],
    temp_air: Annotated[pd.Series, R.air_temperature, Field()],
    wind_speed: Annotated[pd.Series, R.wind_speed, Field()],
    sapm_temperature_model_param_a: float = -3.56,
    sapm_temperature_model_param_b: float = -0.075,
) -> pd.Series:
    """
    Wrapper around the PVLIB implementation of the Sandia Array Performance Model (SAPM) module temperature model.
    """
    module_temperature = sapm_module(
        poa_global=poa_global,
        temp_air=temp_air,
        wind_speed=wind_speed,
        a=sapm_temperature_model_param_a,
        b=sapm_temperature_model_param_b,
    )
    return module_temperature
