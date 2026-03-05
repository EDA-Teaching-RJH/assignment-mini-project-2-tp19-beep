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

        choice = input("Choose an option between 1 and 8.").strip()
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
    if not collection:
        print("Your Collection is Empty.")
        return
    
    print("\nYour Collection:")
    for c in collection:
        print(
            f"{c['brand']} | {c['name']} | {c['year']} | "
            f"{c['rarity']} | ${c['price']:.2f} USD | ID: {c['number_id']}"
        )

def  add_collectible():
    print("\n---Add New Collectible---")
    brand = input("Enter Brand: ").strip()
    name = input("Enter Name: ")

    while True: 
        year_input = input("Enter Year: ").strip()
        if year_input.isdigit():
            year = int(year_input)
            break
        else:
            print("Invalid input. Please enter a valid year.")

    while True:
        price_input = input("Enter Price: ")
        price = price_input
        
    while True:
        rarity_input = input("Enter Rarity (Common/Uncommon/Rare/Very Rare/Ultra Rare): ")
        rarity = rarity_input.strip().title()
        if rarity in ["Common", "Uncommon", "Rare", "Very Rare", "Ultra Rare"]:
            break 
        else:
            print("Invalid input. Please enter a valid rating.")



def remove_collectible():
    print("Removing a Collectible...")

def search_collection():
    print("Searching Collection...")

def  update_collectible():
    print("Updating Collection...")

def count_collectibles():
    print("Counting Collectibles...")

def random_collectible():
    print("Choosing a random Collectible...")


if __name__ == "__main__":
    main()