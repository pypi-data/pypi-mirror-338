"""
    itsa_launcher.py
    ---------------------------
    Launcher for ITSA workflow

    author: Bertrand Lovery

    Usage:
    - to run in parallel several stations from prompt:
    itsa_launcher.py -m par -s ATIC CBRO
    - to process as OAR tasks stations listed in a file:
    itsa_launcher.py -m oar -f stations.txt

    Options:
    -v <int> : set verbosity
    -m <str> : set operating mode
    -s <str> : stations to process
    -f <str> : name of the file were stations are listed
"""

import sys
import os
import logging
import argparse
import subprocess
import multiprocessing as mp
from multiprocessing.pool import Pool
from tqdm import tqdm
import socket


python_alias = "python3"

def work_local(station):
    return subprocess.call([python_alias, "itsa/tsanalysis_itsa.py", station])


def work_oar(station, host, workdir):
    if host == "ist-oar":
        return subprocess.call(["oarsub", "--project", "iste-pro-gpsall", "-l", "/nodes=1/core=1,walltime=06:00:00", 
                                f"source /soft/env.bash; module load python/python3.9; ipython3 {workdir}/tsanalysis_itsa.py {station}"])
    else:
        return subprocess.call(["oarsub", "--project", "f-cycle", "-l", "/nodes=1/core=1,walltime=06:00:00", 
                                f"ipython3 {workdir}/tsanalysis_itsa.py {station}"])


def update_progress_bar(_):
    progress_bar.update()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Dispatch jobs in sequential, parallel, or OAR mode")
    parser.add_argument("-v", type=int, default=3, choices=[0, 1, 2, 3, 4],
                        help=("Define verbosity:"
                              "0: critical, 1: error, 2: warning, "
                              "3: info, 4: debug, default=info"))
    parser.add_argument("-m", type=str, default="par", choices=["seq", "par", "oar"],
                        help=("Define operating mode:"
                              "seq: sequential, par: parallel, "
                              "oar: OAR submissions"))
    parser.add_argument("-s", nargs='+', help="Stations to be processed")
    parser.add_argument("-f", type=str, help="File with stations to be processed")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])              
    logging_translate = [logging.CRITICAL, logging.ERROR, logging.WARNING,
                         logging.INFO, logging.DEBUG]
    logging.basicConfig(level=logging_translate[args.v])

    logger = logging.getLogger()

    if args.s and args.f:
        raise ValueError("You cannot use both -s and -f arguments, please keep only one!")
    elif args.s:
        stations = args.s
    else:
        stations = []
        with open(args.f, "r") as sta_file:
            for station in sta_file:
                stations.append(station.strip())

    if args.m == "seq":
        for station in stations:
            logger.info(f"Launching processing for station {station}...")
            work_local(station)
    elif args.m == "par":
        logger.info(f"Launching parallel processing for stations {stations}...")
        nb_proc = max(min(mp.cpu_count()-1, len(stations)), 1)
        progress_bar = tqdm(total=nb_proc)
        pool = Pool(nb_proc)
        for station in stations:
            pool.apply_async(work_local, args=(station,), callback=update_progress_bar)
        pool.close()
        pool.join()
    else:
        hostname = socket.gethostname()
        if "ist-oar" in hostname:
            max_sub = 20
        elif "luke" in hostname:
            max_sub = 30
        elif"dahu" in hostname:
            max_sub = 40
        if not "ist-oar" in hostname and not "luke" in hostname and not "dahu" in hostname:
            raise SystemError("You are not working on a supported system for 'oar' mode, please retry in 'par' or 'seq' mode!")
        logger.info(f"Launching parallel processing for stations {stations}...")
        nb_proc = max(min(len(stations), max_sub), 1)
        workdir = os.getcwd()
        progress_bar = tqdm(total=nb_proc)
        pool = mp.Pool(nb_proc)
        for station in stations:
            pool.apply_async(work_oar, args=(station, hostname, workdir,), callback=update_progress_bar)
        pool.close()
        pool.join()
    if len(stations) == 1:
        logger.info(f"Processing is over! 1 station has been processed")
    else:
        logger.info(f"Processing is over! {len(stations)} stations have been processed")

