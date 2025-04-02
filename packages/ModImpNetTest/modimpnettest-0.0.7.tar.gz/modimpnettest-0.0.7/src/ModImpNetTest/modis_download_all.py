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

    print(f'Hello: {config_toml_path}')

    # with open(config_toml_path, 'r', encoding="utf-8") as f:
    #     config = toml.load(f)

    # list_product_id = ['MOD10A1.061', 'MOD11A1.061']

    # dest_dir = config['directories']['dest_dir']
    # os.makedirs(dest_dir, exist_ok=True)
    # logfilepath = create_log(dest_dir)
    # for product_id in list_product_id:
    #     write_product_metadata(logfilepath, product_id)
