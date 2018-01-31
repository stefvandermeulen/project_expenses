"""
Stef
30/01/2018
"""

import pandas as pd
import os
import datetime


PATH_HOME = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DEFAULT_DTYPES = {}


def str2float(string: str) -> float:
    if "," not in string:
        return float(string)
    string = string.replace(".", "")
    string = string.replace(",", ".")
    return float(string)


def str2date(string: str) -> datetime.date:

    try:
        return datetime.datetime.strptime(string, "%d-%m-%Y").date()
    except ValueError as e:
        return datetime.datetime.strptime(string, "%Y-%m-%d").date()


def create_dir(path: str) -> bool:

    if os.path.isdir(path):
        print("{} already exists".format(path))
        return True

    os.mkdir(path)
    return True


def read_pandas(path: str, headers: list = None, sep: str= ",", **kwargs) -> pd.DataFrame:

    names = headers

    if headers is None:
        with open(path, "r") as f:
            headers = f.readline().split(sep)

    converters = {}
    for key, value in DEFAULT_DTYPES.items():
        if key in headers:
            converters[key] = value

    converters["Amount"] = str2float
    converters["Date"] = str2date

    return pd.read_csv(path, names=names, sep=sep, converters=converters, **kwargs)


def write_pandas(df: pd.DataFrame, path: str) -> bool:

    create_dir(path)

    df.to_csv(path_or_buf=path, index=False)
    print("df written to {}".format(path))
    return True


def main():
    print(PATH_HOME)


if __name__ == "__main__":
    main()