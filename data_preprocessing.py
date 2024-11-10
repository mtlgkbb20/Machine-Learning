import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

# Load the data
data = pd.read_csv('PlayTennis.csv')
print(data)