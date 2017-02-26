import numpy as np
import pandas as pd
from datetime import datetime

def make_dataset():
    df = pd.read_csv("../Dataset/hr_race.csv")
    df = df.drop(['Unnamed: 0', 'id'], axis=1)
    
    df['rcDate'] = pd.to_datetime(df['rcDate'])
    df['year'] = pd.to_datetime(df.rcDate).dt.year
    df['rcTime'] = pd.to_datetime(df['rcTime']).apply(lambda d: datetime.time(d))
    
    df['ord'] = np.nan_to_num(df['ord']).astype(int)
    df['plc'] = np.nan_to_num(df['plc']).astype(int)
    df['win'] = np.nan_to_num(df['win']).astype(int)
    
    df['isWin'] = df['ord']==(1 or 2)
    df = df.drop(df['ord']==0)
    
    train = df[df['year'] < 2014]
    test = df[df['year'] >= 2014]

    print("Make racing dataset...")
    return train, test