import pandas as pd
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    melb_data = pd.read_csv("dataset/melb_data.csv")
    print(type(melb_data.isnull().sum()))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
