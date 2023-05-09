# Model-Free Quantum Control with Reinforcement Learning
Fork of v-sivak/quantum-control-rl, frozen version where the server (RL agent) and client (experiment or sim) communicate over tcpip.

## Requirements
Requires a variety of packages, but for ease of use one should create the conda environment defined in qcrl-server-tf240.yml.  See the installation section for more details.

## Installation
To install this package clone this repository, cd into its directory, and run:
```sh
pip install -e .
```
This package should be used with the conda environment defined in qcrl-server-tf240.yml.  To create this environment from the file, open an anaconda cmd prompt and run:
```sh
conda env create -f qcrl-server-tf240.yml
```

