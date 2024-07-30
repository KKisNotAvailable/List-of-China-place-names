import pandas as pd
import numpy as np

# check out https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
pd.options.mode.copy_on_write = True

def analysis(df: pd.DataFrame):
    # ----------
    # Preporcess
    # ----------
    # promote means the promotion year, so none year digits and NaN set to 0
    df.fillna({'promote': 0}, inplace=True)
    df.loc[df['promote'] < 1800, "promote"] = 0

    print(min(df[df['promote'] > 0]['promote']))
    return

def main():
    df = pd.read_excel("books/data_port_processed.xlsm", sheet_name="Sheet1")

    print(df.shape)
    print(df.columns)

    cols_to_keep = [
        "year", "rank", "begin", "promote", "transfer",
        "pay", "areacode", "portcode", "certainty_lvl",
        "port", "possible_names"
    ]

    # I thought "year" should be the observation year
    # and "begin" should be the year this guy started this job
    # there are several records having year > begin
    # TODO: find the several extent
    analysis(df[cols_to_keep])

if __name__ == "__main__":
    main()