import numpy as np
import matplotlib.pyplot as plt

import pyNN
from pyNN.standardmodels.cells import *

# from pyNN.utility import normalized_filename

# https://neuralensemble.org/docs/PyNN/reference/neuronmodels.html

"""
The AdExp component needs to be placed inside a PointNeuron, e.g.:

celltype = sim.PointNeuron( sim.AdExp(tau_m=10.0, v_rest=-60.0), )

http://neuralensemble.org/docs/PyNN/reference/neuronmodels.html#pyNN.standardmodels.cells.LIF.units

class AdExp(**parameters)[source]

Bases: StandardCellTypeComponent

Exponential integrate and fire neuron with spike triggered and sub-threshold adaptation currents according to:

Brette R and Gerstner W (2005) Adaptive Exponential Integrate-and-Fire Model as an Effective Description of Neuronal Activity. J Neurophysiol 94:3637-3642

default_parameters = {'a': 4.0, 'b': 0.0805, 'cm': 0.281, 'delta_T': 2.0, 'i_offset': 0.0, 'tau_m': 9.3667, 'tau_refrac': 0.1, 'tau_w': 144.0, 'v_reset': -70.6, 'v_rest': -70.6, 'v_spike': -40.0, 'v_thresh': -50.4}

recordable = ['spikes', 'v', 'w']

injectable = True

default_initial_values = {'v': -70.6, 'w': 0.0}

units = {'a': 'nS', 'b': 'nA', 'cm': 'nF', 'delta_T': 'mV', 'i_offset': 'nA', 'tau_m': 'ms', 'tau_refrac': 'ms', 'tau_w': 'ms', 'v': 'mV', 'v_reset': 'mV', 'v_rest': 'mV', 'v_spike': 'mV', 'v_thresh': 'mV', 'w': 'nA'}


"""

# defining simulator
#import pyNN.neuron as sim
#import pyNN.brian2 as sim
import pyNN.nest as sim

delta_t_step = 0.01
sim.setup(timestep=delta_t_step)

initial_values = {"v": -96.2}

SPN_cell = sim.PointNeuron(
    sim.AdExp(
        cm=123.5 * 1e-3,
        tau_refrac=2.47,
        v_spike=10,
        v_reset=-51,
        v_rest=-96.2,
        tau_m=3.5283698074395744, # 123.5 / (8.6 * 4.07)
        i_offset=0.0,
        a=-14.5,
        b=500.0 * 1e-3,
        delta_T=16,
        tau_w=15,
        v_thresh=-51,
    )
)

cells = sim.Population(size=1, cellclass=SPN_cell, initial_values=initial_values)
current_protocol = sim.StepCurrentSource(
    times=[0.0, 100.0, 900.0], amplitudes=[0.0, 0.5, 0.0]
)  # nA
current_protocol.inject_into(cells)
rec = cells.record(["v", "w"])
sim_duration = 1000.0
sim.run(sim_duration)
results = cells.get_data()

print(results)


def plot_results(currents, voltages, sim_duration, delta_t_step):
    time = np.arange(0, sim_duration + delta_t_step, delta_t_step)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    for i in range(0, voltages.shape[1]):
        vol = voltages[:, i]
        ax1.plot(time, vol)
        ax1.set_xlabel("ms")
        ax1.set_ylabel("mV")
        ax1.set_title("Membrane potential")
    for i in range(0, currents.shape[1]):
        curr = currents[:, i]
        ax2.plot(time, curr)
        ax2.set_xlabel("ms")
        ax2.set_ylabel("nA")
        ax2.set_title("Spike-adaptation current")
    plt.subplots_adjust(wspace=0.25)
    plt.show()

currents = results.segments[0].filter(name="w")[0].magnitude
voltages = results.segments[0].filter(name="v")[0].magnitude

plot_results(currents, voltages, sim_duration, delta_t_step)
