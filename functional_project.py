import os
import json
import logging
import tomllib
from helper.exceptions import UsernameException, PasswordException
from typing import (
    List,
    Dict
)

from enum import IntEnum


# exit command
EXIT_COMMAND: List[str] = ['Quit', 'Q', 'Ex', 'Exit0']

# all goods
GOODS: List[str] = ['Apple', 'Cherry', 'Orange', 'Beef', 'Chicken', 'Lamb', 'Milk', 'Pasta', 'Rice']                                                # noqaE E501

# show items with numbers
NUMBERS_GOODS: Dict[str, int] = {'Apple': 100, 'Cherry': 100, 'Orange': 100, 'Beef': 100, 'Chicken': 100, 'Lamb': 100, 'Milk': 100, 'Pasta': 100, 'Rice': 100}  # noqaE E501


# show items with price
class Price(IntEnum):
    """ """
    Apple = 25
    Cherry = 50
    Orange = 30
    Beef = 200
    Chicken = 100
    Lamb = 300
    Milk = 15
    Pasta = 20
    Rice = 120


# Total purchase amount
PAYMENT: int = 0

# define the list
items: Dict = dict()


def get_details_of_user():
    """ get name & password for registering in website"""
    print("Please Provide")
    name = input("Name: ").casefold()
    if name == 'admin':
        raise UsernameException
    else:
        password = input("Password: ").casefold()
        if len(password) < 3:
            raise PasswordException
        else:
            with open(r'G:\django\project_02\helper\user_data.json') as myfile:
                info = json.load(myfile)
                for i in range(len(info)):
                    if name in info[i]:
                        print("Name Unavailable. Please Try Again")
                        break
                else:
                    with open(r'G:\django\project_02\helper\user_data.json', 'w') as myfile:                                                # noqaE E501
                        new_info = {name: password}
                        info.append(new_info)
                        json.dump(info, myfile)
                    print('your registration was successful!')
                    logging.basicConfig(level= logging.INFO, filename= 'app.log', filemode= 'a', format= '%(name)s - %(levelname)s - %(message)s')      # noqaE E501
                    logging.info(f'user: {name} registered.')


def show_stock() -> None:
    """Shows the inventory to the user"""
    print(f'we have {NUMBERS_GOODS} now')


def show_payment() -> None:
    """It shows the amount of payment required for the user at any moment"""
    print(f'you should pay {PAYMENT} until now')


def beautify_dict(shopping: Dict[str, int]) -> None:
    """
    Parameters
    ----------
    shopping: Dict[str : int] :
        Takes an entry in the form of a dictionary
    Returns
    -------
    the beautiful form for showing shopping list
    """
    for key, value in shopping.items():
        print(f'> {key} : {value}')


def add_item(shopping: Dict[str, int], item: str, numbers: int) -> Dict[str, int]:                                              # noqaE E501
    """

    Parameters
    ----------
    shopping_dict : dict : Takes an entry in the form of a dictionary
        
    item : str : take the item that they want to add to shopping list
        
    numbers : int : take the number of the item that
        
    Returns
    -------
    return dict that its items are str, int
    """
    shopping[item] = numbers
    return shopping


def remove_item(shopping: Dict[str, int], item: str) -> Dict[str, int]:
    """

    Parameters
    ----------
    shopping_dict : dict : Takes an entry in the form of a dictionary
        
    Returns
    -------
    return dict that its items are str, int
    """
    if item not in shopping:
        print('the item that you are trying remove is not in the list.')
    shopping.pop(item)
    return shopping


def search_item(shopping: Dict[str, int], item: str) -> None:
    """

    Parameters
    ----------
    shopping_dict : list : Takes an entry in the form of a dictionary

    Returns
    -------
    None
    """
    if item in GOODS:
        if item in shopping:
            print(f'{item} is in your list')
        else:
            print('the item that you are trying to find is not in the list.')
    else:
        print('the item that you are trying to find is not in our stock.')


def clear_screen():
    """clear the screen after any action"""
    return os.system('cls')


def edit(shopping: Dict[str, int], previous_item: str, new_item: str, number_of_new_item: int) -> Dict[str, int]:                            # noqaE E501
    """

    Parameters
    ----------
    shopping_dict : Takes an entry in the form of a dictionary
        
    previous_item : take the  previous item that they want to delete it
        
    new_item : take the  new item that they want to replace it
        
    Returns
    -------
    return dict that its items are str, int
    """
    if previous_item not in shopping:
        print('the item that you are trying edit is not in the list.')
    shopping.pop(previous_item)
    shopping[new_item] = number_of_new_item
    return shopping


