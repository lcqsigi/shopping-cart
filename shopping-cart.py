import pandas as pd
import datetime

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

products_url="https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv"

#    id                                               name                          aisle       department  price
#     1                         Chocolate Sandwich Cookies                  cookies cakes           snacks   3.50
#     2                                   All-Seasons Salt              spices seasonings           pantry   4.99

df=pd.read_csv(products_url)
print(df.head(20))

valid_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

selected_products = [] 

while True:
    selected_id = input("Please input a product id, or 'DONE': " )

    if selected_id.upper() == "DONE":
        break 

    if str(selected_id) ==str(0):
        print("Invalid option try only numbers [1-20]")

    if selected_id not in str(valid_options):
        print("Invalid option try only numbers [1-20]")

    if selected_id in str(valid_options) and int(selected_id) > 0:
        print("LOOKING UP PRODUCT", selected_id)
        for x in range(0,len(df),1):
            if str(selected_id) == str(df["id"][x]):
                matching_product = str(df["name"][x])
        selected_products.append(matching_product)

print("-----Roel's Store-----")
print("-----404 421 2365-----")

print(f"CHECKOUT: {datetime.datetime.now().strftime('%m/%d/%y %I:%M %p')}") 

print("-----Thank you!!!-----")
print(selected_products)
