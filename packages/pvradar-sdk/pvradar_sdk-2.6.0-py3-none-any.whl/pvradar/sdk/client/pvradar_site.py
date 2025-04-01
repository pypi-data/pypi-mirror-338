import warnings
from typing import Any, Mapping, Optional, override
from pvlib.location import Location

from .pvradar_validation import validate_pvradar_attrs
from ..modeling.basics import PvradarResourceType, Attrs
from ..modeling.geo_located_model_context import GeoLocatedModelContext
from ..modeling.library_manager import enrich_context_from_libraries
from ..pv.design import (
    ArrayDesign,
    ModuleDesign,
    StructureDesign,
    PvradarSiteDesign,
)


class PvradarSite(GeoLocatedModelContext):
    def __init__(
        self,
        *,
        location: Optional[Location] = None,
        interval: Optional[Any] = None,
        default_tz: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(location=location, interval=interval, default_tz=default_tz, **kwargs)
        enrich_context_from_libraries(self)

    def pvradar_resource_type(self, resource_type: PvradarResourceType, *, attrs: Optional[Attrs] = None, **kwargs):
        warnings.warn(
            '.pvradar_resource_type() is deprecated, use .resource(attrs(resource_type=...)) instead', DeprecationWarning
        )
        req: dict[str, Any] = {'resource_type': resource_type}
        if attrs:
            new_req = dict(attrs.copy())
            new_req.update(req)
            req = new_req

        return self.resource(req, **kwargs)

    @override
    def _convert_by_attrs(self, value: Any, param_attrs: Mapping[str, Any]) -> Any:
        if not self.config.get('disable_validation'):
            validate_pvradar_attrs(param_attrs)
        return super()._convert_by_attrs(value, param_attrs)

    @property
    def design(self) -> PvradarSiteDesign:
        return self.resource('design')

    @design.setter
    def design(self, value: PvradarSiteDesign):
        if not isinstance(value, PvradarSiteDesign):
            raise ValueError(f'While setting design expected PvradarSiteDesign, got {value.__class__.__name__}')
        self['design'] = value

    @property
    def array(self) -> ArrayDesign:
        return self.design.array

    @property
    def module(self) -> ModuleDesign:
        return self.array.module

    @property
    def structure(self) -> StructureDesign:
        return self.array.structure

    @override
    def __repr__(self):
        return f'Pvradar site at ({self.location}) with interval {self.interval}'
