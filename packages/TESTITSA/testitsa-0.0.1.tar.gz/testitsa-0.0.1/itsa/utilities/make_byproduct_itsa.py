"""
    Read tsanalysis_itsa.py results and make by-products

    Require:
     - ITSA module
     - Results from tsanalysis_itsa.py

    To lauch use the following lines in terminal:
     - module load python/python3.9
     - python3.9 make_byproduct_itsa CODE
        *CODE correspond to the code of the station you want

    ----
    Developed at: ISTerre
    By: Lou MARILL
"""

#%%#############
## PARAMETERS ##
################

# ITSA module path
path_module = '/Users/marilll/Desktop/python3.9'

# Results folder
folder_res = '/Users/marilll/Desktop/TS-analysis/RESULTS/'

# Reference frame
save_frame = 'ITRF2014'

# Acceleration?
acc = True

# By-product parameters
# Velocity and acceleration trend
vel = [True, False, True]
# Seasonal variation (annual and semi-annual)
seas = [True, False, True]
# Antenna changes
ant = True
# Co-seismic jumps
co = [True, False, True]
# Swarm
sw = [True, False, True]
# SSE
sse = [True, False, False]
# Post-seismic effect
post = [True, False, True]
# Name of folder to save the by-products
names = ['RESIDUALS', 'PHY', 'GEO']
# Display figures? True = display
disp = [False, True, True]


#%%#################
## IMPORT MODULES ##
####################

# General modules
from sys import path, argv
import numpy as np

# Add path
path.append(path_module)

# ITSA module
from itsa.gts.Gts import Gts
from itsa.jps.Jps import Jps
from itsa.lib.save_Gts_byproduct import save_byp


#%%###########
## READ GTS ##
##############

# Create Gts
if len(argv) > 1:
    ts = Gts(argv[1])
else:
    ts = Gts('0036')
# Print in STDOUT
print('Station: %s' %ts.code)
print()

# Read raw TS
folder_read = folder_res+'OUTPUT_FILES/'
ts.read_PBOpos(folder_read+'TS_DATA/RAW/', warn=False)

# Read Jps
ts.jps = Jps(ts.code)
ts.jps.read(folder_read+'JPS/')

# Read Green's function and associated model
ts.read_GMOD(folder_read+'G_MATRIX', folder_read+'MODEL_AMP')

# Acceleration?
if acc:
    ts_acc = ts.copy()
    ts_acc.G = None
    ts.read_GMOD(folder_read+'G_MATRIX_QUA', folder_read+'MODEL_AMP_QUA')

# Change reference frame
if save_frame != ts.ref_frame:
    if (save_frame[:3].upper() == 'IGS'
        or save_frame[:4].upper() == 'ITRF'):
        ts.itrf_convert(save_frame, in_place=True)
    else:
        ts.fixed_plate(save_frame[:4], in_place=True)

# Put |self.t0| to the first available data
idx_nonan = np.unique(np.where(~np.isnan(ts.data))[0])
ts.change_ref(ts.time[idx_nonan[0], 1])


#%%###############################
## SAVE AND DISPLAY BY-PRODUCTS ##
##################################

# Define target folder
folder_pos = folder_res+'OUTPUT_FILES/TS_DATA/'
folder_fig = folder_res+'PLOTS/'

# Save and display
save_byp(ts, vel, seas, ant, co, sw, sse, post, names, disp, folder_pos,
          folder_fig, replace=True)

# Acceleration?
if acc:
    # Convert all parameters into np.ndarray with same shape
    from itsa.lib.modif_vartype import adapt_shape
    (names, vel, seas, ant,
     co, sw, sse, post, disp) = adapt_shape([names, vel, seas, ant,
                                             co, sw, sse, post, disp])
    # Select only by-product impacted by acceleration
    spe_acc = vel | seas
    # Change by-product folder names
    acc_names = np.char.add(names[spe_acc], np.repeat('_QUA', sum(spe_acc)))
    # Save and display
    save_byp(ts, vel[spe_acc], seas[spe_acc], ant[spe_acc], co[spe_acc],
             sw[spe_acc], sse[spe_acc], post[spe_acc], acc_names,
             disp[spe_acc], folder_pos, folder_fig, replace=True)
