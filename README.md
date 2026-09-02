# Sionna RT book: sample code

Chapter-by-chapter Jupyter notebooks and supporting scenes for the Sionna RT
books.

| Language | Book | Notebooks |
|---|---|---|
| English | *Radio Propagation Ray Tracing with Sionna RT* | `notebooks_en/` |
| 日本語 | 『Sionna RTによる電波伝搬レイトレーシング入門』 | `notebooks/` |

## Target environment

- Python 3.11
- Sionna RT 2.0.1
- Jupyter Notebook / JupyterLab

The Sionna RT API can change between releases. To reproduce the steps in the
books, use the bundled `environment.yml`. When moving to a newer environment,
check the [official Sionna documentation](https://nvlabs.github.io/sionna/) as
well.

## Setup

```bash
git clone https://github.com/isobe-tech/sionna-rt-book-code.git
cd sionna-rt-book-code
conda env create -f environment.yml
conda activate sionna-rt-book
cd notebooks_en      # or notebooks, for the Japanese edition
jupyter lab
```

Run the notebooks with that directory as the working directory. Generated
figures are written to `figs/chXX/`.

## Notebooks by chapter

| Ch. | Topic | Notebook |
|---:|---|---|
| 2 | Setting up the environment | `ch02_install_check.ipynb` |
| 3 | Basic ray tracing | `ch03_basic_ray_tracing.ipynb` |
| 4 | CIR, CFR, channel taps, angle of arrival | `ch04_cir_cfr_taps.ipynb` |
| 5 | Radio maps | `ch05_radio_map_basic.ipynb` |
| 6 | Scenes and visualization | `ch06_visualization.ipynb` |
| 7 | Material models, reflection and transmission | `ch07_materials.ipynb` |
| 8 | Diffraction | `ch08_diffraction.ipynb` |
| 9 | Scattering | `ch09_scattering.ipynb` |
| 10 | Mobile channels and Doppler | `ch10_mobility_doppler.ipynb` |
| 11 | Creating and editing a scene | `ch11_scene_editing.ipynb` |
| 13 | Antennas and polarization | `ch13_antenna_polarization.ipynb` |
| 14 | Arrays and beam steering | `ch14_array_beam_control.ipynb` |
| 15 | Indoor Wi-Fi | `ch15_indoor_wifi.ipynb` |
| 16 | Urban 5G and mmWave | `ch16_urban_5g_mmwave.ipynb` |
| 17 | Road environments and V2X | `ch17_v2x_road_environment.ipynb` |
| 18 | Speed, accuracy, and validation | `ch18_validation.ipynb` |

Chapter 12 covers Blender, OpenStreetMap, and converting external 3D data, and
has no corresponding notebook.

## Notes on running

- The computation time and memory use of a radio map depend on the scene, the
  cell size, the samples per transmitter, and the maximum number of reflections.
- Start with coarse cells and a reduced sample count to confirm it runs.
- A GPU is not required. The Mitsuba variant actually selected can be checked
  with `mitsuba.variant()`.
- Chapter 15 uses the custom scene in `scenes/indoor_apartment/`.

## Reporting errata and problems

Report code defects, discrepancies with either book, and information about the
runtime environment through
[Issues](https://github.com/isobe-tech/sionna-rt-book-code/issues). Include the
versions of Python, Sionna RT, Mitsuba, and Dr.Jit, and the operating system.

## Licence

The code in this repository is released under the [MIT License](LICENSE).
Sionna RT and the bundled scenes and external data carry their own licences.

This is not an official NVIDIA repository.
