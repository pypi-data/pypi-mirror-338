"""
    Remove outliers and save data in PBO pos file 

    ----
    Developed at: ISTerre
    By: Lou MARILL
"""

#%%#########
## IMPORT ##
############

# General modules
import sys
from os import path, mkdir
# Add path
sys.path.append('/Users/marilll/Desktop/python3.9')
#('/data/cycle/marilll/python3.9')
# itsa modules
from itsa.gts.Gts import Gts


#%%#############
## PARAMETERS ##
################

# Read terminal arguments
data_type = 'GG'
#data_type = sys.argv[1]
sta = '1008'
#sta = sys.argv[2]

# Print in STDOUT
print('Data type: %s' % data_type)
print('Station:   %s' % sta)
print()


#%%###########
## OUTLIERS ##
##############

# Output directory
outdir = 'POS_FILES_WOOUT_'+data_type
if not path.isdir(outdir):
    mkdir(outdir)

# Reference frame
if data_type == 'GG':
    ref_frame = 'ITRF2014'
    process = 'GAMIT/GLOBK'
elif data_type in  ['GX', 'NGL']:
    ref_frame = 'IGS2014'
    if data_type == 'GX':
        process = 'GipsyX'
    else:
        process = 'Nevada Geodetic Laboratory'
elif data_type == 'F3':
    ref_frame = 'ITRF2005'
    process = 'F3'
else:
    ref_frame = 'Unknown'
    process = 'Unknown'

# Create and read Gts
ts = Gts(sta)
ts.read_allpos('POS_FILES_'+data_type, ref_frame=ref_frame, process=process)
ts.remove_duplicated_dates()

# Find and remove outliers
ts.continuous_time(in_place=True)
ts.find_outliers(window_len=365)
ts.remove_outliers(in_place=True)
ts.nonan_time(in_place=True)

# Change reference coordinates
ts.change_ref(ts.time[0, 1])

# Save new Gts
ts.write_PBOpos(outdir, replace=True)
