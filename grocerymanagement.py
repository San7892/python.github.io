class GroceryStore:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def update_quantity(self, item_name, new_quantity):
        if item_name in self.inventory:
            self.inventory[item_name] = new_quantity
        else:
            print(f"{item_name} not found in inventory.")

    def view_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"{item_name} removed from inventory.")
        else:
            print(f"{item_name} not found in inventory.")

def main():
    store = GroceryStore()

    while True:
        print("\nOptions:")
        print("1. Add new item to inventory")
        print("2. Update item quantity")
        print("3. View current inventory")
        print("4. Remove item from inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            store.add_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Enter item name: ")
            new_quantity = int(input("Enter new quantity: "))
            store.update_quantity(item_name, new_quantity)
        elif choice == '3':
            store.view_inventory()
        elif choice == '4':
            item_name = input("Enter item name to remove: ")
            store.remove_item(item_name)
        elif choice == '5':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
