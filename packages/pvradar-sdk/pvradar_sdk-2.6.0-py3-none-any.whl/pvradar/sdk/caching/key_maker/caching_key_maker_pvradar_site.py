from typing import Optional, Any, override
import pandas as pd
from pvlib.location import Location

from ...modeling.base_model_context import BaseModelContext
from .caching_key_maker import CachingKeyMaker
from ... import ModelContext, PvradarSite
from ...modeling.basics import ModelParam


def interval_to_key(interval: ModelContext | pd.Interval) -> str:
    if isinstance(interval, BaseModelContext):
        effective = interval.get('interval')
    else:
        effective = interval
    if not effective:
        return 'None'
    left_value = int(effective.left.value * 1e-9)
    right_value = int(effective.right.value * 1e-9)
    tz = effective.left.tz
    if tz == 'UTC+00:00':
        tz = 'UTC'
    return f'{left_value}_{right_value}_{effective.closed}_{effective.left.tz}'


def location_to_key(location: ModelContext | Location) -> str:
    if isinstance(location, BaseModelContext):
        effective = location.get('location')
    else:
        effective = location
    if not effective:
        return 'None'
    tz = effective.tz
    if tz == 'UTC+00:00':
        tz = 'UTC'
    return f'{effective.latitude}_{effective.longitude}_{tz}'


class CachingKeyMakerPvradarSite(CachingKeyMaker):
    @override
    def make_key(
        self,
        *,
        resource_name: str,
        as_param: Optional[ModelParam] = None,
        defaults: Optional[dict[str, Any]] = None,
        context: Optional[ModelContext] = None,
    ) -> str | None:
        assert isinstance(context, PvradarSite)
        if as_param and as_param.attrs and 'resource_type' in as_param.attrs:
            return interval_to_key(context) + '__' + location_to_key(context) + '__' + as_param.attrs['resource_type']
