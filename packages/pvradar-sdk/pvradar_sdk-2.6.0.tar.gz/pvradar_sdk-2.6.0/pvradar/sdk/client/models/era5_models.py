from typing import Any, Annotated as A
import pandas as pd

from ..api_query import Query
from ..client import PvradarClient
from pvlib.location import Location
from ...modeling.decorators import datasource, standard_resource_type
from ...modeling import R
from ...modeling.utils import auto_attr_table, convert_series_unit
from ..pvradar_resources import SeriesConfigAttrs as S
from ...modeling.resource_types._list import standard_mapping
from ...modeling.basics import Attrs as P


era5_series_name_mapping: dict[str, str | A[Any, Any]] = {
    # ----------------------------------------------------
    # Single levels
    #
    '2m_temperature': A[pd.Series, S(resource_type='air_temperature', unit='degK', agg='mean', freq='1h')],
    'snow_depth': A[
        pd.Series, S(resource_type='snow_depth_water_equivalent', unit='m', agg='mean', freq='1h')
    ],  # snow_depth_water
    'snowfall': A[pd.Series, S(resource_type='snowfall_water_equivalent', unit='m', agg='sum', freq='1h')],  # snowfall_water
    'snow_density': A[pd.Series, S(resource_type='snow_density', unit='kg/m^3', agg='mean', freq='1h')],
    # ----------------------------------------------------
    # Pressure levels
    'relative_humidity': A[pd.Series, S(resource_type='relative_humidity', unit='%', agg='mean', freq='1h')],
}


def _auto_attr_table(df: pd.DataFrame, **kwargs) -> None:
    if df is None:
        return
    auto_attr_table(
        df,
        series_name_mapping=era5_series_name_mapping,
        resource_annotations=standard_mapping,
        **kwargs,
    )
    for name in df:
        df[name].attrs['datasource'] = 'era5'


# ----------------------------------------------------
# ERA5 tables


@standard_resource_type(R.era5_single_level_table)
@datasource('era5')
def era5_single_level_table(
    location: Location,
    interval: pd.Interval,
) -> pd.DataFrame:
    query = Query.from_site_environment(location=location, interval=interval)
    query.set_path('datasources/era5/raw/hourly/csv')
    result = PvradarClient.instance().get_df(query, crop_interval=interval)
    _auto_attr_table(result)

    if (
        len(result)
        and interval.left > pd.Timestamp('2005-01-01T00:00:00+05:00')
        and interval.left <= pd.Timestamp('2005-01-01T00:00:00UTC')
    ):
        index = pd.date_range(interval.left, result.index[-1], freq='h')
        original = result
        result = result.reindex(index)
        result = result.bfill()
        # workaround for bug in pandas overwriting attrs
        for column in result.columns:
            result[column].attrs = original[column].attrs

    return result


# ----------------------------------------------------
# ERA5 series (alphabetical order)


@standard_resource_type(R.air_temperature)
@datasource('era5')
def era5_air_temperature(
    *,
    era5_single_level_table: A[pd.DataFrame, P(resource_type='era5_single_level_table')],
) -> pd.Series:
    return convert_series_unit(era5_single_level_table['2m_temperature'], to_unit='degC')


@standard_resource_type(R.relative_humidity)
@datasource('era5')
def era5_relative_humidity(
    *,
    era5_single_level_table: A[pd.DataFrame, P(resource_type='era5_single_level_table')],
) -> pd.Series:
    series = era5_single_level_table['relative_humidity']
    if series.attrs['unit'] != '%':
        raise ValueError(f'Unexpected unit: {series.attrs["unit"]}')
    return series.copy()


@standard_resource_type(R.snow_density)
@datasource('era5')
def era5_snow_density(
    *,
    era5_single_level_table: A[pd.DataFrame, P(resource_type='era5_single_level_table')],
) -> pd.Series:
    series = era5_single_level_table['snow_density']
    if series.attrs['unit'] != 'kg/m^3':
        raise ValueError(f'Unexpected unit: {series.attrs["unit"]}')
    return series.copy()


@standard_resource_type(R.snow_depth_water_equivalent)
@datasource('era5')
def era5_snow_depth_water_equivalent(
    *,
    era5_single_level_table: A[pd.DataFrame, P(resource_type='era5_single_level_table')],
) -> pd.Series:
    result = era5_single_level_table['snow_depth']
    # unit conversion done automatically
    result.attrs['resource_type'] = 'snow_depth'
    return result


@standard_resource_type(R.snow_depth)
@datasource('era5')
def era5_snow_depth(
    *,
    era5_snow_depth_water_equivalent: A[pd.Series, P(resource_type='snow_depth_water_equivalent', datasource='era5')],
    snow_density: A[pd.Series, P(resource_type='snow_density', datasource='era5')],
) -> pd.Series:
    result = era5_snow_depth_water_equivalent * (1000 / snow_density)
    result.attrs['agg'] = 'mean'
    return result


@standard_resource_type(R.snowfall_water_equivalent)
@datasource('era5')
def era5_snowfall_water_equivalent(
    *,
    era5_single_level_table: A[pd.DataFrame, P(resource_type='era5_single_level_table')],
) -> pd.Series:
    result = era5_single_level_table['snowfall']
    # unit conversion done automatically
    result.attrs['resource_type'] = 'snowfall'
    return result


@standard_resource_type(R.snowfall)
@datasource('era5')
def era5_snowfall(
    *,
    era5_snowfall_water_equivalent: A[pd.Series, P(resource_type='snowfall_water_equivalent', datasource='era5')],
) -> pd.Series:
    snow_density_value = 100  # Kg/m^3, value for fresh snow
    result = era5_snowfall_water_equivalent * (1000 / snow_density_value)
    result.attrs['agg'] = 'sum'
    return result
