import pandas as pd
from pvlib.location import Location as PvlibLocation
from timezonefinder import TimezoneFinder
from debugpy.common.singleton import Singleton


class TZFinder(TimezoneFinder, Singleton):
    pass


class PvradarLocation(PvlibLocation):
    def __init__(self, latitude, longitude, tz=None, altitude=None, name=None):
        if tz is None:
            tz = TZFinder().timezone_at(lng=longitude, lat=latitude)
            if tz is None:
                raise ValueError(f'Could not determine timezone for ({latitude}, {longitude})')
            reference_date = pd.Timestamp('2024-01-01T00:00:00')
            zoneinfo = reference_date.tz_localize(tz).tzinfo
            if zoneinfo is None:
                raise ValueError(f'Could not find zoneinfo for TZ {tz}')
            offset = zoneinfo.utcoffset(reference_date)
            if offset is None:
                raise ValueError(f'Failed getting UTC offset for TZ {tz}')
            hour_offset = offset.total_seconds() // 3600
            tz = f'UTC{hour_offset:+03.0f}:00'

        # here we can't pass tz directly, because UTC+02:00 format is not supported
        super().__init__(latitude, longitude, tz='UTC', altitude=altitude, name=name)

        self.tz = tz
