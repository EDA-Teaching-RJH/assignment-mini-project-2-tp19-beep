import re

class Collectible:
    def __init__(self, brand, name, year, price, rarity, number_id ):
        self.brand = brand
        self.name = name
        self.year = year 
        self.price = price
        self.rarity = rarity 
        self.number_id = number_id
            

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

