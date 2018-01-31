"""
Stef
31/01/2018
"""
import os
import pandas as pd
import plotly as py

from plotly.graph_objs import Scatter

import src.utils.file_manager as fm


class Plotter(object):

    def __init__(self, path_output: str):
        self.path_output = path_output
        fm.create_dir(path_output)

    def plot(self, df: pd.DataFrame):
        # Create a trace
        trace1 = Scatter(x=df["Date"], y=df["Amount"], mode="line")
        trace2 = Scatter(x=df["Date"], y=df["Amount_cumsum"], mode="line")
        data = [trace1, trace2]
        py.offline.plot(data, filename=os.path.join(self.path_output, "triodos_expenses.html"))


def main():
    pass


if __name__ == "__main__":
    main()