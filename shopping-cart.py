import pandas as pd
import requests

products_url="https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv"

#    id                                               name                          aisle       department  price
#     1                         Chocolate Sandwich Cookies                  cookies cakes           snacks   3.50
#     2                                   All-Seasons Salt              spices seasonings           pantry   4.99



df=pd.read_csv(products_url)

print(df.head(20))


selected_products = [] 

while True:
    selected_id = input("Please input a product id, or 'DONE': " )

    if selected_id.upper() == "DONE":
        break # break out of the while loop 
    else:
        print("LOOKING UP PRODUCT", selected_id)
        for x in range(0,len(df),1):
            if str(selected_id) == str(df["id"][x]):
                matching_product = str(df["name"][x])
            #else:
                #matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
                #matching_product = matching_products[0] # this will trigger an IndexError if there are no matching products
        selected_products.append(matching_product)
        # continue the while loop
        #
print(selected_products)
