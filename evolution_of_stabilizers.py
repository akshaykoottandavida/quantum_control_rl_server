# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:24:22 2020

@author: Vladimir Sivak
"""

import os
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"]='true'
os.environ["CUDA_VISIBLE_DEVICES"]="0"

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from time import time
from math import pi
from gkp.gkp_tf_env import tf_env_wrappers as wrappers
from gkp.gkp_tf_env import policy as plc
from gkp.gkp_tf_env import gkp_init

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

env = gkp_init(simulate='oscillator', 
                init='vac', H=4, T=4, batch_size=1000, episode_length=100, 
                reward_mode='zero', quantum_circuit_type='v2')

from gkp.action_script import phase_estimation_symmetric_with_trim_4round as action_script
to_learn = {'alpha':True, 'beta':True, 'phi':False}
env = wrappers.ActionWrapper(env, action_script, to_learn)
env = wrappers.FlattenObservationsWrapperTF(env,
                        observations_whitelist=['msmt','clock'])

root_dir = r'E:\VladGoogleDrive\Qulab\GKP\sims\PPO\July\OscillatorGKP'
policy_dir = r'mlp3_steps36_48_lr1e-4_script_alpha_v2\policy\000100000'
policy = tf.compat.v2.saved_model.load(os.path.join(root_dir,policy_dir))


# from gkp.action_script import phase_estimation_symmetric_with_trim_4round as action_script
# policy = plc.ScriptedPolicy(env.time_step_spec(), action_script)

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# What operators to measure 
names = [r'Re($S_x$)', r'Re($S_y$)', r'Re($S_z$)',
         r'Im($S_x$)', r'Im($S_y$)', r'Im($S_z$)']
# Translation amplitudes
stabilizers = [env.code_map[S] for S in ['S_x','S_y','S_z']*2]
# Qubit measurement angles
angles = [0]*3 + [-pi/2]*3
# Params for plotting
lines = ['-']*3 + ['--']*3
palette = plt.get_cmap('tab10')
colors = [palette(0), palette(1), palette(2)]*2

results = {name : np.zeros(env.episode_length) for name in names}
cache = [] # store intermediate states (after feedback)
times = [] # for timing every round

# Collect batch of episodes
time_step = env.reset()
policy_state = policy.get_initial_state(env.batch_size)
counter = 0
while not time_step.is_last()[0]:
    t_start = time()
    counter += 1
    action_step = policy.action(time_step, policy_state)      
    policy_state = action_step.state
    time_step = env.step(action_step.action)
    t_stop = time()
    cache.append(env.info['psi_cached'])
    times.append(t_stop - t_start)
    print('%d: Time %.3f sec' %(counter, times[-1]))

# Measure stabilizers on cached wavefunctions
for name, stabilizer, phi in zip(names, stabilizers, angles):
    for i, psi in enumerate(cache):
        stabilizer_batch = tf.stack([stabilizer]*env.batch_size)
        stabilizer_batch = tf.cast(stabilizer_batch, tf.complex64)
        phi_batch = tf.stack([phi]*env.batch_size)
        _, z = env.phase_estimation(psi, stabilizer_batch, phi_batch)
        results[name][i] = np.mean(z)

# Plot stabilizers Re and Im
fig, ax = plt.subplots(1,1)
ax.set_xlabel('Step')
ax.set_title('Stabilizers')
steps = np.arange(env.episode_length)
for i, name in enumerate(names):
    ax.plot(steps, results[name], label=name, 
            linestyle=lines[i], color=colors[i])
ax.legend()
