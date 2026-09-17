# Part B — Shopping List Manager

# Start with an empty list
shopping_list = []

# Use a loop to show a small menu repeatedly
while True:
    print("\n--- Shopping List Menu ---")
    choice = input("Choose an option (add / remove / show / done): ").strip().lower()
    
    if choice == "add":
        item = input("Enter the item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added to your list.")
        else:
            print("Item name cannot be empty.")
            
    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        # Check it is actually in the list with 'in' before removing
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your list.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("\nYour Current Shopping List:")
        if not shopping_list:
            print("  (Your list is empty)")
        else:
            for idx, item in enumerate(shopping_list, start=1):
                print(f"  {idx}. {item}")
                
    elif choice == "done":
        print("\nThank you for using the Shopping List Manager. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please choose from: add, remove, show, done.")