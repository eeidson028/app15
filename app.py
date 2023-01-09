from flask import Flask, render_template, url_for
app = Flask(__name__)

import pandas as pd
df=pd.read_csv('data.csv')
Credit_Total = int(df['Credit'].sum())
Debit_Total = int(df['Debit'].sum())
Net = '{:,}'.format(Credit_Total - Debit_Total)
Bal2 = int(df['Balance'][0])
Bal = '{:,}'.format(Bal2)
cost_num_cats = df.groupby("Classification")["Debit"].sum().sort_values().tail(10).to_list()
cost_class_cats =df.groupby("Classification")["Debit"].sum().sort_values().tail(10).keys().to_list()

RN = df['Credit'].dropna().sort_values().tail(15).values.tolist()

RC = df[['Description','Credit']].dropna().sort_values(by='Credit').tail(15)
RC2 = RC['Description'].values.tolist()

test6 = df[['Post Date','Credit']].dropna().sort_values(by='Credit').tail(15)
dates2= test6['Post Date'].to_list()



@app.route('/')
def index(
    DT=Debit_Total,
    CT=Credit_Total,
    NT=Net,
    BL=Bal,
    CC = cost_num_cats,
    CLC= cost_class_cats,
    RN=RN,
    RC2=RC2,
    DAT=dates2
    ):
    
    return render_template('index.html',DT=DT,CT=CT,NT=NT,
            BL=BL, CC=CC, CLC=CLC, RN=RN, RC2=RC2,DAT=DAT)


if __name__ == '__main__':
   app.run(debug = True)


