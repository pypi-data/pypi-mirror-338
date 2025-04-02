"""This module makes the MODIS download automatic"""

import os
import toml

from ModImpNetTest.modis_requests import create_log, write_product_metadata


##################################################################################
##################################################################################

def download_modis(config_toml_path):
    """Downloads the MODIS results in csv form, saves them to a directory, and writes a text log.

    Parameters
    ----------
    config_toml_path: str
        path to the TOML configuration file

    Returns
    -------
    .csv files with MODIS data
    .txt log file
    """

    print(f'In the download_modis() function, config_toml_path: {config_toml_path}')

    with open(config_toml_path, 'r', encoding="utf-8") as f:
        config = toml.load(f)
        print(f'In the download_modis() function, opened config_toml_path: {config_toml_path}')


    list_product_id = ['MOD10A1.061', 'MOD11A1.061']

    dest_dir = config['directories']['dest_dir']
    os.makedirs(dest_dir, exist_ok=True)
    print(f'In the download_modis() function, dest_dir: {dest_dir}')
    print('In the download_modis() function, about to run create_log() function')
    logfilepath = create_log(dest_dir)
    print('In the download_modis() function, finished running create_log() function')
    print(f'In the download_modis() function, logfilepath: {logfilepath}')
    for product_id in list_product_id:
        print(f'In the download_modis() function, product_id: {product_id}')
        print('In the download_modis() function, about to run write_product_metadata() function')
        write_product_metadata(logfilepath, product_id)
        print('In the download_modis() function, finished running write_product_metadata() function')
