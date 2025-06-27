"""
Cashier Agent implementation
"""
from swarm import Agent

# Sample data for Cashier Agent
products_price = [
    {"product": "oven", "price": 299.99},
    {"product": "microwave", "price": 89.99},
    {"product": "toaster", "price": 24.99},
    {"product": "blender", "price": 49.99}
]

Product_REdirect = [
    {"setup": "oven", "who": "user", "response": "the price for oven is {{price}}!"},
    {"setup": "microwave", "who": "user", "response": "the price for microwave is {{price}}!"},
    {"setup": "toaster", "who": "user", "response": "the price for toaster is {{price}}!"},
    {"setup": "blender", "who": "user", "response": "the price for blender is {{price}}!"}
]

from ...lookup import lookup_by_key
import re

def product_redirect(user_input: str = ""):
    # Try to extract product name from user input
    product_names = [item["product"] for item in products_price]
    found = None
    for name in product_names:
        if re.search(rf"\\b{name}\\b", user_input, re.IGNORECASE):
            found = name
            break
    if not found:
        return "Sorry, I couldn't find that product."
    price = next((item["price"] for item in products_price if item["product"] == found), "Unknown")
    template = next((t["response"] for t in Product_REdirect if t["setup"] == found), "No template found.")
    return template.replace("{{price}}", str(price))

def create_cashier_agent():
    return Agent(
        name="Cashier Agent",
        instructions="Helps direct customers to the best product and provides pricing. Call product_redirect(user_input) with the user's message.",
        functions=[product_redirect]
    )
