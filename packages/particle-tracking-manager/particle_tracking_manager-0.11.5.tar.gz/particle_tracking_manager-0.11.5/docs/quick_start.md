---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.1
kernelspec:
  display_name: Python 3.12.0 ('ptm')
  language: python
  name: python3
---

# Quick Start Guide

+++

The simplest way to run `particle-tracking-manager` is to choose a built-in ocean model and select a location to initialize drifters, then use the built-in defaults for everything else (including start time which defaults to the first time step in the model output). You can do this interacting with the software as a Python library or using a command line interface.

Alternatively, you can run the package with new model output by inputting the necessary information into the `Manager`.

Details about what setup and configuration are available in {doc}`configuration`.

+++

## Python Package

Run directly from the Lagrangian model you want to use, which will inherit from the manager class. For now there is one option of `OpenDriftModel`.

```
import particle_tracking_manager as ptm

m = ptm.OpenDriftModel(ocean_model="NWGOA", lon=-151, lat=59, steps=1)
# Can modify `m` between these steps, or look at `OpenDrift` config with `m.drift_model_config()`
m.run_all()
```

Then find results in file `m.outfile_name`.

+++

## Command Line Interface

The equivalent for the set up above for using the command line is:

```
ptm lon=-151 lat=59 ocean_model=NWGOA steps=1
```

To just initialize the simulation and print the `OpenDrift` configuration to screen without running the simulation, add the `--dry-run` flag:

```
ptm lon=-151 lat=59 ocean_model=NWGOA steps=1 --dry-run
```

You can choose to output one or more plots with the `plots` keyword. For example, the following will output a spaghetti plot made from the track file, using OpenDrift's plotting capabilities:

```
ptm lon=-151 lat=59 ocean_model=NWGOA steps=1 plots="{'spaghetti': {}}"
```

You can instead run your simulation and then later make plots with:

```
ptm outfile=[path for outfile including suffix] plots="{'spaghetti': {}}"
```

`m.outfile_name` is printed to the screen after the command has been run. `ptm` is installed as an entry point with `particle-tracking-manager`.


If you are running this locally (this is for Axiom people), you'll want to run it like this:

```
ptm lon=-151 lat=59 ocean_model=NWGOA steps=1 ocean_model_local=True start_time=2000-1-1T01 plots="{'spaghetti': {}}"
```

where you should include `ocean_model_local=True` since you are running the model locally on a server, if you are doing so, you need to input a `start_time` since it will create a kerchunk file on the fly for `ocean_model` that you select. Note that each plot option should be input in a dictionary but then within a string to be correctly interpreted by the CLI. More information on plot options in PTM is available in {ref}`plots`. Many options are available, including animations (see [OpenDrift docs for more information](https://opendrift.github.io/)).

Similarly you would do:

```
ptm lon=-151 lat=59 ocean_model=NWGOA steps=1 ocean_model_local=True start_time=2000-1-1T01 --dry-run
```


+++

(new_reader)=
## Python package with local model output

This demo will run using easily-available ROMS model output from `xroms` and create a spaghetti plot.

```{code-cell} ipython3

import particle_tracking_manager as ptm
import xroms
import xarray as xr
import ast


m = ptm.OpenDriftModel(lon = -90, lat = 28.7, number=10, steps=20,
                       use_static_masks=True, plots={'spaghetti': {}})


url = xroms.datasets.CLOVER.fetch("ROMS_example_full_grid.nc")
ds = xr.open_dataset(url, decode_times=False)
m.add_reader(ds=ds)

# m.run_all() or the following
m.seed()
m.run()
```

You can access the plot name as follows (note you need to use `ast.literal_eval()` because `plots` is stored as a string in the file).

```{code-cell} ipython3
ast.literal_eval(m.plots)["spaghetti"]["filename"]
```


## Idealized simulation

To run an idealized scenario, no reader should be added but configuration parameters can be manually changed, for example:

```{code-cell} ipython3
import particle_tracking_manager as ptm
from datetime import datetime
m = ptm.OpenDriftModel(lon=4.0, lat=60.0, start_time=datetime(2015, 9, 22, 6),
                       use_auto_landmask=True, steps=20)

# idealized simulation, provide a fake current
m.o.set_config('environment:fallback:y_sea_water_velocity', 1)

# seed
m.seed()

# run simulation
m.run()
```

```{code-cell} ipython3
m.o.plot(fast=True)
```

## Ways to Get Information

Check drifter initialization properties:

```
m.initial_drifters
```

Look at reader/ocean model properties:

```
m.reader
```

Get reader/ocean model properties (gathered metadata about model):

```
m.reader_metadata(<key>)
```

Show configuration details — many more details on this in {doc}`configuration`:

```
m.show_config()
```

Show `OpenDrift` configuration for selected `drift_model`:

```
m.drift_model_config()
```
