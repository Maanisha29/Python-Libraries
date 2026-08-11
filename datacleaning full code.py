import numpy as np
import pandas as pd
data = {
    "Name": [
        "Arun", "Priya", "Ravi", "Divya", "Kumar",
        "Meena", "Suresh", "Latha", "Rahul", "Anitha",
        "Vijay", "Sneha", "Manoj", "Kavya", "Ajay",
        "Deepa", "Ramesh", "Harini", "Prakash", "Arun"
    ],

    "Age": [
        20, 21, None, 22, 21,
        20, 23, 21, None, 20,
        21, 22, 23, 20, 21,
        22, None, 20, 22, 20
    ],

    "Study_Hours": [
        5, 7, 3, None, 2,
        6, 4, 7, 3, 9,
        None, 8, 4, 6, 2,
        7, 3, 8, None, 5
    ],

    "Attendance": [
        85, 92, 65, 95, None,
        88, 72, 90, 60, 96,
        80, None, 70, 86, 58,
        91, 68, 89, 82, 85
    ],

    "CGPA": [
        8.2, 9.1, 6.5, 9.3, 5.8,
        8.5, None, 8.9, 6.2, 9.5,
        7.8, 9.0, 6.8, None, 5.9,
        8.7, 6.4, 8.8, 7.6, 8.2
    ],

    "City": [
        "Salem", "Chennai", "Salem", "Madurai", "Chennai",
        "salem", "Chennai", "MADURAI", "Salem", "Chennai",
        "Salem", "Chennai", "Madurai", "salem", "Chennai",
        "Madurai", "Salem", "Chennai", " Madurai ", "Salem"
    ],

    "Result": [
        "Pass", "Pass", "Fail", "Pass", "Fail",
        "Pass", "Pass", "Pass", "Fail", "Pass",
        "Pass", "Pass", "Fail", "Pass", "Fail",
        "Pass", "Fail", "Pass", "Pass", "Pass"
    ]
}
pd=pd.DataFrame(data)
print(pd)
print(pd.isnull())

print(pd.isnull().sum())
pd["Age"]=pd["Age"].fillna(pd["Age"].mean()).round().astype(int)
pd["Study_Hours"]=pd["Study_Hours"].fillna(pd["Study_Hours"].mean()).round().astype(int)
pd["Attendance"]=pd["Attendance"].fillna(pd["Attendance"].mean()).round().astype(int)
pd["CGPA"]=pd["CGPA"].fillna(pd["CGPA"].mean()).round().astype(int)
print(pd)
print(pd.duplicated())
print(pd.duplicated().sum())
pd=pd.drop_duplicates()
print(pd)