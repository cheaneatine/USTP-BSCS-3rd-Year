class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self):
        name = input("Enter the product name: ")
        quantity = int(input("Enter the product quantity: "))
        price = float(input("Enter the product price: "))
        item = InventoryItem(name, quantity, price)
        self.items.append(item)
        print(f"Added {quantity} of '{name}' at ${price:.2f} each.")

    def display_items(self):
        if not self.items:
            print("No items in inventory.")
            return
        
        print("\nInventory Items:")
        for item in self.items:
            print(f"Name: {item.name}, Quantity: {item.quantity}, Price: ₱{item.price:.2f}")

    def calculate_total_value(self):
        total_value = sum(item.total_value() for item in self.items)
        print(f"\nTotal inventory value: ${total_value:.2f}")


def main():
    inventory = Inventory()

    while True:
        print("\nInventory System Menu:")
        print("1. Add item")
        print("2. Display items")
        print("3. Calculate total inventory value")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            inventory.add_item()
        elif choice == '2':
            inventory.display_items()
        elif choice == '3':
            inventory.calculate_total_value()
        elif choice == '4':
            print("Exiting the inventory system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()