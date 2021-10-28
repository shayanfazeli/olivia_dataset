from datetime import datetime, date, timedelta
import time
import numpy
import pandas
import os
import json
from epiweeks import Week
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
from copy import deepcopy

from olivia_dataset.utilities.config import read_olivia_dataset_config

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def retrieve_health_center_program_participants() -> None:
    """
    The health-center program participants
    """
    # - retrieving the config
    config = read_olivia_dataset_config()
    livedataset_repo = config['livedataset_repo']

    cache_folder = os.path.abspath(os.path.join(os.path.expanduser("~"), '.olivia_dataset'))
    os.makedirs(cache_folder, exist_ok=True)

    os.makedirs(os.path.join(livedataset_repo, 'resolution', 'state', 'hrsa'), exist_ok=True)
    filepath = os.path.join(livedataset_repo, 'resolution',  'state', 'hrsa', 'health_center_program_participants.csv')

    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    full_df = []
    for state in tqdm(states):
        vgm_url = f'https://www.hrsa.gov/coronavirus/health-center-program/participants/{state}'
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        data = []
        list_header = []
        header = soup.find_all("table")[0].find("tr")

        for items in header:
            try:
                list_header.append(items.get_text())
            except:
                continue

        HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

        for element in HTML_data:
            sub_data = []
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text())
                except:
                    continue
            data.append(sub_data)

        table = pd.DataFrame(data = data, columns = list_header)
        full_df.append(deepcopy(table))

    full_df = pd.concat(full_df)
    full_df = full_df.loc[:, [e for e in full_df.columns if not e=='\n']]

    full_df.reset_index(drop=True, inplace=True)

    full_df.to_csv(filepath)
    logger.info(f"the hrsa health center program participants file has been successfully saved into {filepath}")
