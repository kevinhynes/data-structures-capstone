from trie import Trie
from data_structures import *
from data import cuisines, restaurant_data
import welcome
from collections import namedtuple


def build_trie(word_list):
    for cuisine in cuisines:
        t.insert(cuisine)


def test_trie(word_list):
    for item in word_list:
        search_string = item[0][0]  # first letter of cuisine type
        search_results = t.search(search_string)
        print("Searching for '{}': \t Found: {}"
              .format(search_string, search_results))


def build_ll(word_list):
    new_linked_list = CuisineList()
    for word in word_list:
        new_linked_list.insert_beginning(word)
    return new_linked_list


def print_restaurant_names(restaurant_list):
    for r in restaurant_list:
        print(r[1])


Restaurant = namedtuple("Restaurant_nt",
                        ['cuisine', 'name', 'price', 'rating', 'address'])


def build_data_structure(cuisine_list, restaurant_list):
    cuisine_ll = build_ll(cuisine_list)
    # TODO create build_hashmaps function
    for r in restaurant_list:
        new_restaurant = Restaurant(*r)
        cuisine_node = cuisine_ll.search(new_restaurant.cuisine)
        cuisine_node.value.assign(new_restaurant.name, new_restaurant)
    return cuisine_ll


def list_by_cuisine(cuisine_type, data_structure):
    cuisine_node = data_structure.search(cuisine_type)
    print(cuisine_node.value.stringify_array())


t = Trie()
build_trie(cuisines)

data_structure = build_data_structure(cuisines, restaurant_data)

welcome.print_welcome()
opening_message = "\nWhat type of food would you like to eat?" \
                  "\nType the beginning of that food type and press enter" \
                  "to see if it's here.\n"

while True:
    user_input = input(opening_message)
    search_results = t.search(user_input)
    if search_results is None:
        print("\nSorry, we don't have that cuisine available!")
    elif len(search_results) > 1:
        print("\nYour search returned these results: {}".format(search_results))
    elif len(search_results) == 1:
        match = search_results[0]
        print(f"\nThe only cuisine with those beginnging letters is {match.capitalize()}")
        user_input = input(f"\nWould you like to see {match.capitalize()} restaurants? Enter 'y' for yes"
                               " and 'n' for no.")
        if user_input == 'y':
            list_by_cuisine(match, data_structure)
        elif user_input == 'n':
            print(f"\nThank you, Good bye!")
            break
        else:
            print(f"\nThat is not a valid choice.")


