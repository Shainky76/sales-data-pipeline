import pandas as pd

df = pd.read_csv('sales.csv')
# filter data whose amount < 60
df = df[df['amount'] > 60].copy()
df.loc[df['amount'] >= 200, 'status'] = 'VIP'
df.loc[df['amount'] < 200, 'status'] = 'Regular'

df.to_csv('cleaned_sales.csv', index=False)
