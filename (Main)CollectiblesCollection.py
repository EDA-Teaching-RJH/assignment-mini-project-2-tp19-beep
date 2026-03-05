DATA_FILE = "collection.txt"
collection = []

def load_collection():
    global collection
    collection = []

    try:
        

def main():
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
            print("Exiting The Collector's Vault...")
            print("...")
            print("Goodbye!")
            break
        else:
            print("INVALID")
            print("Please select an option between 1 and 8")

def view_collection():
    print("Viewing Collection...")

def  add_collectible():
    print("Adding a new Collectible...")

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