def change_number(shopping: Dict[str, int], item: str, new_number: int) -> None:                                                                  # noqaE E501
    """

    Parameters
    ----------
    shopping_dict : Takes an entry in the form of a dictionary
        
    item : take the item that they want to change the number of it
        
    Returns
    -------
    None
    """
    shopping[item] = new_number


def sort_order(shopping: Dict[str, int]) -> None:
    """

    Parameters
    ----------
    shopping: Dict[str : takes dict that its items are str, int
        
    Returns
    -------
    None
    """
    new_sort = sorted(shopping.items(), key=lambda x: x[1])
    for i in new_sort:
        print(i[0], i[1])


def final(shopping: Dict[str, int]) -> None:
    """
    Parameters
    ----------
    shopping: Dict[str : int] : return dict that its items are str, int
        
    Returns
    -------
    None
    """
    print(shopping)


def read_log():
    """ it can read logs from config.toml"""
    with open("config.toml", "rb") as my_file:
        data = tomllib.load(my_file)
    return data


list_of_user = []

print("Please choose what would you like to do.")
try:
    # user choose 1 for register and choose 2 for login
    choice = int(input("For Signing Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
        #if user choose a1 get_details_of_user run for giving name & password from user                                                        # noqaE E501
        get_details_of_user()
    elif choice == 2:
        print("Please Provide")
        # input name for login
        name = input("Name: ").casefold()
        # load myfile for checking name of user
        with open(r'G:\django\project_02\helper\user_data.json') as myfile:
            info = json.load(myfile)
        for i in info:
            #check name of user with details of past users
            if name in i.keys():
                list_of_user.append('*')
                # take password from user
                password = input("Password: ").casefold()
                # checking name & password with past detail of users
                if {name: password} in info:
                    # show format of logging for login
                    logging.basicConfig(level= logging.INFO, filename= 'app.log', filemode= 'a', format= '%(name)s - %(levelname)s - %(message)s')     # noqaE E501
                    # logging for announce that one user login        
                    logging.info(f'user: {name} login.')
                    print("Welcome Back, " + name)
                    # show help for user
                    with open('G:\django\project_02\helper\help.txt') as myfile:                                                                   # noqaE E501
                        print(myfile.read())
                    #enter the budget of user
                    budget = int(input('Enter your budget: '))
                    while True:
                        # before every input show categories to help user
                        with open('G:\django\project_02\helper\category.txt') as myfile:                                                           # noqaE E501
                            print(myfile.read())
                        # give item for buying in small letter
                        item = input('enter the item to add to your list: ').title()                                                                              # noqaE E501
                        # clear the terminal screen
                        clear_screen()
                        # if user entered EXIT_COMMAND then exit the loop
                        if item in EXIT_COMMAND:
                            # after EXIT_COMMAND print the list
                            beautify_dict(items)
                            show_payment()
                            break
                        match item:
                            # see help command
                            case 'Help':
                                with open('G:\django\project_02\helper\help.txt') as myfile:                                                     # noqaE E501
                                    print(myfile.read())
                            # show the items that are in the list
                            case 'Category':
                                with open('G:\django\project_02\helper\category.txt') as myfile:                                                             # noqaE E501
                                    print(myfile.read())
                            # show the price of goods
                            case 'Price':
                                with open('G:\django\project_02\helper\price.txt') as myfile:                                                          # noqaE E501
                                    print(myfile.read())
                            # show the stock
                            case 'Stock':
                                show_stock()
                            # show the total payment
                            case 'Payment':
                                show_payment()
                                # show items that you buy until now
                            case 'Show':
                                beautify_dict(items)
                            # sort items that you buy until now
                            case 'Sort':
                                sort_order(items)
                            # remove the item from the list
                            case 'Remove':
                                item_to_remove = input('enter the item to remove: ').title()                                                        # noqaE E501
                                # checks the input item for remove is in the shopping list                                                             # noqaE E501
                                if item_to_remove in items:
                                    # if the input item is in the shopping list, remove it                                                        # noqaE E501
                                    NUMBERS_GOODS[item_to_remove] = 100
                                    PAYMENT -= Price[item_to_remove] * items[item_to_remove]                                                         # noqaE E501
                                    remove_item(items, item_to_remove)
                                else:
                                    # check the input item is  in the shopping list                                                              # noqaE E501
                                    print(f'you dont have {item_to_remove} in your shopping list')                                                    # noqaE E501
                            case 'Search':
                                # give the item for search
                                item_to_search = input('enter the item to search: ').title()                                                         # noqaE E501
                                # search for an item in the list
                                search_item(items, item_to_search)
                            case 'Edit':
                                # Takes the product, we want to change
                                previous_item = input('enter the item that you want to edit it: ').title()                                               # noqaE E501   
                                # It checks whether this amount is in the shopping list or not                                                  # noqaE E501
                                if previous_item in items:
                                    NUMBERS_GOODS[previous_item] = 100
                                    # He calculates the price of the product he wants to return                                                   # noqaE E501
                                    price_previous_item = items[previous_item] * Price[previous_item]                                                 # noqaE E501
                                    # Takes the value we want to replace
                                    new_item = input('enter the item that you want to replace: ').title()                                       # noqaE E501
                                    # Checks whether the new product is available in the store or not                                                 # noqaE E501
                                    if new_item in GOODS:
                                        # checks the new product is available in shopping list or not                                              # noqaE E501
                                        if new_item in items:
                                            # If the new product is in the shopping list, announce                                                  # noqaE E501
                                            print(f'{new_item} is already in your list!')                                                             # noqaE E501
                                        else:
                                            # it takes the desired number in the input                                                                    # noqaE E501
                                            number_new_item = \
                                            int(input(f'how many {new_item} do you want to add: '))                                                        # noqaE E501
                                            # calculate number of the new item in stock                                                                  # noqaE E501
                                            NUMBERS_GOODS = 100 - number_new_item                                                                       # noqaE E501
                                            # calculate the price of the new item                                                                   # noqaE E501
                                            price_new_item = number_new_item * Price[new_item]                                                        # noqaE E501
                                            # calculate the new budget
                                            PAYMENT = PAYMENT - price_previous_item + price_new_item                                                    # noqaE E501
                                            if PAYMENT > budget:
                                                # If the payment amount is more than the user's budget,                                                  # noqaE E501
                                                # it will announce the lack of budget                                                                      # noqaE E501
                                                print(f'You have {PAYMENT - budget} less money')                                                            # noqaE E501
                                                # The user chooses to increase the budget or not                                                            # noqaE E501
                                                choice = input('if you want increase your budget, enter "YES" or otherwise enter "NO": ')                     # noqaE E501
                                                choice = choice.upper()
                                                if choice == 'YES':
                                                    # Enter the budget that she wants to increase                                                    # noqaE E501
                                                    budget = int(input('Enter your budget: '))                                                              # noqaE E501
                                                    # The new product replaces the previous product                                                       # noqaE E501
                                                    edit(items, previous_item, new_item, number_new_item)                                               # noqaE E501
                                                else:
                                                    # they cannot change the product                                                                       # noqaE E501
                                                    print('you cant edit your goods!')                                                                       # noqaE E501
                                            # If the payment is enough, they can replace new product                                                          # noqaE E501
                                            else:
                                                edit(items, previous_item, new_item, number_new_item)                                                      # noqaE E501
                                    else:
                                        # the product that wants to replace is not in the store                                                             # noqaE E501
                                        print('we dont have that item you are trying to replace.')                                                             # noqaE E501
                                else:
                                    # if the previous product is not in the shopping list                                                                    # noqaE E501
                                    print(f'there is no {previous_item} in your list')                                                                       # noqaE E501
                            # change number of specific item
                            case 'Change_Number':
                                # Takes the name of the products that you want to change the number                                                         # noqaE E501
                                item_to_change = \
                                    input('enter the item that you want to chang its number: ').title()                                                      # noqaE E501
                                # takes the new number
                                number_to_change = \
                                    int(input(f'How many numbers of {item_to_change} do you want? '))                                                       # noqaE E501
                                NUMBERS_GOODS[item_to_change] = 100 - number_to_change                                                                            # noqaE E501
                                # chang the number of product
                                PAYMENT = PAYMENT - items[item_to_change] * Price[item_to_change] + number_to_change * Price[item_to_change]                    # noqaE E501
                                change_number(items, item_to_change, number_to_change)                                                                           # noqaE E501
                            case 'Final':
                                # get fiNAL list
                                final(items)
                            case _:
                                # check if item exists in shopping list
                                if item in items:
                                    print('item is already in your list.')
                                # check if item exists in store
                                elif item not in GOODS:
                                    # if the product is not in the store, announce it                                                                             # noqaE E501
                                    print(f'we dont have {item}')
                                else:
                                    # if the product exits in the store, ask the number                                                                          # noqaE E501
                                    try:
                                        number = int(input('enter num: '))
                                        # Checks the desired quantity is available in store                                                                        # noqaE E501
                                        if number <= NUMBERS_GOODS[item]:
                                            # Calculates a payment
                                            PAYMENT += (number * Price[item])
                                            # the payment is more than the budget or not                                                                         # noqaE E501
                                            if PAYMENT > budget:
                                                # it announce the lack of budget                                                                                  # noqaE E501
                                                print(f'You have {PAYMENT - budget} less money')                                                                  # noqaE E501
                                                # it asks if they wants to increase the budget or not                                                             # noqaE E501
                                                choice = input('if you want increase your budget, enter "YES" or if you want to continue enter "NO": ')            # noqaE E501
                                                choice = choice.upper()
                                                if choice == 'YES':
                                                    # Asks the amount of the budget increase                                                                      # noqaE E501
                                                    more_budget = int(input('Enter your budget: '))                                                                # noqaE E501
                                                    # calculate the new budget
                                                    budget += more_budget
                                                    # add the new item to the shopping list                                                                       # noqaE E501
                                                    add_item(items, item, number)                                                                                 # noqaE E501
                                                else:
                                                    # if user dont increase budget, calculate a payment                                                           # noqaE E501
                                                    PAYMENT -= (number * Price[item])                                                                             # noqaE E501
                                            else:
                                                # if the payment is enough, add it to shopping list                                                               # noqaE E501
                                                add_item(items, item, number)
                                                # It says the products that have been added to the list                                                           # noqaE E501
                                                print(f'{number} {item} add to your list')                                                                        # noqaE E501
                                                # It tells the number of products that have been purchased                                                        # noqaE E501
                                                print(f'there are {len(items)} type goods in your list')                                                          # noqaE E501
                                                # The number of products in stock is calculated                                                                   # noqaE E501
                                                NUMBERS_GOODS[item] -= number
                                                # It tells the number of products in stock                                                                        # noqaE E501
                                                show_payment()
                                                # It tells the amount paid by the user                                                                            # noqaE E501
                                                show_stock()
                                        # the requested product is more than the stock                                                                            # noqaE E501
                                        else:
                                            # show format of logging for finishing of product in stock                                                            # noqaE E501
                                            logging.basicConfig(level= logging.WARNING, filename= 'app.log', filemode= 'a', format= '%(name)s - %(levelname)s - %(message)s')    # noqaE E501
                                            logging.warning(f'{item} is out of stock!')                                                                           # noqaE E501
                                            # announce number of items that user want in stock
                                            print(f'{number} of {item} is out of stock! enter stock.')                                                            # noqaE E501
                                    # show except if the user dont enter the number for product                                                                   # noqaE E501
                                    except ValueError:
                                        print('Oops! that was no valid number. Try again')                                                                       # noqaE E501
                                    # show except for some error that we dont expect
                                    except Exception as e:
                                        logging.error(f'Weird error happened with message: {e}!, exc_info = True')                                               # noqaE E501
                else:
                    # Create a custom logger
                    logger = logging.getLogger(__name__)
                    # Create handlers
                    f_handler = logging.FileHandler('config.toml')
                    f_handler.setLevel(logging.WARNING)
                    # Create formatters and add it to handlers
                    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')                                                        # noqaE E501
                    f_handler.setFormatter(f_format)
                    # Add handlers to the logger
                    logger.addHandler(f_handler)
                    logger.warning('This is A WARNING. User enter the wrong password! ')                                                                        # noqaE E501
                    print('sth is wrong**!')
        if len(list_of_user) == 0:
            print('first you should sign up!')
# show except if user dont enter the number for login or register
except ValueError:
    print('Oops! Enter the number. Not string!')
# show except for some error that we dont expect
except Exception as e:
    logging.error(f'Weird error happened with message: {e}!, exc_info = True')
