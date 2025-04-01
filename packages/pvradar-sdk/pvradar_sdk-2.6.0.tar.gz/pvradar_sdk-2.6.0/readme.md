Software Developer Kit (SDK) for PVRADAR platform.

https://pvradar.com

# Installation

```sh
pip install pvradar-sdk
```

# Usage

```python
from pvradar.sdk import PvradarSite, attrs, describe

site = PvradarSite(location=(-23, 115), interval='2020..2023')
ghi = site.resource(attrs(resource_type='global_horizontal_irradiance'))
print(ghi)
print(describe(ghi))
```

Please, contact PVRADAR for more details and features.
