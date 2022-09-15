import pandas as pd

df = pd.read_csv("./csv/gtfs_realtime.csv")

df.drop_duplicates(inplace=True)

df.to_csv("./csv/gtfs_realtime.csv",index=False)