"""
Stef
30/01/2018
"""

import os
import src.utils.file_manager as fm


def main():

    path_data = os.path.join("D:", "Administratie", "uitgaven")
    file_name = "mutations20180130221630.csv"
    headers = [
        "Date", "Destination Account", "Amount", "Type",
        "Name Src Account Holder", "Source Account", "Code", "Description"]
    df = fm.read_pandas(os.path.join(path_data, file_name), sep=",", headers=headers)
    print(len(df.columns))
    print(df.columns)
    print(df.head(5))
    print(type(df["Date"].iloc[0]))
    fm.write_pandas(df=df, path=os.path.join(path_data, "uitgaven_triodos.csv"))


if __name__ == "__main__":
    main()