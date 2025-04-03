"""
    Convert NGL pos files to PBO pos file and change station code

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

# Path to reference PBO files (to adapt station code)
path_other_pos = 'POS_FILES_GG'

# Read terminal arguments
sta = 'J632'
# sta = sys.argv[1]

# Print in STDOUT
print('Station:   %s' % sta)
print()

#%%###########
## READ NGL ##
##############

ts = Gts(sta)
ts.read_NGLtxyz('POS_FILES_NGL', ref_frame='IGS2014',
                other_pos_name=path_other_pos)
ts.remove_duplicated_dates()

#%%###########
## SAVE PBO ##
##############

# Output directory
outdir = 'POS_FILES_WOOUT_NGL'
if not path.isdir(outdir):
    mkdir(outdir)

ts.write_PBOpos(outdir, replace=True)
