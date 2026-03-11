"""
CollectiblesCollection.py

Main application for the Collectors Vault system.

This program allowsn Collectors to manage their collectibles and toys from the 2000s to 2010s. 
Users can add, view, remove, search, update and request a random collectible within the system.
The items for the Vault are stored in a text file.

Features: 
- Viewing collectibles
- Adding new items
- Removing items
- Searching the collection
- Updating collectibles
- Random collectible selection

Uses:
- sys for command-line arguments
- random for random selection
- vaultlib for validation and file handling
"""

import sys # random lets us select a collectible at random
import random # random lets us select a collectible at random
from vaultlib import valid_id, valid_price, valid_year, load_collection, save_collection, Doll

collection = []


def main():
    """
    Main program loop.

    loads the collection from text file. 
    Optionally greets the use if a command line arguemnt is used.
    displays the main menu until user exits.
    """
    global collection  # Load saved collectibles from the text file
    collection = load_collection()

    # If the user passed a command-line argument, greet them by name
    if len(sys.argv) > 1:
        print(f"Hello, {sys.argv[1]}! Welcome to the Collectors Vault!")

    while True:
        print("\n!!Welcome to the Collectors Vault!!")
        print("A manager for collectibles and toys from the 2000s and 2010s!")
        print("LOADING...")
        print("...")

        print("\nPlease select an option: ")
        print("1. View Collection")
        print("2. Add Collectible")
        print("3. Remove Collectible")
        print("4. Search Collection")
        print("5. Update Collectible")
        print("6. Count Collectibles")
        print("7. Give me a random Collectible")
        print("8. Exit.")

        choice = input("Choose an option between 1 and 8: ").strip()
        if choice == '1': 
            view_collection()
        elif choice == '2':
            add_collectible()
        elif choice == '3':
            remove_collectible()
        elif choice == '4':
            search_collection()
        elif choice == '5':
            update_collectible()
        elif choice == '6': 
            count_collectibles()
        elif choice == '7':
            random_collectible()
        elif choice == '8':
            save_collection(collection)
            print("Exiting The Collector's Vault...")
            print("...")
            print("Goodbye!")
            print("Session Ended.")
            break
        else:
            print("INVALID")
            print("Please select an option between 1 and 8")



def view_collection():
    """
    Dsiplays all the Collectibles in the collection. 

    The collection is sorted by brand.
    Lambda Function.
    """
    print("Viewing collection...")
    if not collection:
        print("Your Collection is Empty.")
        return
    
    print("\n--- Your Collection ---")

    # Sort the collection by brand
    sorted_collection = sorted(collection, key=lambda item: item["brand"], reverse=True)

    for c in sorted_collection:
        print(
            f"{c['brand']} | {c['name']} | {c['year']} | "
            f"{c['rarity']} | ${c['price']:.2f} USD | ID: {c['number_id']}"
        )


def add_collectible():
    """
    Prompts the user to add details for a new collectible.

    The function validates the year, price and ID input from vaultlib.py.
    If the ID is unique, the collectible will be added to the text file.
    """

    print("\n---Add New Collectible---")
    brand = input("Enter Brand: ").strip()
    name = input("Enter Name: ").strip()

    while True: 
        year_input = input("Enter Year: ").strip()
        if valid_year(year_input):  # Keep asking until the user enters a valid 4-digit year
            year = int(year_input)
            break
        else:
            print("Invalid input. Please enter a valid year.") 

    while True:
        price_input = input("Enter Price: ").strip()
        if valid_price(price_input): # Keep asking until the user enters a valid price
            price = float(price_input)
            break 
        else:
            print("Invalid input. Please enter a Valid price")

    while True:
        rarity_input = input("Enter Rarity (Common/Uncommon/Rare/Very Rare/Ultra Rare): ")
        rarity = rarity_input.strip().title()
        if rarity in ["Common", "Uncommon", "Rare", "Very Rare", "Ultra Rare"]:
            break 
        else:
            print("Invalid input. Please enter a valid rating.")

    while True:
        number_id = input("Enter ID (5-digits): ").strip()
        
        if not valid_id(number_id): # Check whether the entered ID already exists in the collection
            print("Invalid input. Please enter a 5-digit numeric ID.")
            continue

        duplicate = False
        for item in collection:
            if item["number_id"] == number_id:
                duplicate = True
                break
        
        if duplicate:
            print("ID already exists. Please enter a unique ID.")
        else:
            break 

    new_doll = Doll(brand, name, year, price, rarity, number_id)
    collectible = {
        "brand": new_doll.brand,
        "name": new_doll.name, 
        "year": new_doll.year, 
        "price": new_doll.price, 
        "rarity": new_doll.rarity, 
        "number_id": new_doll.number_id
    }

    collection.append(collectible) # adds to collection
    save_collection(collection) # runs save_collection function in vaultlib.py and saves

    print("Collectible added successfully!")


