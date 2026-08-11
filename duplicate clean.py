import numpy as np
import pandas as pd
data={
    "Name":["Arun","Priya","Ravi","tharun","Arun"],
    "Age":[21,np.nan ,20,21,22],
    "City":["Salem","CHENNAI","Salem","Unknown","Salem"],
    "Salary":[30000,45000,np.nan,60000,50000]
}
pd=pd.DataFrame(data)
print(pd)
#pd["Age"]=pd["Age"].fillna(pd["Age"].mean())
#pd["Salary"]=pd["Salary"].fillna(pd["Salary"].mean())
print(pd.duplicated())
print(pd.duplicated().sum())
print(pd)
#pd = pd.drop_duplicates()