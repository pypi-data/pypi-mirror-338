"""This module has functions that allow for authentication, task submission, download"""

from datetime import datetime
import os
import requests


##################################################################################
##################################################################################

def create_log(dest_dir):
    """Creates a .txt log for MODIS task request submission and download.

    Parameters
    ----------
    dest_dir: str
        A directory that where the log file will be created.

    Returns
    -------
    logfilepath: str
        path to the log file
    """
    print('In the create_log() function, starting')
    datetime_now = datetime.now().strftime('%Y%m%d%H%M%S')
    logfile = f'MODIS_log_{datetime_now}.txt'
    logfilepath = os.path.join(dest_dir, logfile)

    print(f'In the create_log() function, logfilepath: {logfilepath}')

    with open(logfilepath,'a+', encoding="utf-8") as _:
        pass

    return logfilepath

def write_product_metadata(logfilepath, product_id):
    """Writes product (MODIS) metadata to .txt log file.

    Parameters
    ----------
    logfilepath: str
        path to the log file
    product_id: str
    """

    print(f'In the write_product_metadata() function, logfilepath: {logfilepath}')
    print(f'In the write_product_metadata() function, product_id: {product_id}')

    params = {'pretty': True}
    response = requests.get(
        f'https://appeears.earthdatacloud.nasa.gov/api/product/{product_id}',
        params=params, timeout=86400)
    dataset_metadata = response.text

    with open(logfilepath,'a+', encoding="utf-8") as f:
        f.write('Log file for MODIS download\n \n')
        f.write('#' * 80 + '\n')
        f.write('#' * 80 + '\n')
        f.write('\n \n')
        f.write(f'Information about the MODIS product with product_id={product_id}: \n \n')
        f.write(dataset_metadata)
        f.write('\n \n')
