"""
vaultlib.py

Library for the Collectors Vault application.

This contains validators, file handling, OOP, that is used by the main file CollectiblesCollection.py
"""

import re
DATA_FILE = "collection.txt"

class Collectible:
    """
    Base class reprsenting a collectible item.

    Stores information about the collectible.
    Property setters used to validate values when atributes are assigned.
    """

    def __init__(self, brand, name, year, price, rarity, number_id ):
        self.brand = brand
        self.name = name
        self.year = year 
        self.price = price
        self.rarity = rarity 
        self.number_id = number_id

    def __str__(self): 
        return (
            f"{self.brand} | {self.name} | {self.year} | "
            f"{self.rarity} | ${self.price:.2f} USD | ID: {self.number_id}"
        )

    @property
    def brand(self): 
        return self._brand

    @brand.setter
    def brand(self, value): 
        if not value: 
            raise ValueError("Brand Cannot be Empty.")
        self._brand = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value): 
        if not value: 
            raise ValueError("Name cannot be Empty.")
        self._name = value

    @property
    def year(self): 
        return self._year

    @year.setter
    def year(self, value): 
        if not valid_year(str(value)):
            raise ValueError("Year must be a 4-digit number.")
        self._year = int(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not valid_price(str(value)):
            raise ValueError("Price must be a valid number with up to 2 decimal places")
        self._price = float(value)

    @property 
    def rarity(self): 
        return self._rarity

    @rarity.setter
    def rarity(self, value): 
        if value not in ["Common", "Uncommon", "Rare", "Very Rare", "Ultra Rare"]:
            raise ValueError("Rarity must be one of: Common, Uncommon, Rare, Very Rare, Ultra Rare.")
        self._rarity = value
        
    @property
    def number_id(self): 
        return self._number_id
    
    @number_id.setter
    def number_id(self, value):
        if not valid_id(str(value)):
            raise ValueError("ID must be a 5-digit number.")
        self._number_id = value
            
class Doll(Collectible): 
    """"
    sublass of collectible representing a doll collectible.

    inherits attributes and validation from Collectible class.
    """

    def __init__(self, brand, name, year, price, rarity, number_id): 
        super().__init__(brand, name, year, price, rarity, number_id)

def valid_id(number_id):
    """
    Returns true if the ID consists of exactly 5 digits
    """

    if re.fullmatch(r"\d{5}", number_id):
        return True
    return False

def valid_price(price):
    """
    returns true if the price is a valid number with up to 2 decimal places
    """

    if re.fullmatch(r"\d+(\.\d{1,2})?", price):
        return True
    return False

def valid_year(year):
    """
    returns true if the year consists of exactly 4 digits.
    """

    if re.fullmatch(r"\d{4}", year):
        return True
    return False

def load_collection():
    """
    Load collectibles from the collection.txt file.

    Each line in the file is converted into a dictionary and returned as a list of collectibles.
    """
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

    return collection

def save_collection(collection):
    """
    saves current collection list to collection.txt file.

    Each collectible dictionary is written as a comma separated line in the file.
    """
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




