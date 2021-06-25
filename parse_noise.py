import pandas as pd
import numpy as np

from datetime import datetime
from datetime import time


def read_noise_csv(file):

    df = pd.read_csv(file, delimiter=";", skiprows=list(range(8)))

    return df


def combine_date_hour(row):

    date = row["Data"]
    hour = row["Ora"]

    parsed_date = datetime.strptime(
        date, "%d-%m-%Y"
    )

    parsed_hour = datetime.strptime(
        hour, "%H:%M"
    ).time()

    combined_date = datetime.combine(
        parsed_date, parsed_hour
    )

    return combined_date



def convert_float(num):

    if isinstance(num, str):
        return float(num.replace(",","."))