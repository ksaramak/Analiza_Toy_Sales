import pandas as pd
#załadowanie danych
plik = "Desktop/Projekty/Analiza_Toy_Sales/Ecommerce_data_toy_sales.xlsx"
dane = pd.read_excel(plik)
print(dane.dtypes)

print(dane)
print(dane.describe())

#usuniecie duplikatów i pustych wierszy
dane = dane.drop_duplicates()
dane = dane.dropna()

#Usuniecie niepotrzebnych znaków oraz zmiana typu InvoiceNo 
dane["InvoiceNo"] = dane["InvoiceNo"].str.replace(r'[a-zA-Z]', '', regex=True)
dane["InvoiceNo"] = dane["InvoiceNo"].astype(int)

#usuniecie wierszy z wartością "missing" oraz zmienienie typu w kolumnie
dane=dane[dane["Product_id"] != "missing"]
dane["Product_id"] = dane["Product_id"].astype(int)

#wybranie jedynie wierszy z poprawnymi wartościami kolumny "Quantity"
dane=dane[dane["Quantity"] >= 1]

#zmiana typu kolumny "CustomerID"
dane["CustomerID"] = dane["CustomerID"].astype(int)

#Ujednolicenie "UK" oraz "United Kingdom" do "United Kingdom"
dane["Country"] = dane["Country"].replace("UK", "United Kingdom")

#Poprawienie dat dla kolumny "ShippingDate"
dane["ShippingDate"] = dane["ShippingDate"].str.replace("day", "")
dane["ShippingDate"] = dane["ShippingDate"].str.replace(",", ".")
dane["ShippingDate"] = dane["ShippingDate"].astype(float)
dane["ShippingDate"] = pd.to_datetime(dane["ShippingDate"], unit='D', origin='1899-12-30')
dane["ShippingDate"] = dane["ShippingDate"].dt.round("s")

print(dane)
print(dane.describe())
print(dane.dtypes)

#Sprawdzenie co powoduje ogromny skok we wrzesniu
wrzesien = dane[dane["InvoiceDate"].dt.month == 9]
print(wrzesien.sort_values(by="Quantity", ascending = False))

#Stworzenie zbioru bez jednego zamowienia powodujacego wielki skok we wrzesniu
dane_dokladne = dane[dane["InvoiceNo"] != 581483 ]

dane.to_excel("Desktop/Projekty/Analiza_Toy_Sales/Clean_Ecommerce_data_toy_sales.xlsx", index=False)
dane_dokladne.to_excel("Desktop/Projekty/Analiza_Toy_Sales/Clean_bez_jednego_Ecommerce_data_toy_sales.xlsx", index=False)