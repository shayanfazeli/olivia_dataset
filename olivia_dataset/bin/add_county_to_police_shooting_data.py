import argparse
import pandas
import time
import os, sys
sys.path.append('/Users/mednet_machine/PHOENIX/ai_health_informatics/pandemic_modeling/olivia_dataset')
from olivia_dataset.fetching.police_shooting.utilities import get_county
import numpy
from tqdm import tqdm
# from pandarallel import pandarallel
# pandarallel.initialize()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_filepath", type=str, required=True)
    parser.add_argument("--output_filepath", type=str, required=True)

    args = parser.parse_args()

    df = pandas.read_csv(args.input_filepath)

    t1 = time.time()
    df['county'] = df.apply(get_county, axis=1)
    print(f"time spent: {time.time() - t1}")

    df.to_csv(args.output_filepath, index=False)
    print("all done.")