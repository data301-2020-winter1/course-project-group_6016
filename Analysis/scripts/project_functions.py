import numpy as np
import pandas as pd

csv = r"Electric_Vehicle_Population_Data.csv"

def load_and_process(csv_file):
    
    df1 = (
        pd.read_csv(csv_file)
        .drop('State', axis=1)
        .drop('Clean Alternative Fuel Vehicle (CAFV) Eligibility', axis=1)
        .drop('Legislative District', axis=1)
        .drop('DOL Vehicle ID', axis=1)
        .rename(columns={'VIN (1-10)': 'VIN'})
        .rename(columns={'ZIP Code': 'ZIP'})
        .rename(columns={'Model Year': 'Model_Year'})
        .rename(columns={'Electric Vehicle Type': 'EV_Type'})
        .rename(columns={'Electric Range': 'Range'})
        .rename(columns={'Base MSRP': 'MSRP'})
        .rename(columns={'Vehicle Location': 'Location'})
        .dropna()
        .reset_index(drop=True)
    )
    
    df1.loc[df1.EV_Type == 'Plug-in Hybrid Electric Vehicle (PHEV)', 'EV_Type'] = 'PHEV'
    df1.loc[df1.EV_Type == 'Battery Electric Vehicle (BEV)', 'EV_Type'] = 'BEV'
    
    df1['Latitude'] = df1.apply(lambda row: float(row.Location.split(" ")[2].split(")")[0]), axis = 1)
    df1['Longitude'] = df1.apply(lambda row: float(row.Location.split(" ")[1].split("(")[1]), axis = 1)
    df1['North_South'] = np.where(df1['Latitude']>=47.2, 'North', 'South')
    df1['West_East'] = np.where(df1['Longitude']>=120, 'West', 'East')
    return df1