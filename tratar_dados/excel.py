import pandas as pd


df = pd.read_excel('documentos\pedido.xlsx')

# print(df.columns)

swag = df.loc[df['Unnamed: 7'].isin(['A PAGAR', 'a pagar'])]

totalpagar = swag.values[0][-1]  # -1 traz o ultimo elemento da lista

print(totalpagar)