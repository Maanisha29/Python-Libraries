import numpy as np
import pandas as pd
data={
    "Name":["Arun","Priya","Ravi","Arun","Divya"],
    "Age":[21,np.nan ,20,21,22],
    "City":["Salem","Chennai","Salem","SALEM","Unknown"],
    "Salary":[30000,45000,np.nan,30000,50000]
}
pd=pd.DataFrame(data)
print(pd.isnull().sum())