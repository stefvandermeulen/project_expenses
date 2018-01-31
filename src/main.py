"""
Stef
30/01/2018
"""

import os
import pandas as pd
import src.utils.file_manager as fm
from src.visualisation.plot import Plotter


def credit_or_debet(row: pd.Series) -> float:
    if row["Type"] == "Credit":
        return row["Amount"]
    return -1 * row["Amount"]

def main():

    path_data = os.path.join("D:", "Administratie", "uitgaven")
    path_expenses = os.path.join(path_data, "uitgaven_triodos.csv")
    path_plots = os.path.join(path_data, "plots")

    if not os.path.isfile(path_expenses):
        file_name = "mutations20180130221630.csv"
        headers = [
            "Date", "Destination Account", "Amount", "Type",
            "Name Src Account Holder", "Source Account", "Code", "Description"]
        df = fm.read_pandas(os.path.join(path_data, file_name), sep=",", headers=headers)
        fm.write_pandas(df=df, path=os.path.join(path_data, "uitgaven_triodos.csv"))
    else:
        df = fm.read_pandas(path=path_expenses, sep=",")

    df["Amount"] = df[["Amount", "Type"]].apply(credit_or_debet, axis=1)

    df_grouped = df.groupby(by="Date").agg(sum).reset_index()
    df_grouped["Amount_cumsum"] = df_grouped["Amount"].cumsum()

    plotter = Plotter(path_output=path_plots)
    plotter.plot(df=df_grouped)


if __name__ == "__main__":
    main()