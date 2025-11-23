# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if not item:
        print("No item entered. Nothing was added.")
        return
    shopping_list.append(item)
    print(f"Added: '{item}'")

def remove_item(shopping_list):
    if not shopping_list:
        print("The shopping list is empty. Nothing to remove.")
        return
    item_to_remove = input("Enter item to remove: ").strip()
    if not item_to_remove:
        print("No item entered. Nothing was removed.")
        return

    # Find first case-insensitive match and remove it
    for i, existing in enumerate(shopping_list):
        if existing.lower() == item_to_remove.lower():
            removed = shopping_list.pop(i)
            print(f"Removed: '{removed}'")
            return

    print(f"Item '{item_to_remove}' not found in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty.")
        return
    print("\nCurrent shopping list:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
