import pandas as pd

df=pd.read_csv('data.csv')

Credit_Total = df['Credit'].sum()

Debit_Total = df['Debit'].sum()

