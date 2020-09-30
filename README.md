# gdc: an API for GameDataCrunch

[![PyPI status][pypi-image]][pypi]
[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]
  
This repository contains Python code to download data through [GameDataCrunch API][gamedatacrunch].

## Installation

The code is packaged for [PyPI][pypi], so that the installation consists in running:
```bash
pip install gamedatacrunch
```

## Usage

### Load data

Data is locally cached to `data/%Y%m%d_gamedatacrunch.json` for offline reuse.
```python
import gamedatacrunch as gdc

data = gdc.load()
```

### Load a list of appIDs

For a list of appIDs (`int`), without the matching app names:
```python
import gamedatacrunch as gdc

app_ids = gdc.load_app_ids()
```

### Retro-compatibility: Steam API

For retro-compatibility, the output is formatted as with [Steam API][steam-api]:
```python
import gamedatacrunch as gdc

data = gdc.load_as_steam_api()
```

### Retro-compatibility: SteamSpy API

For retro-compatibility, the output is formatted as with [SteamSpy API][steamspy-api]:
```python
import gamedatacrunch as gdc

data = gdc.load_as_steamspy_api()
```

<!-- Definitions -->

[gamedatacrunch]: <https://www.gamedatacrunch.com>
[steamspy-api]: <https://github.com/woctezuma/steamspypi>
[steam-api]: <https://steamapi.xpaw.me/#ISteamApps/GetAppList>

<!-- Definitions for badges -->

[pypi]: <https://pypi.python.org/pypi/gamedatacrunch>
[pypi-image]: <https://badge.fury.io/py/gamedatacrunch.svg>

[build]: <https://github.com/woctezuma/gamedatacrunch/actions>
[build-image]: <https://github.com/woctezuma/gamedatacrunch/workflows/Python package/badge.svg?branch=master>
[publish-image]: <https://github.com/woctezuma/gamedatacrunch/workflows/Upload Python Package/badge.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/gamedatacrunch/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/gamedatacrunch/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/gamedatacrunch/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/gamedatacrunch>
[codecov-image]: <https://codecov.io/gh/woctezuma/gamedatacrunch/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/gamedatacrunch>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/1033f9ca50bf4fdf9d41bd2365558ce3>
