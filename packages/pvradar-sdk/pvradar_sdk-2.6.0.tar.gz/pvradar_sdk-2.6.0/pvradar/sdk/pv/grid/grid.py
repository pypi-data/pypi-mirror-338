from typing import Annotated
import pandas as pd
import numpy as np
from ...modeling.decorators import standard_resource_type
from ...modeling import R


@standard_resource_type(R.available_grid_power, override_unit=True)
def available_grid_power_pvradar(
    available_ac_power: Annotated[pd.Series, R.available_ac_power],
    grid_limit: pd.Series,
) -> pd.Series:
    available_grid_power = pd.Series(
        np.minimum(available_ac_power.to_numpy(), grid_limit.to_numpy()), index=available_ac_power.index
    )
    return available_grid_power
