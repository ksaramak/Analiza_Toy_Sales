import pandas as pd
plik = "Desktop/Projekty/Analiza_Toy_Sales/Ecommerce_data_toy_sales.xlsx"
plik = pd.read_excel(plik)
print(plik.dtypes)

print(plik)
print(plik.describe())

plik = plik.dropna()
plik=plik[plik["Product_id"] != "missing"]
plik["Product_id"] = plik["Product_id"].astype(int)

plik=plik[plik["Quantity"] >= 1]

plik["CustomerID"] = plik["CustomerID"].astype(int)

plik["Country"] = plik["Country"].replace("UK", "United Kingdom")

plik["ShippingDate"] = plik["ShippingDate"].str.replace("day", "")
plik["ShippingDate"] = plik["ShippingDate"].str.replace(",", ".")
plik["ShippingDate"] = plik["ShippingDate"].astype(float)
plik["ShippingDate"] = pd.to_datetime(plik["ShippingDate"], unit='D', origin='1899-12-30')
plik["ShippingDate"] = plik["ShippingDate"].dt.round("s")

print(plik)
print(plik.describe())
print(plik.dtypes)

plik.to_excel("Desktop/Projekty/Analiza_Toy_Sales/Clean_Ecommerce_data_toy_sales.xlsx", index=False)