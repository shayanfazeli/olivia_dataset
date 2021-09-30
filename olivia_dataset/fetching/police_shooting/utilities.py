import requests
import os
import pandas
from tqdm import tqdm
tqdm.pandas()
# from pandarallel import pandarallel
# pandarallel.initialize(progress_bar=True)
from olivia_dataset.utilities.config import read_olivia_dataset_config
from olivia_dataset.utilities.web.download import cookie_enabled_download

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


"""
from olivia_dataset.fetching.police_shooting.utilities import get_county, fetch_most_uptodate_police_shooting_data
df = fetch_most_uptodate_police_shooting_data()
"""


def fetch_most_uptodate_police_shooting_data() -> pandas.DataFrame:
    """
    Retrieving the police shooting data and adding the county column.
    If ran using 1-thread, it takes ~1 hour to complete.

    Returns
    ----------
    The dataframe which includes county column.
    """
    download_url = 'https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'
    df = pandas.read_csv(download_url)
    df['county'] = df.progress_apply(get_county, axis=1)
    return df


def retrieve_police_shooting_data() -> None:
    """
    Retrieving the county-included police shooting data.

    __Remark__: There might be location-based incompatibiltiies given that the county value does come from the
    coordinates. If incompatible, one option is to use the county's state instead of the recorded one. A decision
    about this needs ot be made.
    """
    # - retrieving the config
    config = read_olivia_dataset_config()
    livedataset_repo = config['livedataset_repo']
    filepath = os.path.join(livedataset_repo, 'resolution', 'county', 'county_level_police_shooting_data.csv')
    df = fetch_most_uptodate_police_shooting_data()
    df.to(filepath)
    logger.info("police shooting data is fetched.")


def get_county(x) -> str:
    """county adding"""
    try:
        url = 'https://geo.fcc.gov/api/census/area?lat=' + f"{x['latitude']}&lon={x['longitude']}" + '&format=json'
    except Exception as e:
        import pdb
        pdb.set_trace()

    params = dict(
        origin='Chicago,IL',
        destination='Los+Angeles,CA',
        waypoints='Joplin,MO|Oklahoma+City,OK',
        sensor='false'
    )

    resp = requests.get(url=url, params=params)
    data = resp.json() # Check the JSON Response Conte
    try:
        output = data['results'][0]['county_name']

        if output.lower().endswith('city') or output.lower().endswith('county') or output.lower().endswith('parish'):
            return ' '.join(output.split(' ')[:-1])
        else:
            return output
    except:
        return 'N/A'
