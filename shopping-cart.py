import pandas as pd
import requests

products_url="https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv"

#products=requests.get(products_url)

#print(products.text)

df=pd.read_csv(products_url)

print(df.head(20))
