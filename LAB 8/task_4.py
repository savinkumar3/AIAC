class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name, quantity=1):
        if name in self.items:
            if self.items[name]['quantity'] > quantity:
                self.items[name]['quantity'] -= quantity
            else:
                del self.items[name]
        else:
            print(f"Item '{name}' not found in cart.")

    def total_cost(self):
        return sum(info['price'] * info['quantity'] for info in self.items.values())

def main():
    cart = ShoppingCart()
    while True:
        print("\nOptions: add, remove, total, quit")
        choice = input("Enter your choice: ").strip().lower()
        if choice == 'add':
            name = input("Item name: ")
            price = float(input("Item price: "))
            quantity = int(input("Quantity: "))
            cart.add_item(name, price, quantity)
            print(f"Added {quantity} x {name} to cart.")
        elif choice == 'remove':
            name = input("Item name to remove: ")
            quantity = int(input("Quantity to remove: "))
            cart.remove_item(name, quantity)
        elif choice == 'total':
            print(f"Total cost: ${cart.total_cost():.2f}")
        elif choice == 'quit':
            print("Exiting. Final total: ${:.2f}".format(cart.total_cost()))
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()