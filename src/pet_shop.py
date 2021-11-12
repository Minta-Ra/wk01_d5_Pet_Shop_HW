# Import Python debugger
import pdb # pdb.set_trace()

# WRITE YOUR FUNCTIONS HERE


# This function takes pet shop
def get_pet_shop_name(pet_shop):
    # return the name
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


# This function covers both, test_add_or_remove_cash__add and remove from pet_shop.py
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold


# Both functions return number of pets in the shop
def get_stock_count(pet_shop):
    num_of_pets = 0
    for pet in pet_shop["pets"]:
        num_of_pets += 1
    return num_of_pets
# OR:
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


##########################################################################
# This function covers both, test_all_pets_by_breed__found and not_found from pet_shop.py
def get_pets_by_breed(pet_shop, breed):
    # Empty list to store breeds
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)  
    return pets_by_breed


# This function covers both, test_find_pet_by_name__returns_pet and returns_None from pet_shop.py
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    # If pet name is not found
    return None


def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer_wallet):
    return customer_wallet["cash"]


def remove_customer_cash(customer_wallet, money_spent):
    customer_wallet["cash"] -= money_spent


def get_customer_pet_count(customer_pets):
    return len(customer_pets["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)