# Motion

<img src="https://raw.githubusercontent.com/pyomeca/design/master/logo/logo_plain_doc.svg?sanitize=true" alt="logo">

Pyomeca is a python library allowing you to carry out a complete biomechanical analysis; in a simple, logical and concise way.

## Pyomeca documentation

See Pyomeca's [documentation site](https://romainmartinez.github.io/motion).

## Example

Here is an example of a complete EMG pipeline in just one command:

```python
from pyomeca import Analogs3d

emg = (
    Analogs3d.from_c3d("path/to/your/c3d.c3d", names=['anterior_deltoid', 'biceps'])
    .band_pass(freq=2000, order=4, cutoff=[10, 425])
    .center()
    .rectify()
    .low_pass(freq=2000, order=4, cutoff=5)
    .normalization()
    .time_normalization()
)
```

## Features

- Object-oriented architecture where each class is associated with common and specialized functionalities:
  - **Markers3d**: 3d markers positions
  - **Analogs3d**: analogs (emg, force or any analog signal)
  - **GeneralizedCoordinate**: generalized coordinate (joint angle)
  - **RotoTrans**: roto-translation matrix


- Specialized functionalities include signal processing routine commonly used in biomechanics: filters, normalization, onset detection, outliers detection, derivative, etc.


- Each functionality can be chained. In addition to making it easier to write and read code, it allows you to add and remove analysis steps easily (such as Lego blocks).


- Each class inherits from a numpy array, so you can create your own analysis step easily.


- Easy reading and writing interface to common files in biomechanics:
  - **c3d** (binary file used in biomechanics): `from_c3d` and `to_c3d`
  - **csv**: `from_csv` and `to_csv`
  - **mat** (_MATLAB_ file): `from_mat` and `to_mat`
  - **sto** (OpenSim storage file): `to_sto` (must install pyosim)
  - **trc** (OpenSim markers position file): `to_trc` (must install pyosim)


- Common linear algebra routine implemented: get Euler angles to/from roto-translation matrix, create a system of axes, set a rotation or translation, transpose or inverse, etc.

## Installation

### Using Conda

First, install [miniconda](https://conda.io/miniconda.html) or [anaconda](https://www.anaconda.com/download/).
Then type:

```bash
conda install pyomeca -c conda-forge
```

### Using pip

First, you need to install python, swig and numpy. 
Then, follow the instructions to compile [ezc3d](https://github.com/pyomeca/ezc3d).
Finally, install pyomeca with:

```bash
pip install git+https://github.com/pyomeca/pyomeca/`
```

## Integration with other modules

Pyomeca is designed to work well with other libraries that we have developed:

- [pyosim](https://github.com/pyomeca/pyosim): interface between [OpenSim](http://opensim.stanford.edu/) and pyomeca to perform batch musculoskeletal analyses
- [ezc3d](https://github.com/pyomeca/ezc3d): Easy to use C3D reader/writer in C++, Python and Matlab
- [biorbd](https://github.com/pyomeca/biorbd): C++ interface and add-ons to the Rigid Body Dynamics Library, with Python and Matlab binders.

## Bug Reports & Questions

Pyomeca is Apache-licensed and the source code is available on [GitHub](https://github.com/pyomeca/pyomeca). If any questions or issues come up as you use pyomeca, please get in touch via [GitHub issues](https://github.com/pyomeca/pyomeca/issues). We welcome any input, feedback, bug reports, and contributions.