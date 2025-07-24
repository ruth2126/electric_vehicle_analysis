import pandas as pd
df=pd.read_csv('/content/Electric_Vehicle_Population_Data.csv')
df.shape
df.info()
df.head()
df.isnull().sum()