from typing import Annotated
import pvlib
import pandas as pd
import pvlib.transformer

from ...pv.design import PvradarSiteDesign
from ...modeling.decorators import standard_resource_type
from ...modeling import R


@standard_resource_type(R.available_ac_power, override_unit=True)
def available_ac_power_pvlib(
    available_inverter_power: Annotated[pd.Series, R.available_inverter_power],
    design: PvradarSiteDesign,
) -> pd.Series:
    transformer = design.transformer
    available_ac_power = pvlib.transformer.simple_efficiency(
        input_power=available_inverter_power,
        no_load_loss=transformer.no_load_loss,
        load_loss=transformer.full_load_loss,
        transformer_rating=design.array.rated_ac_power,  # match inverter rating
    )
    return available_ac_power
