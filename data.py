
import pandas as pd
import random



df = pd.read_csv("FinalCharity.csv")
df['_id'] = df.reset_index().index + 1
df.set_index("_id", inplace = True)
df.to_csv("FinalCharity.csv")
