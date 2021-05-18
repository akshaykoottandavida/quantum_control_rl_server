# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:13:49 2020

@author: Vladimir Sivak
"""

import os
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"]='true'
os.environ["CUDA_VISIBLE_DEVICES"]="0"


import tensorflow as tf
import qutip as qt
import numpy as np
from math import pi, sqrt
import matplotlib.pyplot as plt
from gkp.gkp_tf_env import policy as plc
from gkp.gkp_tf_env import helper_functions as hf
from gkp.gkp_tf_env import tf_env_wrappers as wrappers
from gkp.gkp_tf_env import env_init
from simulator.utils import expectation
import gkp.action_script as action_scripts

# N=50
# target_state = (qt.basis(N,9)+sqrt(3)*qt.basis(N,3)).unit()

# reward_kwargs = {'reward_mode' : 'overlap', 
#                   'target_state' : target_state,
#                   'postselect_0' : False
#                   }

# env = gkp_init(simulate='snap_and_displacement', 
#                 reward_kwargs=reward_kwargs,
#                 init='vac', H=1, T=5, attn_step=1, batch_size=1, N=N, episode_length=5)

# action_script = 'snap_and_displacements'
# action_scale = {'alpha':4, 'theta':pi}
# to_learn = {'alpha':True, 'theta':True}
# action_script = action_scripts.__getattribute__(action_script)
# env = wrappers.ActionWrapper(env, action_script, action_scale, to_learn)

# root_dir = r'E:\data\gkp_sims\PPO\examples\test100\seed1'
# policy_dir = r'policy\001900'
# policy = tf.compat.v2.saved_model.load(os.path.join(root_dir,policy_dir))


# env = gkp_init(simulate='gkp_qec_autonomous_sBs_osc_qb', 
#                 reward_kwargs={'reward_mode':'zero'},
#                 init='vac', H=1, T=2, attn_step=1, batch_size=1, episode_length=2,
#                 encoding='square')

# from gkp.action_script import gkp_qec_autonomous_sBs_2round as action_script
# policy = plc.ScriptedPolicy(env.time_step_spec(), action_script)


# N=100
# target_state = qt.tensor(qt.basis(2,0), qt.basis(100,4))

# N = 70
# db_val = 8
# z = db_val / (20 * np.log10(np.e))
# target_state = qt.tensor(qt.basis(2,0), qt.squeeze(N,z)*qt.basis(N,0))

# N = 60
# pz = (qt.basis(N,0) + qt.basis(N,4))/np.sqrt(2.0)
# mz = qt.basis(N,2)
# py = (pz + 1j*mz)/np.sqrt(2.0)
# target_state = qt.tensor(qt.basis(2,0), py)

# target_state_cav = qt.qload('E:\data\gkp_sims\PPO\ECD\GKP_state_delta_0p25')
# target_state = qt.tensor(qt.basis(2,0), target_state_cav)
# N = target_state_cav.dims[0][0]

# reward_kwargs = {'reward_mode' : 'overlap', 
#                   'target_state' : target_state,
#                   'postselect_0' : False}

# env = gkp_init(simulate='ECD_control',
#                 reward_kwargs=reward_kwargs,
#                 init='vac', H=1, T=16, attn_step=1, batch_size=1, N=N, 
#                 episode_length=16)

# from gkp.action_script import ECD_control_residuals as action_script
# policy = plc.ScriptedPolicy(env.time_step_spec(), action_script)


# N=40
# reward_kwargs = {'reward_mode' : 'overlap', 
#                   'target_state' : qt.tensor(qt.basis(2,0), qt.basis(N,3)),
#                   'postselect_0' : False
#                   }

# env = gkp_init(simulate='snap_and_displacement_miscalibrated', 
#                 reward_kwargs=reward_kwargs,
#                 init='vac', H=1, T=5, attn_step=1, batch_size=1, N=N, episode_length=5)

# action_script = 'snap_and_displacements'
# action_scale = {'alpha':4, 'theta':pi}
# to_learn = {'alpha':True, 'theta':True}
# action_script = action_scripts.__getattribute__(action_script)
# env = wrappers.ActionWrapper(env, action_script, action_scale, to_learn)

# root_dir = r'E:\data\gkp_sims\PPO\paper_data\miscalibrated_snap\ideal_overlap\0'
# policy_dir = r'policy\003000'
# policy = tf.compat.v2.saved_model.load(os.path.join(root_dir,policy_dir))


# N=200
# reward_kwargs = {'reward_mode' : 'stabilizers_v2',
#                  'Delta' : 0.0, 'beta' : sqrt(pi),
#                  'sample' : False}

# env = gkp_init(simulate='snap_and_displacement', 
#                 reward_kwargs=reward_kwargs,
#                 init='vac', H=1, T=6, attn_step=1, batch_size=1, N=N, episode_length=6)

# action_script = 'snap_and_displacements'
# action_scale = {'alpha':6, 'theta':pi}
# to_learn = {'alpha':True, 'theta':True}
# action_script = action_scripts.__getattribute__(action_script)
# env = wrappers.ActionWrapper(env, action_script, action_scale, to_learn)

# root_dir = r'E:\data\gkp_sims\PPO\examples\test_gkp_eps0.1\delta0.55\seed0'
# policy_dir = r'policy\010000'
# policy = tf.compat.v2.saved_model.load(os.path.join(root_dir,policy_dir))


# N=50
# target_state = qt.tensor(qt.basis(2,0), qt.basis(50,2))

# reward_kwargs = {'reward_mode' : 'overlap', 
#                   'target_state' : target_state,
#                   'postselect_0' : False
#                   }

# env = gkp_init(simulate='ECD_control',
#                 reward_kwargs=reward_kwargs,
#                 init='vac', H=1, T=8, attn_step=1, batch_size=1, N=N, 
#                 episode_length=8)

# action_script = 'ECD_control'
# action_scale = {'beta':3, 'phi':pi}
# to_learn = {'beta':True, 'phi':True}
# action_script = action_scripts.__getattribute__(action_script)
# env = wrappers.ActionWrapper(env, action_script, action_scale, to_learn, 
#                               learn_residuals=False)

# root_dir = r'E:\data\gkp_sims\PPO\ECD\test_fock2_2'
# policy_dir = r'policy\001000'
# policy = tf.compat.v2.saved_model.load(os.path.join(root_dir,policy_dir))


N=100
target_state = qt.tensor(qt.basis(2,0), qt.basis(50,4))

reward_kwargs = {'reward_mode' : 'overlap', 
                  'target_state' : target_state,
                  'postselect_0' : True
                  }

env = env_init(simulate='ECD_control', reward_kwargs=reward_kwargs,
               init='vac', T=8, batch_size=1, N=N, episode_length=8,
               phase_space_rep='characteristic_fn')

action_script = 'ECD_control_residuals'
action_scale = {'beta':3/8, 'phi':pi/8}
to_learn = {'beta':True, 'phi':True}
action_script = action_scripts.__getattribute__(action_script)
env = wrappers.ActionWrapper(env, action_script, action_scale, to_learn, 
                              learn_residuals=True)

root_dir = r'E:\data\gkp_sims\PPO\ECD\EXP\fock4\run_2'
policy_dir = r'policy\000300'
policy = tf.compat.v2.saved_model.load(os.path.join(root_dir,policy_dir))

# from gkp.action_script import ECD_control_residuals as action_script
# policy = plc.ScriptedPolicy(env.time_step_spec(), action_script)


### Plot cardinal points
if 0:
    for state_name in env.states.keys():
        state = tf.reshape(env.states[state_name], [1,env.N])
        hf.plot_wigner_tf_wrapper(state, title=state_name)

### Simulate one episode
if 1:
    n = [] # average photon number 
    time_step = env.reset()
    policy_state = policy.get_initial_state(env.batch_size)
    while not time_step.is_last():
        action_step = policy.action(time_step, policy_state)
        policy_state = action_step.state
        time_step = env.step(action_step.action)
        n.append(float(expectation(env._state, env.n)))
        env.render()
        # print(time_step.observation)
    
    fig, ax = plt.subplots(1,1)
    ax.set_xlabel('Step')
    ax.set_ylabel(r'$\langle \, n \, \rangle$')
    ax.plot(range(len(n)), n)

    print("="*25 + '%f' %time_step.reward)