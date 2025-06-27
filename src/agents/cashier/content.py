# Mock data for Cashier Agent
products_price = [
    {"product": "oven", "price": 299.99},
    {"product": "microwave", "price": 89.99},
    {"product": "toaster", "price": 24.99},
    {"product": "blender", "price": 49.99}
]

# Response template
Product_REdirect = [
    {"setup": "oven", "who": "user", "response": "the price for oven is {{price}}!"},
    {"setup": "microwave", "who": "user", "response": "the price for microwave is {{price}}!"},
    {"setup": "toaster", "who": "user", "response": "the price for toaster is {{price}}!"},
    {"setup": "blender", "who": "user", "response": "the price for blender is {{price}}!"}
]
