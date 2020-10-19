import pandas as pd

def formatsize(size):
    if size[-1] == 'M':
        return (int(size[0:-1])*1024)
    else:
        return int(size) 

def normalizeFields(input_df):

    # Format the number of installs
    input_df["Installs"] = input_df["Installs"].map(
        lambda x: x.strip()
                   .replace('+', '')
                   .replace(',', '')
    ).astype(int)

    # Format the size
    input_df["Size"] = input_df["Size"].map(formatsize).astype(int)
    return input_df