import pandas as pd
df=pd.read_csv('/content/Electric_Vehicle_Population_Data.csv')
df.shape
df.info()
df.head()
df.isnull().sum()
nunique_values = [col for col in df.columns if df[col].nunique()< len(df)]
print(nunique_values)
df_cleaned=df.dropna()
df_cleaned.isnull().sum()
df_cleaned.shape
df_cleaned= df_cleaned.drop(columns=['VIN (1-10)', 'DOL Vehicle ID', 'Vehicle Location', 'Postal Code'])
df_cleaned.shape
df_cleaned["EV_Type_Code"]= df_cleaned["Electric Vehicle Type"].map({"Battery Electric Vehicle (BEV)": 1, "Plug-in Hybrid Electric Vehicle (PHEV)": 2})
