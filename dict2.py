products = [
    {"p_name":"Apple Iphone 11","brand":"Apple","Category":"Mobile","price":98000},
    {"p_name":"Redmi Note 6","brand":"Xiaomi","Category":"Mobile","price":15000},
    {"p_name":"Sports Shoes","brand":"Puma","Category":"Shoes","price":3400},
    {"p_name":"JBL Headphones bluetooth","brand":"JBL","Category":"Headphones","price":1200},
    {"p_name":"Leather Jacket","brand":"Zara","Category":"Clothes","price":4500},
    {"p_name":"Puma Shoes","brand":"Puma","Category":"Shoes","price":2070},
    {"p_name":"Adidas Sports Shoes","brand":"Adidas","Category":"Shoes","price":1900},
    {"p_name":"Macbook Pro","brand":"Apple","Category":"Laptop","price":128000},
    {"p_name":"Lenovo thinkpad","brand":"Lenovo","Category":"Laptop","price":78000},
    {"p_name":"Asus Zenbook","brand":"Asus","Category":"Laptop","price":88000},
    ]
'''
    - user can enter product name, product brand or category
    - now store the data in a different list (searchResults = [])
    - ask user if he wants to sort data based on price
    - ask the order of sorting
'''
toSearch = input("Search Here : ")
toSearch = toSearch.lower()

searchResults = []

for product in products:
    if toSearch in product["p_name"].lower() or toSearch in product["brand"].lower() or toSearch in product["Category"].lower():
        searchResults.append(product)

if len(searchResults) == 0:
    print("No products found matching your search term.")
else:
    print("Search Results:")
    for product in searchResults:
        print("- " + product["p_name"] + " (" + product["brand"] + ", " + product["Category"] + ") - Rs. " + str(product["price"]))

    sortResults = input("Do you want to sort the results by price? (yes/no): ")

    if sortResults.lower() == "yes":
        sortOrder = input("Do you want to sort in ascending or descending order? (asc/desc): ")
        
        searchResults = sorted(searchResults, key=lambda x: x["price"], reverse=(sortOrder.lower() == "desc"))

        print("Sorted Search Results:")
        for product in searchResults:
            print("- " + product["p_name"] + " (" + product["brand"] + ", " + product["Category"] + ") - Rs. " + str(product["price"]))