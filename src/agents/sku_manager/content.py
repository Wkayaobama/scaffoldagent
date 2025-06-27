# Mock data for SKU Manager
products_stock = [
    {"product": "oven", "quantity": 12},
    {"product": "microwave", "quantity": 7},
    {"product": "toaster", "quantity": 15},
    {"product": "blender", "quantity": 9}
]

# Response template
Product_stock_inquiry = [
    {"setup": "oven", "who": "user", "response": "the quantity for oven is {{quantity}}!"},
    {"setup": "microwave", "who": "user", "response": "the quantity for microwave is {{quantity}}!"},
    {"setup": "toaster", "who": "user", "response": "the quantity for toaster is {{quantity}}!"},
    {"setup": "blender", "who": "user", "response": "the quantity for blender is {{quantity}}!"}
]
