import pandas
df=pandas.read_excel(r'C:\Users\TA0097\Desktop\TEST.xlsx')
print(df)
gb=df.groupby('Name').agg('sum')
print(gb)