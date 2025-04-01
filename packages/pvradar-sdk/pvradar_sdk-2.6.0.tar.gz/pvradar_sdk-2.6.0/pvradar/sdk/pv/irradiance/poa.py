from ...modeling.decorators import standard_resource_type
from ...modeling import R
from ..design import ModuleDesign
from typing import Literal, Annotated
import pandas as pd


ModuleSide = Literal['both', 'front', 'back']


### --- GLOBAL PLANE OF ARRAY IRRADIANCE --- ###


@standard_resource_type(R.global_poa_irradiance_on_front, override_unit=True)
def global_poa_irradiance_on_front(
    ground_reflected_irradiance_on_front: Annotated[pd.Series, R.ground_reflected_irradiance_on_front],
    sky_diffuse_irradiance_on_front: Annotated[pd.Series, R.sky_diffuse_irradiance_on_front],
    direct_irradiance_on_front: Annotated[pd.Series, R.direct_irradiance_on_front],
) -> pd.Series:
    """
    The global irradiance on the front side of a tilted or tracked pv module.
    'global' means sum of all components but without losses.
    """
    global_on_front = ground_reflected_irradiance_on_front + sky_diffuse_irradiance_on_front + direct_irradiance_on_front
    global_on_front = global_on_front.fillna(0)
    return global_on_front


@standard_resource_type(R.global_poa_irradiance_on_rear, override_unit=True)
def global_poa_irradiance_on_rear(
    ground_reflected_irradiance_on_rear: Annotated[pd.Series, R.ground_reflected_irradiance_on_rear],
) -> pd.Series:
    """
    The global irradiance on the front side of a tilted or tracked pv module.
    'global' means sum of all components but without losses.
    """
    global_on_rear = ground_reflected_irradiance_on_rear.copy()
    global_on_rear = global_on_rear.fillna(0)
    return global_on_rear


@standard_resource_type(R.global_poa_irradiance, override_unit=True)
def global_poa_irradiance(
    poa_on_front: Annotated[pd.Series, R.global_poa_irradiance_on_front],
    poa_on_rear: Annotated[pd.Series, R.global_poa_irradiance_on_rear],
) -> pd.Series:
    return poa_on_front + poa_on_rear


### --- EFFECTIVE POA IRRADIANCE --- ###
@standard_resource_type(R.effective_poa_irradiance, override_unit=True)
def effective_poa_irradiance(
    ground_reflected_irradiance_on_front: pd.Series,
    sky_diffuse_irradiance_on_front: pd.Series,
    direct_irradiance_on_front: pd.Series,
    ground_reflected_irradiance_on_rear: pd.Series,
    soiling_loss_factor: Annotated[pd.Series, R.soiling_loss_factor],
    snow_loss_factor: Annotated[pd.Series, R.snow_loss_factor],
    spectral_mismatch_loss_factor: Annotated[pd.Series, R.spectral_mismatch_loss_factor],
    reflection_loss_factor: Annotated[pd.Series, R.reflection_loss_factor],
    rear_side_shading_factor: float,
    module: ModuleDesign,
) -> pd.Series:
    diffuse_on_front = ground_reflected_irradiance_on_front + sky_diffuse_irradiance_on_front
    effective_on_front = (
        (diffuse_on_front + direct_irradiance_on_front * (1 - reflection_loss_factor))
        * (1 - spectral_mismatch_loss_factor)
        * (1 - soiling_loss_factor)
        * (1 - snow_loss_factor)
    )
    effective_on_rear = (
        ground_reflected_irradiance_on_rear
        * (1 - rear_side_shading_factor)
        * module.bifaciality_factor
        * spectral_mismatch_loss_factor
    )
    effective_poa = effective_on_front + effective_on_rear
    return effective_poa
