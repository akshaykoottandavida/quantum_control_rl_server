# Model-Free Quantum Control with Reinforcement Learning
Fork of v-sivak/quantum-control-rl, frozen version where the server (RL agent) and client (experiment or sim) communicate over tcpip.

## Requirements
Requires a variety of packages, but for ease of use one should create the conda environment defined in qcrl-server-tf240.yml.  See the installation section for more details.  The included qcrl-server environment uses tensorflow v2.4.0 and tf-agents v0.6.0, which has been tested to work with CUDA v11.0 and cudnn v8.0.5 for GPU acceleration.  Without CUDA set up, this package will still work using the CPU, but this may limit performance depending on the application.

## Installation
To install this package, first clone this repository.  This package should be used with the conda environment defined in qcrl-server-tf240.yml.  To create this environment from the file, open an anaconda cmd prompt, cd into the repo directory, and run:
```sh
conda env create -f qcrl-server-tf240.yml
```
To install this package into this conda environment qcrl-server, first activate the environment using
```sh
conda activate qcrl-server
```
then cd into the repo directory and run:
```sh
pip install -e .
```

## CUDA Compatibility

The qcrl-server conda environment has been tested to work with CUDA v11.0 and cudnn v8.0.5. 

## Using the package



