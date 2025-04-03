"""
    Time series analysis

    Require:
     - ITSA module
     - param_itsa.py

    To lauch use the following lines in terminal:
     - module load python/python3.9
     - python3 tsanalysis_itsa.py CODE
        *CODE correspond to the code of the station you want to analyse

    ----
    Developed at: ISTerre
    By: Lou MARILL
"""

#%%#################
## IMPORT MODULES ##
####################

# General modules
import matplotlib
# deactivate figure display, need to be at the program's begginig
matplotlib.use('Agg')
from sys import path, argv
import numpy as np
import os
from os.path import exists, getsize, isdir
from os import mkdir
module_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
path.append(module_dir)

# Program parameters
import param_itsa as pm

# Add path
if exists(pm.path_module):
    path.append(pm.path_module)
else:
    raise ValueError(f"The 'path_module' variable is incorrectly set in param_itsa.py:\n \
            The directory {pm.path_module} does not exist!")

# ITSA module
from itsa.gts.Gts import Gts
from itsa.lib.astrotime import cal2decyear, decyear2mjd, mjd2decyear
from itsa.lib.index_dates import get_index_from_dates
from itsa.lib.read_cat import read_antenna
from itsa.lib.read_cat import read_station_info
from itsa.lib.select_ev import select_ev
from itsa.lib.save_Gts_byproduct import save_byp


def write_QC(data, sta, folder):
    """
    Write QC indicators to a file
    """
    Sn = ts.data[1:, 4]
    Se = ts.data[1:, 5]
    Su = ts.data[1:, 6]
    avg_Sn = np.nanmean(Sn) 
    avg_Se = np.nanmean(Se) 
    avg_Su = np.nanmean(Su)
    qc_dir = os.path.join(folder_out, "QC")
    qc_file = os.path.join(qc_dir, f"qc_{ts.code}.txt")
    if not isdir(qc_dir):
        mkdir(qc_dir)
    with open(qc_file, "w") as qc:
            qc.write("Station avg_Sn avg_Se avg_Su\n")
            qc.write(f"{ts.code} {avg_Sn} {avg_Se} {avg_Su}\n")


#%%###################
## READ TIME SERIES ##
######################

# Create Gts
if len(argv) > 1:
    ts = Gts(argv[1])
else:
    ts = Gts('0036')
# Print in STDOUT
print('Station: %s' %ts.code)
print()



# Read Gts
# POS_FILES folder
if exists(pm.path_workdir):
    if pm.type_ts == '':
        folder_ts = os.path.join(pm.path_workdir, 'INPUT_TS')
    else:
        folder_ts = os.path.join(pm.path_workdir, f'INPUT_TS_{pm.type_ts}')
else:
    raise ValueError(f"The 'path_workdir' variable is incorrectly set in param_itsa.py:\n \
            The directory {pm.path_workdir} does not exist!")
# Read
try:
    ts.read_allpos(folder_ts, ref_frame=pm.ref_frame, process=pm.process)
except:
    print('[WARNING] from [tsanalysis_itsa]:')
    print("\tNo file '%s*.pos' was found in '%s'!" % (ts.code, folder_ts))
