# Author: Ben Brock 
# Created on May 08, 2023 

from setuptools import setup

setup(
    name="quantum_control_rl_server",
    version="1.0",
    description="Fork of v-sivak/quantum-control-rl, frozen version where the server (RL agent) and client (experiment or sim) communicate over tcpip",
    author="Volodymyr Sivak, Henry Liu, Ben Brock",
    author_email="bbrock89@gmail.com",
    url="https://github.com/bbrock89/quantum-control-rl-server",
    packages=["quantum_control_rl/agents", "quantum_control_rl/remote_env_tools", "quantum_control_rl/tf_env", "quantum_control_rl/utils"],
)