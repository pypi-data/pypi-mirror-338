import numpy as np
import nest
import matplotlib.pyplot as plt

#######################################################################################################
# definition of the simulation. 
# it takes the cell and the stimulation protocol
# it returns the stimulation amplitude, the time, the membrane voltage,
# the Spike-adaptation current and the number of spikes
def simulate(time, stim, params, V_init=None):
    model = 'aeif_cond_exp'
    nest.ResetKernel()
    nrn = nest.Create(model, params=params)
    #V_m -> mV -Membrane potential; w -> pA - Spike-adaptation current
    mme = nest.Create('multimeter', params={'record_from': ['V_m', 'w']})
    spd = nest.Create('spike_recorder')
    nest.Connect(mme, nrn)
    nest.Connect(nrn, spd)

    if V_init:
        nest.SetStatus(nrn, {'V_m': V_init})
    else:
        nest.SetStatus(nrn, {'V_m': V_rest})
    nest.Simulate(stim['delay'])
    I_e = nest.GetStatus(nrn, 'I_e')[0]
    nest.SetStatus(nrn, {'I_e': I_e + stim['amp']})
    print('I_e=', I_e + stim['amp'])
    nest.Simulate(stim['duration'])
    nest.SetStatus(nrn, {'I_e': I_e})
    nest.Simulate(time - stim['delay'] - stim['duration'])
    
    spikes = nest.GetStatus(spd, keys='events')[0]['times']
    times = nest.GetStatus(mme)[0]['events']['times']
    V_m = nest.GetStatus(mme)[0]['events']['V_m']
    w = nest.GetStatus(mme)[0]['events']['w']
    sweep_data = {'stim_amp': stim['amp'], 
                  'times': times, 
                  'V_m': V_m, 
                  'w': w, 
                  'spikes': spikes}
    return sweep_data


def plot_v_w_c(t, v, w, c, method, color):
    methods = ('Euler', 'Nest', 'Brian', 'Alex_solve_ivp')
    if method not in method:
        raise ValueError("Invalid method.")
    
    # Creating subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,4))
    if method == 'Nest':
        # Plotting on the first subplot
        ax1.plot(v, 'o-', markersize=1, color=color)
        # Plotting on the second subplot
        ax2.plot(w, 'o-', markersize=1, color=color)
        # Plotting on the third subplot
        ax3.plot(c, color=color)
    #if method == 'Euler' or method == 'Brian' or method == 'Alex_solve_ivp':
    else:    
        # Plotting on the first subplot
        ax1.plot(t, v, 'o-', markersize=1, color=color)
        # Plotting on the second subplot
        ax2.plot(t, w, 'o-', markersize=1, color=color)    
        # Plotting on the third subplot
        if len(t) != len(c):
            t = np.linspace(0,len(c)*0.01,len(c))
        ax3.plot(t, c, color=color)    

    # Refining first subplot
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('[mV]')
    ax1.set_title('Membrane potential')
    # Refining second subplot
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('[pA]')
    ax2.set_title('Spike-adaptation current')
    # Refining third subplot
    ax3.set_xlabel('Time [ms]')
    ax3.set_ylabel('[pA]')
    ax3.set_title('Injected current')

    # Refining figure
    fig.suptitle(str(method) + ' implementation', fontsize=16)
    plt.subplots_adjust(top=0.85, hspace=0.5)
    plt.subplots_adjust(wspace=0.3)
    plt.show()
#######################################################################################################    


Time = 1 * 10**5 # 1s
dt = 0.01 # ms

# explicitly defining the time
time=np.arange(0,Time*dt,dt)

### current protocol.
amp = 100                  # pA
stim_delay = 100./dt       # ms
stim_duration = 800./dt    # ms
duration = 1000./dt        # ms 

current_protocol = np.zeros(Time)
current_protocol[0:int(stim_delay)] = 0
current_protocol[int(stim_delay):int(stim_delay+stim_duration)] = amp
current_protocol[int(stim_delay+stim_duration):] = 0

# Striatal dSPN neruon, setting for NEST
V_rest = -96.2   #mV
V_th = -51.      #mV
params_NEST = { 'C_m': 123.5 *1,            # pF - Capacity of the membrane
                'g_L': 8.6 *4.07,           # nS - Leak conductance
                'E_L': -96.2,               # mV - Leak reversal potential
                'I_e': 0.,                  # pA - Constant external input current
                'a': -14.5,                 # nS - Subthreshold adaptation
                'b': 500.,                  # pA - Spike-triggered adaptation
                'tau_w': 15.,               # ms Adaptation time constant
                'V_th': V_th,
                'Delta_T': 16.,             # mV - Slope factor
                'V_reset': -51.,            # mV - Reset value for V_m after a spike
                'V_peak': 10,               # mV - Spike detection threshold
                't_ref': 2.47,              # ms - Duration of refractory period
                }


# definition of the stimulation protocol
nest_amps = [amp]                             # pA
nest_delay = stim_delay * dt                  # ms
nest_duration = stim_duration * dt            # ms
stimuli = [{'delay': nest_delay, 'duration': nest_duration, 'amp': nest_amp} for nest_amp in nest_amps]

# running the simulation and saving the output in sweeps
sweeps = [simulate(stim['duration'] + 2*stim['delay'], stim, params_NEST, V_init=V_rest) for stim in stimuli]

# saving output
v_nest = sweeps[0]['V_m']
w_nest = sweeps[0]['w']

# calling the plotting function
plot_v_w_c(time, v_nest, w_nest, current_protocol, color='red', method='Nest')


print(f'Total number of spikes detected when integrating using NEST: {len(sweeps[0]["spikes"])}')























