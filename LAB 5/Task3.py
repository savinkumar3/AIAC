# Python program to recommend products based on user history

# Sample product database with categories and usefulness
products = [
    {"name": "Laptop", "category": "Electronics", "useful": True},
    {"name": "Smartphone", "category": "Electronics", "useful": True},
    {"name": "Headphones", "category": "Electronics", "useful": True},
    {"name": "Blender", "category": "Home Appliances", "useful": True},
    {"name": "Vacuum Cleaner", "category": "Home Appliances", "useful": True},
    {"name": "Novel", "category": "Books", "useful": True},
    {"name": "Comics", "category": "Books", "useful": False},
    {"name": "Gaming Console", "category": "Electronics", "useful": False},
    {"name": "Socks", "category": "Clothing", "useful": True},
    {"name": "T-shirt", "category": "Clothing", "useful": True},
    {"name": "Action Figure", "category": "Toys", "useful": False},
    {"name": "Cookbook", "category": "Books", "useful": True},
]

# Function to get user history input
def get_user_history():
    print("Enter your purchase/view history (comma separated, e.g., Laptop, Novel, Socks):")
    user_input = input()
    # Split input by comma and strip whitespace
    history = [item.strip() for item in user_input.split(",") if item.strip()]
    return history

# Function to find categories from user history
def get_categories_from_history(history):
    categories = set()
    for item in history:
        for product in products:
            if product["name"].lower() == item.lower():
                categories.add(product["category"])
    return categories

# Function to recommend useful products based on categories
def recommend_products(categories, history):
    recommendations = []
    history_lower = [h.lower() for h in history]
    for product in products:
        # Recommend only useful products, not already in user's history, and in the same category
        if (product["useful"] and 
            product["category"] in categories and 
            product["name"].lower() not in history_lower):
            recommendations.append(product["name"])
    return recommendations

# Main program
if __name__ == "__main__":
    # Get user history
    user_history = get_user_history()
    # Find categories from user history
    user_categories = get_categories_from_history(user_history)
    # Recommend products
    recommended = recommend_products(user_categories, user_history)
    # Display recommendations
    if recommended:
        print("\nBased on your history, we recommend these useful products:")
        for prod in recommended:
            print(f"- {prod}")
    else:
        print("\nNo new useful product recommendations found based on your history.")
