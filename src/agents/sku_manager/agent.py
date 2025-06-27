"""
SKU Manager Agent implementation
"""
from swarm import Agent

# Sample data for SKU Manager
products_stock = [
    {"product": "oven", "quantity": 12},
    {"product": "microwave", "quantity": 7},
    {"product": "toaster", "quantity": 15},
    {"product": "blender", "quantity": 9}
]

Product_stock_inquiry = [
    {"setup": "oven", "who": "user", "response": "the quantity for oven is {{quantity}}!"},
    {"setup": "microwave", "who": "user", "response": "the quantity for microwave is {{quantity}}!"},
    {"setup": "toaster", "who": "user", "response": "the quantity for toaster is {{quantity}}!"},
    {"setup": "blender", "who": "user", "response": "the quantity for blender is {{quantity}}!"}
]

from ...lookup import lookup_by_key
import re

def stock_inquiry(user_input: str = ""):
    # Try to extract product name from user input
    product_names = [item["product"] for item in products_stock]
    found = None
    for name in product_names:
        if re.search(rf"\\b{name}\\b", user_input, re.IGNORECASE):
            found = name
            break
    if not found:
        return "Sorry, I couldn't find that product."
    quantity = next((item["quantity"] for item in products_stock if item["product"] == found), "Unknown")
    template = next((t["response"] for t in Product_stock_inquiry if t["setup"] == found), "No template found.")
    return template.replace("{{quantity}}", str(quantity))

def create_sku_manager_agent():
    return Agent(
        name="SKU Manager Agent",
        instructions="Handles product stock inquiries. Call stock_inquiry(user_input) with the user's message.",
        functions=[stock_inquiry]
    )
