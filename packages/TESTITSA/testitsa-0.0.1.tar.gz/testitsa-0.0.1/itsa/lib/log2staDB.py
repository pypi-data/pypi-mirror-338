#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:20:52 2024

@author: tsaponga
"""

# Import necessary modules
from sys import argv
from pathlib import Path
from datetime import datetime

def date_format(install_date):
    if install_date.strip() and install_date[-1] != 'Z':
        return "%Y-%m-%d"
    else:
        return "%Y-%m-%dT%H:%MZ"
        
def convert_log_to_staDB(log_file, output_directory):
    """
    Convert a station log file to staDB format by extracting receiver and antenna information.
    
    :param log_file: The station log file to process
    :param output_directory: The directory to save the staDB output file
    """
    
    # Lists to store receiver and antenna data
    receiver_data = []
    antenna_data = []
    
    # Open and read the log file
    with open(log_file, 'r') as file:
        line = file.readline()
        #station_marker = line.split()[0][0:4]  # Extract station marker (first 4 characters)
        station_marker = line.split()[0]
        
        while line:
            line = file.readline()
            
            # Extract coordinates and installation date
            if "Site Identification" in line:
                while "Receiver Information" not in line:
                    if "Date Installed" in line:
                        install_date = line.split(" :")[-1].strip()
                    elif "X coordinate" in line:
                        x_coordinate = line.split()[-1]
                    elif "Y coordinate" in line:
                        y_coordinate = line.split()[-1]
                    elif "Z coordinate" in line:
                        z_coordinate = line.split()[-1]
                    line = file.readline()
                
                try:
                    # Format the installation date and create the coordinate entry
                    install_date = datetime.strptime(install_date,  date_format(install_date)).strftime("%Y-%m-%d %H:%M:%S")
                    coordinates_entry = f"{station_marker}  STATE  {install_date}  {x_coordinate}  {y_coordinate}  {z_coordinate}   0.0   0.0   0.0"
                except ValueError:
                    pass
                    #print(f"Invalid date format 1: {install_date}")
            
            # Extract antenna information
            if "Antenna Type" in line:
                while "Date Removed" not in line:
                    if "Antenna Type" in line:
                        antenna_type = ' '.join(line.split(" :")[-1].split())
                    elif "Up Ecc" in line:
                        up_eccentricity = line.split(" :")[-1].strip()
                    elif "North Ecc" in line:
                        north_eccentricity = line.split(" :")[-1].strip()
                    elif "East Ecc" in line:
                        east_eccentricity = line.split(" :")[-1].strip()
                    elif "Serial Number" in line:
                        antenna_serial_number = line.split(" :")[-1].strip()
                    elif "Date Installed" in line:
                        antenna_install_date = line.split(" :")[-1].strip()
                    line = file.readline()
                
                try:
                    # Format the antenna installation date and create the antenna entry
                    antenna_install_date = datetime.strptime(antenna_install_date,  date_format(antenna_install_date)).strftime("%Y-%m-%d %H:%M:%S")
                    antenna_data.append(f"{station_marker}  ANT    {antenna_install_date}  {antenna_type}   {east_eccentricity}   {north_eccentricity}   {up_eccentricity} #{antenna_serial_number}")
                except ValueError:
                    pass
                    #print(f"Invalid date format 2: {antenna_install_date}")
            
            # Extract receiver information
            if "Receiver Type" in line:
                while "Date Removed" not in line:
                    if "Receiver Type" in line:
                        receiver_type = line.split(" :")[-1].strip()
                    elif "Firmware Version" in line:
                        firmware_version = line.split(" :")[-1].strip()
                    elif "Date Installed" in line:
                        receiver_install_date = line.split(" :")[-1].strip()
                    line = file.readline()
                
                try:
                    # Format the receiver installation date and create the receiver entry
                    receiver_install_date = datetime.strptime(receiver_install_date,  date_format(receiver_install_date)).strftime("%Y-%m-%d %H:%M:%S")
                    receiver_data.append(f"{station_marker}  RX     {receiver_install_date}  {receiver_type} #{firmware_version}")
                except ValueError:
                    pass
                    #print(f"Invalid date format 3: {receiver_install_date}")
    
    # Save the data in the staDB format
    output_file = f"{output_directory}/{station_marker.lower()}.sta_db"
    
    with open(output_file, 'w') as output:
        output.write("KEYWORDS: ID STATE END ANT RX\n")
        output.write(f"{station_marker}  ID  UNKNOWN  {station_marker}\n")
        output.write(f"{coordinates_entry}\n")
        
        for antenna_entry in antenna_data:
            output.write(f"{antenna_entry}\n")
        
        for index, receiver_entry in enumerate(receiver_data, 1):
            if index == len(receiver_data):
                gotoLine = ""
            else:
                gotoLine = "\n"
            output.write(f"{receiver_entry}{gotoLine}")
# ConnectionError
if __name__ == "__main__":
    # Validate command line arguments
    if len(argv) <= 1:
        raise ValueError("No arguments passed. Provide a station log file.")
    elif len(argv) > 3:
        raise ValueError("Too many arguments passed. Provide exactly two arguments: log file and output directory.")
        
    # Validate the log file path
    if not Path(argv[1]).exists() or not Path(argv[1]).is_file():
        raise ValueError(f"Input file {argv[1]} is not valid.")
        
    # Validate the output directory
    if not Path(argv[2]).exists():
        try:
            Path(argv[2]).mkdir()
        except FileNotFoundError as e:
            raise ValueError(f"Invalid output directory, could not be created: {e}")
    
    # Validate the log file format
    first_line = open(argv[1], 'r').readline()
    if "Site Information Form (site log)" not in first_line:
        raise ValueError("Invalid file format. Ensure the file follows the M3G site log format (https://gnss-metadata.eu/).")
    
    # Run the log conversion function
    convert_log_to_staDB(argv[1], argv[2])