else:

    # Limit Gts to given time period
    if pm.ini_time is None:
        ini_time = ts.time[0, 0]
    else:
        ini_time = cal2decyear(pm.ini_time[2], pm.ini_time[1], pm.ini_time[0])
    if pm.fin_time is None:
        fin_time = ts.time[-1, 0]
    else:
        fin_time = cal2decyear(pm.fin_time[2], pm.fin_time[1], pm.fin_time[0])
    
    # Use continuous time vector and remove duplicate dates
    ts.continuous_time(ini_time=ini_time, fin_time=fin_time, in_place=True)
   
    # Choose to skip inversion or not based on user parameters and timeseries length
    if pm.skip_inversion == True:
        skip_inversion = True
    else:
        if pm.auto_skip_inversion == True:
            # skip inversion if timeseries shorter than 100 points
            if len(np.unique(np.where(~np.isnan(ts.data))[0])) > 100:
                skip_inversion = False
            else:
                skip_inversion = True
        else:
            skip_inversion = False

    # Find and remove outliers
    if skip_inversion == False:
        if pm.skip_outliers_filter == False:
            ts.find_outliers(pm.thresh, pm.window_len)
            ts.remove_outliers(in_place=True)
        else:
            print('[WARNING] skip_outliers_filter set to True, skipping outliers filtering!')
    else:
        print('[WARNING] skip_inversion set to True, skipping inversion!')
        
    # Enough data to analyse?
    idx_nonan = np.unique(np.where(~np.isnan(ts.data))[0])
    if len(idx_nonan) > ts.time.shape[0]*pm.perc_ts/100:
    
        
        #%%#########################
        ## FIND ASSOCIATED EVENTS ##
        ############################
    
        # Input station metadata
        path_input_stnMD = os.path.join(pm.path_workdir, 'INPUT_STN_METADATA')
        if pm.station_input_name is None:
            antenna_path = os.path.join(path_input_stnMD, 'staDB')
        else:
            antenna_path = os.path.join(path_input_stnMD, pm.station_input_name)
        path_input_cats = os.path.join(pm.path_workdir, 'INPUT_CATS')
        isc_cat_file = os.path.join(path_input_cats, 'isc_catalog.txt')
        eq_cat_file = os.path.join(path_input_cats, 'eq_catalog.txt')
        sse_cat_file = os.path.join(path_input_cats, 'sse_catalog.txt')
        sw_cat_file = os.path.join(path_input_cats, 'swarm_catalog.txt')
        unsta_cat_file = os.path.join(path_input_cats, 'unknown_sta_catalog.txt')
        unev_cat_file = os.path.join(path_input_cats, 'unknown_ev_catalog.txt')
    
        # Jps metadata
        ts.jps.mag_min = pm.Mw_min
        ts.jps.mag_post = pm.Mw_post
        ts.jps.mag_spe = pm.Mw_spe
        ts.jps.dco = pm.dco
        ts.jps.dpost = pm.dpost
        ts.jps.dsse = pm.dsse
        ts.jps.dsw = pm.dsw
    
        # Antenna changes
        # Read
        # Issue 31: allow use of GAMIT station.info
        print(antenna_path, ts.code)
        if pm.station_input_type == None:
            ant_dates = read_antenna(antenna_path, ts.code)
        elif pm.station_input_type.lower() == "gipsyx":
            ant_dates = read_antenna(antenna_path, ts.code)
        elif pm.station_input_type.lower() == "gamit":
            ant_dates = read_station_info(antenna_path, ts.code)
        elif pm.station_input_type.lower() == "all":
            # TODO: Gérer les collisions et lire des deux sources
            ant_dates = read_antenna(antenna_path, ts.code)
        else:
            ant_dates = read_antenna(antenna_path, ts.code)
        # Populate |self.jps|
        if ant_dates.size > 0:
            ts.jps.add_ev(np.c_[ant_dates, decyear2mjd(ant_dates)], 'A')
    
        # Earthquake catalog
        # ISC catalog
        if exists(isc_cat_file) and getsize(isc_cat_file) > 0:
            (isc_cat, type_isc) = select_ev(ts.XYZ0, isc_cat_file, 'ISC',
                                          pm.Mw_min, pm.dco, pm.Mw_post,
                                          pm.dpost)
            if isc_cat.size > 0:
                isc_cat = isc_cat.reshape(-1, 5)
                ts.jps.add_ev(np.c_[isc_cat[:, 0], decyear2mjd(isc_cat[:, 0])],
                              type_isc, isc_cat[:, 1:-1], isc_cat[:, -1])
        # Handmade catalog
        if exists(eq_cat_file) and getsize(eq_cat_file) > 0:
            (eq_cat, type_eq) = select_ev(ts.XYZ0, eq_cat_file, 'E',
                                          pm.Mw_min, pm.dco, pm.Mw_post,
                                          pm.dpost)
            if eq_cat.size > 0:
                eq_cat = eq_cat.reshape(-1, 5)
                ts.jps.add_ev(np.c_[eq_cat[:, 0], decyear2mjd(eq_cat[:, 0])],
                              type_eq, eq_cat[:, 1:-1], eq_cat[:, -1])
    
        # Swarm catalog (optional)
        if exists(sw_cat_file) and getsize(sw_cat_file) > 0:
            (sw_cat, type_sw) = select_ev(ts.XYZ0, sw_cat_file, 'W',
                                          None, pm.dsw)           
            if sw_cat.size > 0:
                sw_cat = sw_cat.reshape(-1, 6)
                ts.jps.add_ev(np.c_[sw_cat[:, 0], decyear2mjd(sw_cat[:, 0])],
                              type_sw, sw_cat[:, 1:-2], sw_cat[:, -2],
                              sw_cat[:, -1])
    
        # SSE catalog (optional)
        if exists(sse_cat_file) and getsize(sse_cat_file) > 0:
            (sse_cat, type_sse) = select_ev(ts.XYZ0, sse_cat_file, 'S',
                                            pm.Mw_min, pm.dsse)            
            if sse_cat.size > 0:
                sse_cat = sse_cat.reshape(-1, 6)
                ts.jps.add_ev(np.c_[sse_cat[:, 0], decyear2mjd(sse_cat[:, 0])],
                              type_sse, sse_cat[:, 1:-2], sse_cat[:, -2],
                              sse_cat[:, -1])
                
        # Unknown from unknown_sta_catalog.txt (optional)
        if exists(unsta_cat_file) and getsize(unsta_cat_file) > 0:
            # Read
            unsta_cat = np.genfromtxt(unsta_cat_file,
                                      dtype=[('Station', 'U4'),
                                             ('Year', 'f8')])
            # Find station dates
            unsta_dates = unsta_cat[
                np.where(unsta_cat['Station'] == ts.code)]['Year']
            # Transform to modified Julian days
            if unsta_dates.size > 0:
                unsta_mjd = np.array(decyear2mjd(unsta_dates), dtype=int)+.5
                # Populate |self.jps|
                ts.jps.add_ev(np.c_[mjd2decyear(unsta_mjd),unsta_mjd], 'U')
    
        # Unknown from unknown_ev_catalog.txt (optional, to avoid)
        if exists(unev_cat_file) and getsize(unev_cat_file) > 0:
            # Read
            (unev_cat, type_unev) = select_ev(ts.XYZ0, unev_cat_file, 'U')           
            # Populate |self.jps|
            if unev_cat.size > 0:
                unev_cat = unev_cat.reshape(-1, 6)
                ts.jps.add_ev(np.c_[unev_cat[:, 0],
                                    decyear2mjd(unev_cat[:, 0])],
                              type_unev, unev_cat[:, 1:-2], None,
                              unev_cat[:, -1])
    
        # Sort events and remove duplicated dates
        ts.jps.remove_duplicated_dates()
           
        # Set Gts to NaN during unknown, antenna and earthquake events
        find_UAEP = np.isin(ts.jps.type_ev,['U','A','E','P'])
        idx_jps_UAEP = get_index_from_dates(ts.time[:, 1],
                                            ts.jps.dates[find_UAEP, 1])
        if pm.skip_outliers_filter == False:
            ts.outliers = idx_jps_UAEP[np.where(idx_jps_UAEP>=0)]
            ts.remove_outliers(in_place=True)
            
    # Still enough data to analyse?
    idx_nonan = np.unique(np.where(~np.isnan(ts.data))[0])
    if len(idx_nonan) <= ts.time.shape[0]*pm.perc_ts/100:
        print('[WARNING] from [tsanalysis_itsa]:')
        print('\tGts %s has not enough data within [%.3f;%.3f] to be analysed!'
              % (ts.code, ini_time, fin_time))
        print()
    else:
        
        # Keep only useful events
        # Whithin the time period
        jps_period = ts.jps.select_ev(
            (ts.jps.dates[:, 1]>ts.time[idx_nonan[0], 1])
            & (ts.jps.dates[:, 1]<ts.time[idx_nonan[-1], 1]))
        # Last post-seismic event before the no-NaN time period
        if pm.pre_post:
            idx_jp_add = np.where(
                (ts.jps.type_ev=='P') &
                (ts.jps.dates[:, 1]<=ts.time[idx_nonan[0], 1]))[0]
            if idx_jp_add.size == 0:
                pm.pre_post = False
            else:
                idx_jp_add = idx_jp_add[-1]
                if isinstance(pm.pre_post, int):
                    time_lim = ts.time[idx_nonan[0], 1]-pm.pre_post
                if (isinstance(pm.pre_post, int)
                    and ts.jps.dates[idx_jp_add, 1] > time_lim):
                    pm.pre_post = False
                else:
                    pm.pre_post = True
                    jps_period.add_ev(ts.jps.dates[idx_jp_add, :],
                                      ts.jps.type_ev[idx_jp_add],
                                      ts.jps.coords[idx_jp_add, :],
                                      ts.jps.mag[idx_jp_add])
                    jps_period.reorder()
        ts.jps = jps_period
        
        # Change reference frame
        if pm.ref_frame != pm.save_frame and pm.save_frame != ts.ref_frame:
            if (pm.save_frame[:3].upper() == 'IGS'
                or pm.save_frame[:4].upper() == 'ITRF'):
                ts.itrf_convert(pm.save_frame, in_place=True)
            else:
                ts.fixed_plate(pm.save_frame[:4], in_place=True)
        
        # Put |self.t0| to the first available data
        ts.change_ref(ts.time[idx_nonan[0], 1])
        
        
        #%%###########
        ## ANALYSIS ##
        ##############
        
        if pm.skip_outliers_filter == False:
            # Green's function initialisation
            # Constant term
            c = np.ones(ts.time.shape[0])
            # Velocity [mm/year]
            tg = ts.time[:, 0]-ts.time[0, 0]
            # Sesonal and semi-seasonal terms
            an1, an2 = np.cos(2.*np.pi*tg), np.sin(2.*np.pi*tg)
            sm1, sm2 = np.cos(4.*np.pi*tg), np.sin(4.*np.pi*tg)
            # Seasonal Green's functions
            G_seas = np.c_[c, tg, an1, an2, sm1, sm2]
            
            # Initialisation
            # Index of no-NaN data
            idx_nonan = np.unique(np.where(~np.isnan(ts.data))[0])
            # Figure folder
            folder_fig = os.path.join(pm.folder_res , argv[1], 'PLOTS')
            folder_window = os.path.join(folder_fig, 'WINDOW')
            
            # Jps not empty?
            if ts.jps.shape() > 0:
                
                # Jump inversion
                ts_res_jps = ts.window_analysis(
                    pm.jps_window_data, np.c_[c, tg], pm.tau_jps, pm.mod_post,
                    disp=pm.disp_window, folder_disp=os.path.join(folder_window, f"JPS{os.sep}"))
           
                # Post-seismic inversion
                # Take only Jps with solution != 0
                idx_jps_ok = np.where((ts.MOD[:, :3]!=0).any(axis=1))[0]
                # Shift index if one post-seismic before time period
                if pm.pre_post:
                    idx_jps_ok = [0]+list(idx_jps_ok+1)
                    jps_ok = ts.jps.select_ev(idx_jps_ok)
                else:
                    jps_ok = ts.jps.select_ev(idx_jps_ok)
                # Consider only post-seismic events
                ts_res_jps.jps = jps_ok.select_ev(jps_ok.type_ev=='P')
                if ts_res_jps.jps.shape() > 0:
                    # Inversion
                    ts_res_post = ts_res_jps.window_analysis(
                        pm.post_window_data, G_seas, pm.tau_post, pm.mod_post,
                        'post', pm.tau_spe, pm.pre_post, disp=pm.disp_window,
                        folder_disp=os.path.join(folder_window, f"POST{os.sep}"))
                    # Populate |ts.G| and |ts.MOD| with post window results
                    ts.G = np.c_[ts.G, ts_res_jps.G];
                    ts.MOD = np.vstack((ts.MOD, ts_res_jps.MOD))
                else:
                    ts_res_post = ts_res_jps.copy()
            
            else:
                ts_res_post = ts.copy()
                
            # Long-term phenomena inversion
            # Quadratic inversion
            if pm.acc:
                # Copy
                ts_acc = ts.copy()
                ts_res_post_acc = ts_res_post.copy()
                # Inversion
                ts_res_acc = ts_res_post_acc.longt_analysis(np.c_[tg**2, G_seas])
                # Recover all Jps events
                ts_res_acc.jps = ts.jps.copy()
                # Populate |ts_acc.G| and |ts_acc.MOD| with long-term phenomena
                # inversion results
                ts_acc.G = np.c_[ts_acc.G, ts_res_post_acc.G];
                ts_acc.MOD = np.vstack((ts_acc.MOD, ts_res_post_acc.MOD))
            # Linear inversion
            ts_res = ts_res_post.longt_analysis(G_seas)
            # Recover all Jps events
            ts_res.jps = ts.jps.copy()
            # Populate |ts.G| and |ts.MOD| with long-term phenomena inversion
            # results
            ts.G = np.c_[ts.G, ts_res_post.G];
            ts.MOD = np.vstack((ts.MOD, ts_res_post.MOD))
                
        
            #%%####################################
            ## DISPLAY ANALYSIS AND RESULTS DATA ##
            #######################################
            
            # Long-term phenomena inversion
            if pm.disp_window:
                from itsa.jps.Jps import Jps
                ts_res_post.jps = Jps(ts.code)
                ts_res_post.plot('darkgreen',
                                 ('Station '+ts_res_post.code
                                  + ' -- Seasonal inversion'),
                                 path_fig=os.path.join(folder_window, f"SEASONAL{os.sep}"))
        
            # Raw data and model
            ts.plot(name_fig=ts.code+'_data', path_fig=os.path.join(folder_fig, f"ANALYSIS{os.sep}"))
            
            # Residuals
            ts_res.plot('green', name_fig=ts_res.code+'_res',
                        path_fig=os.path.join(folder_fig, f"ANALYSIS{os.sep}"), size_marker=1)
            
            # Quadratic inversion
            if pm.acc:
                # Long-term phenomena inversion
                if pm.disp_window:
                    ts_res_post_acc.jps = Jps(ts.code)
                    ts_res_post_acc.plot('darkgreen',
                                         ('Station '+ts_res_post_acc.code
                                          + ' -- Seasonal inversion'),
                                         path_fig=os.path.join(folder_window, f"SEASONAL_QUA{os.sep}"),
                                         acc=True)
                # Raw data and model
                ts_acc.plot(name_fig=ts_acc.code+'_data',
                            path_fig=os.path.join(folder_fig, f"ANALYSIS_QUA{os.sep}"), acc=True) 
                # Residuals
                ts_res_acc.plot('green', name_fig=ts_res_acc.code+'_res',
                                path_fig=os.path.join(folder_fig, f"ANALYSIS_QUA{os.sep}"),
                                size_marker=1, acc=True)
            
        #%%#################################
        ## SAVE ANALYSIS AND RESULTS DATA ##
        ####################################
        
        # Data folder
        folder_out = os.path.join(pm.folder_res , argv[1], 'OUTPUT_FILES')
        folder_pos = os.path.join(folder_out, 'TS_DATA')
        
        # Save RAW time series
        ts.write_PBOpos(os.path.join(folder_pos, 'RAW'), replace=True)
        
        if pm.skip_outliers_filter == False:
            # Save Jps catalog
            ts.jps.write(os.path.join(folder_out, 'JPS'), replace=True)
            
            # Save Green's function and model amplitudes
            names_longt = ['Cst', 'Vel', 'An1', 'An2', 'Sm1', 'Sm2']
            ts.make_GMOD_names(names_longt, pm.tau_post, pm.tau_spe, pm.pre_post)
            ts.write_Gtxt(os.path.join(folder_out, 'G_MATRIX'), replace=True)
            ts.write_MODtxt(os.path.join(folder_out, 'MODEL_AMP'), replace=True)
            
            # Acceleration?
            if pm.acc:
                ts_acc.make_GMOD_names(['Acc']+names_longt, pm.tau_post,
                                       pm.tau_spe, pm.pre_post)
                ts_acc.write_Gtxt(os.path.join(folder_out, 'G_MATRIX_QUA'), replace=True)
                ts_acc.write_MODtxt(os.path.join(folder_out, 'MODEL_AMP_QUA'), replace=True)

            # Save QC indicators
            write_QC(ts.data, ts.code, folder_out)
            
            
            #%%###############################
            ## SAVE AND DISPLAY BY-PRODUCTS ##
            ##################################
            
            if pm.byp_make:
                save_byp(ts, pm.byp_vel, pm.byp_seas, pm.byp_ant, pm.byp_co,
                         pm.byp_sw, pm.byp_sse, pm.byp_post, pm.byp_names,
                         pm.disp_byp, folder_pos, folder_fig, replace=True)
                
                # Acceleration?
                if pm.acc:
                    # Convert all |pm.byp_| parameters into np.ndarray with same
                    # shape
                    from itsa.lib.modif_vartype import adapt_shape
                    (pm.byp_names, pm.byp_vel, pm.byp_seas, pm.byp_ant,
                     pm.byp_co, pm.byp_sw, pm.byp_sse, pm.byp_post,
                     pm.disp_byp) = adapt_shape([pm.byp_names, pm.byp_vel,
                                                 pm.byp_seas, pm.byp_ant,
                                                 pm.byp_co, pm.byp_sw, pm.byp_sse,
                                                 pm.byp_post, pm.disp_byp])
                    # Select only by-product impacted by acceleration
                    # and change by-product folder names
                    if isinstance(pm.byp_vel, np.ndarray):
                        # Select only by-product impacted by acceleration
                        spe_acc = (pm.byp_vel | pm.byp_seas).astype('bool')
                        # Change by-product folder names
                        byp_acc_names = np.char.add(
                            pm.byp_names[spe_acc], np.repeat('_QUA', sum(spe_acc)))
                        # Save and display
                        save_byp(ts_acc, pm.byp_vel[spe_acc], pm.byp_seas[spe_acc],
                                 pm.byp_ant[spe_acc], pm.byp_co[spe_acc],
                                 pm.byp_sw[spe_acc], pm.byp_sse[spe_acc],
                                 pm.byp_post[spe_acc], byp_acc_names,
                                 pm.disp_byp[spe_acc], folder_pos, folder_fig,
                                 replace=True)
                    elif pm.byp_vel | pm.byp_seas:
                        byp_acc_names = pm.byp_names+'_QUA'
                        # Save and display
                        save_byp(ts_acc, pm.byp_vel, pm.byp_seas, pm.byp_ant,
                                 pm.byp_co, pm.byp_sw, pm.byp_sse, pm.byp_post,
                                 byp_acc_names, pm.disp_byp, folder_pos,
                                 folder_fig, replace=True)