def remove_collectible():

    """
    Removes a collectible from the collection.

    The user will enter the collectible id and the program will search for it.
    If the ID is a match the collectible is removed the collection text file is updated.
    """
    if not collection:
        print("Your Collection is empty")
        return

    target_id = input("Enter the collectible ID to remove: ").strip()    
    
    for item in collection:
        if item["number_id"] == target_id:
            collection.remove(item) # removes from collection
            save_collection(collection) # runs save_collection function in vaultlib.py and saves
            print("Collectible Removed Successfully!")
            return 
        
    print("Collectible with given ID not found.")


def search_collection():
    """
    Searches for Collectibles that match the users input.

    The search will check all fields: brand, name, year, price, rarity, ID.
    Any matching results will be displayed.
    """

    if not collection:
        print("Your Collection is empty")
        return

    print("\n---Search Collection---")
    query = input("Enter search term (brand, name, year, rarity OR ID): ").strip() 

    found = False

    for c in collection:
        if(
            query.lower() in c["brand"].lower() or
            query.lower() in c["name"].lower() or
            query.lower() in str(c["year"]) or
            query.lower() in c["rarity"].lower() or
            query in c["number_id"]
        ): 
            print(
            f"{c['brand']} | {c['name']} | {c['year']} | "
            f"{c['rarity']} | ${c['price']:.2f} USD | ID: {c['number_id']}"
            )
            found = True 

    if not found:
        print("No collectible matched your search.")


def update_collectible():
    """
    Updates the details of an existing collectible.

    The user enters the collectible ID and and select which field to update.
    if the input is valid the collection will be updated.
    """

    if not collection:
        print("Your Collection is empty")
        return

    target_id = input("Enter the collectible ID to update: ").strip()

    for item in collection: 
        if item["number_id"] == target_id:
            print("\nFound Collectible")
            print(
            f"{item['brand']} | {item['name']} | {item['year']} | "
            f"{item['rarity']} | ${item['price']:.2f} USD | ID: {item['number_id']}"
            )

            print("\nWhat would you like to update?: ")
            print("1. Brand")
            print("2. Name")
            print("3. Year")
            print("4. Rarity")
            print("5. Price")
            print("6. Cancel")

            choice = input("Choose an option from 1-6: ").strip()

            if choice == "1":
                item["brand"] = input("New Brand: ").strip()
            elif choice == "2":
                item["name"] = input("New Name: ").strip()
            elif choice == "3":
                while True:
                    year_input = input("New Year: ").strip()
                    if valid_year(year_input):  # runs valid_year in vaultlib.py to verify
                        item["year"] = int(year_input)
                        break 
                    print("Invalid year.")
            elif choice == "4":
                while True:
                    rarity_input = input("New Rarity (Common/Uncommon/Rare/Very Rare/Ultra Rare): ").strip().title()
                    if rarity_input in ["Common", "Uncommon", "Rare", "Very Rare", "Ultra Rare"]:
                        item["rarity"] = rarity_input
                        break 
                    print("Invalid rarity.")
            elif choice == "5":
                while True:
                    price_input = input("New Price: ").strip()
                    if valid_price(price_input): # runs valid_price in vaultlib.py to verify
                        item["price"] = float(price_input)
                        break 
                    print("Invalid price.")
            elif choice == "6": 
                print("Update cancelled.")
                return

            else: 
                print("Invalid option.")
                return

            save_collection(collection) # runs save_collection function in vaultlib.py and saves
            print("Collectible updated successfully!")
            return 

    print("Collectible with given ID not found.")


def count_collectibles():
    """
    Displays the curreny number of collectibles stored in the collection.
    """

    print("Counting Collectibles...")
    print(f"\nTotal Collectibles: {len(collection)}") # shows number of collectibles


def random_collectible():
    """
    Selects and displays a random collectible using a random function.
    """

    if not collection:
        print("Your Collection is empty")
        return

    # Choose a random item from the list
    c = random.choice(collection)
    print("\n---Random Collectible---")
    print("Choosing a random Collectible...")
    print(
        f"{c['brand']} | {c['name']} | {c['year']} | "
        f"{c['rarity']} | ${c['price']:.2f} USD | ID: {c['number_id']}"
    )

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()