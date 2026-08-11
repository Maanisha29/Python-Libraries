import numpy as np
import pandas as pd
data = {
    "Name": ["Arun", "Priya", "Ravi", "Divya", "Arun"],
    "Age": [20, 21, np.nan, 22, 20],
    "City": ["salem", "Chennai", "SALEM", " chennai ", "salem"],
    "Marks": [80, np.nan, 65, 90, 80]
}
pd=pd.DataFrame(data)
print(pd)
print(pd.isnull())
print(pd.isnull().sum())
pd["Age"]=pd["Age"].fillna(pd["Age"].mean())
pd["Marks"]=pd["Marks"].fillna(pd["Marks"].mean())
print(pd.duplicated())
print(pd.duplicated().sum())
pd =  pd.drop_duplicates()
print(pd)
print(pd["City"].value_counts())
pd["City"]=pd["City"].replace("UnKnown",np.nan)
print(pd)
pd["City"]=pd["City"].fillna(pd["City"].mode()[0])
print(pd)

