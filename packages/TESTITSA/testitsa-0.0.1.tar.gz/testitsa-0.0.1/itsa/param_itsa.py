import os

"""
    Parameter file for time series analysis with tsanalysis_itsa.py

    ----
    Developed at: ISTerre
    By: Lou MARILL
"""

#%%###############
## PATH TO DATA ##
##################

# Path to the ITSA module
# Path to the folder containing the 'itsa' folder
path_module = "/app/wkdir/"

# Path to the ITSA 'test_files' folder
path_workdir ="/app/wkdir/Data/"

# Dataset identifier
# Can be used when you have various POS_FILES folder
# it will set folder_res and type_ts accordingly
dataset_id = None  # None or str

# Station/antenna information input
# currently handled is GipsyX staDB format
# If None defaults to gipsyx
# Possible values:
# - gipsyx (GipsyX staDB format)
# - gamit (GAMIT station.info format)
# - all : both gipsyx (GipsyX staDB format) and gamit (GAMIT station.info format)
station_input_type = None
# Name of input folder (GipsyX staDB format) or file (GAMIT station.info format)
# Warning: case sensitive!
# If None defaults to staDB
station_input_name = None



# Path and name of result folder
folder_res ="/app/wkdir/RESULTS/SGO-EPND"


#%%#########################
## PROCESSING INFORMATION ##
############################

# Processing type
# Name of the processing from which solution come from
process = 'GipsyX'  # str
# If you have only one POS_FILES folder, put: |type_ts = ''|.
# Else, you must have POS_FILES_XX folder name and put: |type_ts = 'XX'|
# (where XX can be anything you want).
type_ts = ''  # str

# Reference frame
# For my data :
#  - GAMIT/GLOBK: 'ITRF2014',
#  - GipsyX and Nevada Geodetic Laboratory: 'IGS2014',
#  - F3 : 'ITRF2005'.
# Useless if ts file are PBO pos.
ref_frame = 'IGS14'  # str
# If you want to change of reference frame
save_frame = 'EURA'  # str
# Antartica       ANTA
# Arabia          ARAB
# Australia       AUST
# Eurasia         EURA
# India           INDI
# Nasca           NAZC
# North America   NOAM
# Nubia           NUBI
# Pacific         PCFC
# Peruvian Sliver   PS (Villegas-Lanza et al., 2016)
# South America   SOAM
# Somalia         SOMA

# Skip inversion
# Set to True if you want to skip the inversion, to output only the PBO pos file.
skip_inversion = False  # bool
# Automatically skip inversion for short timeseries (less than 100 points)
auto_skip_inversion = True  # bool

# Skip outliers filtering
# Set to True if you want to skip filtering outliers
skip_outliers_filter = False  # bool


#%%##############
## TIME PERIOD ##
#################
# The inital and final dates can both be set to None

# Initial date, in calendar date
# If |ini_time = None|, the first time of the time series is considered.
ini_time = None  # None or list [year, month, day]

# Final date, in calendar date
# If |fin_time = None|, the last time of the time series is considered.
fin_time = None  # None or list [year, month, day]

# Percentage of data wanted
# If you want all stations, put: |perc_ts = 0|.
# Else, you want only stations with at least |perc_ts|% data within the time
# period.
# |perc_ts = 100| mean you want time series without gap (with one data each day
# within th time period).
perc_ts = 0  # int within [0, 100]


#%%##############################
## OUTLIERS REMOVAL PARAMETERS ##
#################################
# Only a basic detection of outliers is including in tsanalysis_ista.py
# If you want more precise detection (and then removal) of outliers you can use
# ista.gts.lib.outliers.py functions (on Gts object only!)

# Detecting threshold
# Value mutliplied by the MAD (Median Absolute Deviation) of the window to
# create the final.
# outlier detection threshold
thresh = 5.  # float

# Window length
# Length of the sliding window.
window_len = 60  # int


#%%###############################
## ASSOCIATED EVENTS PARAMETERS ##
##################################

# Minimum moment magnitudes
# Minimum Mw for all events
Mw_min = 5.1  # float
# Minimum Mw for pos-seismic effect
Mw_post = 6.1  # float
# Minimum Mw for special post-seismic effect (sum of log or exp)
# Put |Mw_spe = None| if you want all post-seismic with the same model.
Mw_spe = 8.  # float

# Influence radius parameter
# Higher the parameter, smaller the influence radius.
# Advise: put all folowing parameters to 1 for your first test,
# then decid if you want larger/smaller influence radius.
# Co-seismic events
dco = 1.15  # float
# Pos-seismic effects
dpost = 1.3  # float
# SSEs
dsse = 1.  # float
# Swarm events
dsw = 1.  # float


#%%###########
## ANALYSIS ##
##############

# Windows length
# Jump window
jps_window_data = 365  # int
# Post-seismic window
post_window_data = 2*365  # int

# Post-seismic model
# Choose between logarithmic or exponential models
mod_post = 'log10' # 'log10' or 'exp'

# Post-seismic relaxation time
# In the jump window
tau_jps = 10  # int
# In the post-seismic window
tau_post = 30  # int
# In the post-seismic window for the special post-seismic effect
# |tau_spe| is not taken into account if |Mw_spe = None|.
tau_spe = 1  # int

# Compute post-seismic from last post-seismic event before the time period
# If |pre_post = True|, take the last post-seismic event no matter the time 
# between the event and the beggining of the time period.
# If |pre_post| is int, take event only if it is within |pre_post| days of the
# beggining of the time period.
pre_post = False # bool or int

# Compute acceleration terme?
acc = False  # bool


#%%##########
## DISPLAY ##
#############

# Window's figure
# If True, save figure from window analysis.
disp_window = True  # bool


#%%#############
## BY-PRODUCT ##
################
# If you want to save/display some by-product with the analysis

# Save by-product?
byp_make = False  # bool

# If |byp_make| is True, the program look at the following variables.
# All variables are bool np.ndarray with how many values than the number of wanted
# by-products.
# True: the component is corrected (removed from the Gts)
# False: nothing done

# Name of folder to save the by-products
byp_names = ['RESIDUALS', 'PHY', 'GEO']
# Velocity and acceleration trend
byp_vel = [True, False, True]
# Seasonal variation (annual and semi-annual)
byp_seas = [True, False, True]
# Antenna changes
byp_ant = True
# Co-seismic jumps
byp_co = [True, False, True]
# Swarm
byp_sw = [True, False, True]
# SSE
byp_sse = [True, False, False]
# Post-seismic effect
byp_post = [True, False, True]
# Display figures? True = display
disp_byp = [False, True, True]
