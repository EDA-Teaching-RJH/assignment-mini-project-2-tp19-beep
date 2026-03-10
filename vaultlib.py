import re

class Collectible:
    def __init__(self, brand, name, year, price, rarity, number_id ):

        if not brand:
            raise ValueError("Brand cannot be empty")
        if not name: 
            raise ValueError("Name cannot be empty")
        if not year: 
            raise ValueError("Year must be a 4-digit number.")
        if not price: 
            raise ValueError("Price must be a valid number with up to 2 decimal places")
        if not rarity: 
            raise ValueError("Rarity must be one of: Common, Uncommon, Rare, Very Rare, Ultra Rare.")
        if not number_id: 
            raise ValueError("ID must be a 5-digit number.")

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

        
            

def valid_id(number_id):
    if re.fullmatch(r"\d{5}", number_id):
        return True
    return False

def valid_price(price):
    if re.fullmatch(r"\d+(\.\d{1,2})?", price):
        return True
    return False

def valid_year(year):
    if re.fullmatch(r"\d{4}", year):
        return True
    return False

