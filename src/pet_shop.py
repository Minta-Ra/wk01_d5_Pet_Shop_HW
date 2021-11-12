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