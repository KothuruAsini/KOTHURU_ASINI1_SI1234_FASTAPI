from fastapi import FastAPI

app = FastAPI()

# Product List
products = [
    {"id":1,"name":"Wireless Mouse","price":599,"category":"Electronics","in_stock":True},
    {"id":2,"name":"Notebook","price":99,"category":"Stationery","in_stock":True},
    {"id":3,"name":"Pen Set","price":49,"category":"Stationery","in_stock":True},
    {"id":4,"name":"Desk Lamp","price":899,"category":"Electronics","in_stock":False},

    # Q1 Added products
    {"id":5,"name":"Laptop Stand","price":799,"category":"Electronics","in_stock":True},
    {"id":6,"name":"Mechanical Keyboard","price":2499,"category":"Electronics","in_stock":True},
    {"id":7,"name":"Webcam","price":1299,"category":"Electronics","in_stock":False}
]

# Show all products
@app.get("/products")
def get_products():
    return {
        "products":products,
        "total":len(products)
    }


# Q2 Category filter
@app.get("/products/category/{category_name}")
def get_by_category(category_name:str):

    filtered = [p for p in products if p["category"].lower() == category_name.lower()]

    if len(filtered) == 0:
        return {"error":"No products found in this category"}

    return {"products":filtered}


# Q3 In stock products
@app.get("/products/instock")
def instock_products():

    instock = [p for p in products if p["in_stock"]==True]

    return {
        "in_stock_products":instock,
        "count":len(instock)
    }


# Q4 Store summary
@app.get("/store/summary")
def store_summary():

    total = len(products)
    instock = len([p for p in products if p["in_stock"]])
    outstock = total - instock

    categories = list(set(p["category"] for p in products))

    return {
        "store_name":"My E-commerce Store",
        "total_products":total,
        "in_stock":instock,
        "out_of_stock":outstock,
        "categories":categories
    }


# Q5 Search products
@app.get("/products/search/{keyword}")
def search_products(keyword:str):

    result = [p for p in products if keyword.lower() in p["name"].lower()]

    if len(result)==0:
        return {"message":"No products matched your search"}

    return {
        "matched_products":result,
        "count":len(result)
    }


# BONUS Deals endpoint
@app.get("/products/deals")
def product_deals():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal":cheapest,
        "premium_pick":expensive
    }
