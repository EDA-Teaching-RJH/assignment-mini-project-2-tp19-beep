import random 
from validators import valid_id, valid_price, valid_year
DATA_FILE = "collection.txt"
collection = []

def load_collection():
    global collection
    collection = []

    try:
        with open(DATA_FILE, "r") as f:
            for line in f: 
                line = line.strip()
                if line == "":
                    continue

                brand, name, year, price, rarity, number_id = line.split(",")

                collectible = {
                    "brand": brand,
                    "name": name,
                    "year": int(year),
                    "price": float(price),
                    "rarity": rarity, 
                    "number_id": number_id
                }
                collection.append(collectible)

    except FileNotFoundError:
        collection = []



def save_collection():
    with open(DATA_FILE, "w") as f:
        for collectible in collection:
            line = (
                f"{collectible['brand']},"
                f"{collectible['name']},"
                f"{collectible['year']},"
                f"{collectible['price']},"
                f"{collectible['rarity']},"
                f"{collectible['number_id']}\n"
            )
            f.write(line)




def main():
    load_collection()
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
            save_collection()
            print("Exiting The Collector's Vault...")
            print("...")
            print("Goodbye!")
            break
        else:
            print("INVALID")
            print("Please select an option between 1 and 8")




def view_collection():
    print("Viewing collection...")
    if not collection:
        print("Your Collection is Empty.")
        return
    
    print("\nYour Collection:")
    for c in collection:
        print(
            f"{c['brand']} | {c['name']} | {c['year']} | "
            f"{c['rarity']} | ${c['price']:.2f} USD | ID: {c['number_id']}"
        )




def add_collectible():
    print("\n---Add New Collectible---")
    brand = input("Enter Brand: ").strip()
    name = input("Enter Name: ").strip()

    while True: 
        year_input = input("Enter Year: ").strip()
        if valid_year(year_input):  
            year = int(year_input)
            break
        else:
            print("Invalid input. Please enter a valid year.")

    while True:
        price_input = input("Enter Price: ").strip()
        if valid_price(price_input):
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
        
        if not valid_id(number_id):
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

    collectible = {
        "brand": brand,
        "name": name, 
        "year": year, 
        "price": price, 
        "rarity": rarity, 
        "number_id": number_id
    }

    collection.append(collectible)
    save_collection()

    print("Collectible added successfully!")




def remove_collectible():
    if not collection:
        print("Your Collection is empty")
        return

    target_id = input("Enter the collectible ID to remove: ").strip()    
    
    for item in collection:
        if item["number_id"] == target_id:
            collection.remove(item)
            save_collection()
            print("Collectible Removed Successfully!")
            return 
        
    print("Collectible with given ID not found.")




def search_collection():
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
        print(f"No Collectible found.")




def update_collectible():
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
                    if valid_year(year_input):
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
                    if valid_price(price_input):
                        item["price"] = float(price_input)
                        break 
                    print("Invalid price.")
            elif choice == "6": 
                print("Update cancelled.")
                return

            else: 
                print("Invalid option.")
                return

            save_collection()
            print("Collectible updated successfully!")
            return 

    print("Collectible with given ID not found.")




def count_collectibles():
    print("Counting Collectibles...")
    print(f"\nTotal Collectibles: {len(collection)}")




def random_collectible():
    if not collection:
        print("Your Collection is empty")
        return

    c = random.choice(collection)
    print("\n---Random Collectible---")
    print("Choosing a random Collectible...")
    print(
        f"{c['brand']} | {c['name']} | {c['year']} | "
            f"{c['rarity']} | ${c['price']:.2f} USD | ID: {c['number_id']}"
    )


if __name__ == "__main__":
    main()