# data structures-capstone

The purpose of this project was to implement data structures in python for a small 'toy' restaurant search application.

#### Inputs: 
1. List of cuisine types: \
`cuisines = ['chinese', thai', 'german,' ...]`

2. List of restaurant data including cuisine type, name, price, rating and address: \
`restaurant_data = [['chinese', "Mr.Wong's", '3', '3', '123 Fake St'], ...]`

#### Output:
1. User enters search string, app outputs list of cuisine types matching string: \
search: `'c'`		results: `['chinese', 'czech', 'cafe']`

2. If only one cuisine type found, print all restaurant info of that type to terminal: \
search: `'chin'`	results: `'chinese'`  ---->  print all chinese restaurant info

#### Data Structures Used:
1. Trie Tree
    * Comprised of all `cuisines`. Validates and suggests user search.
  
2a. Nodes & Linked Lists
    * Linked list used to organize restaurants by cuisine. This `CuisineList` is made of `CuisineNode`s.
    * `CuisineNode.key` holds `cuisine_type`, a string.
    * `CuisineNode.value` holds a hashmap of all restaurants of `cuisine_type`.
2b. HashMap with separate chaining for collision resolution
    * HashMap's array modeled with Python built-in list.
    * Each array holds instance of a Linked list, allowing nodes to be added if a collision occurs. This `LinkedList` is made of `Node`s.
    * `Node.key` holds restaurant's name, a string.
    * `Node.value` holds restaurant data in `r`, an instance of collections.namedtuple.

#### Analysis
1. Search Runtime
    * Trie tree is optimal for this use-case. If only one search result is found, runtime is O(1). In general, runtime is proportional to number of search results. For a small trie with only a few branches runtime can be considered constant.
2. Restaurant Retrieval Runtime
    * Retrieval runtime here is O(n + m) where n = number of cuisines, m = number of restaurants in `HashMap`.
    
#### Discussion
1. Trie Tree - good 'nuff
    * If `cuisines` contained many more `cuisine_types` then this algorithm could be improved with BurstSort.  It is fine as-is given limited input.

2. Overall Data Structure - could be improved
    * No need to search through a linked list of `CuisineNode`s to access the correct hashmap.  Once the `cuisine_type` is validated from user input, a hashmap should be used with `cuisine_type` as a key.
    * For the requirements of this *simple* application, there is no need to store the restaurant data in a hashmap.  It might be slightly faster to use a linked list instead, as there may be unused locations in the hashmap's array that will get searched and waste time.
    * Considering a *real life* application, it makes sense to store the restaurant data in a hashmap so that a user can directly look up restaurant information if they know the name (and another trie tree could be used to suggest names).  This is why I went this route, though this functionality is not implemented.
    * Similarly, storing the restaurant data in a namedtuple created additional work in printing the output for this simple app, but I believe the use of the namedtuple would be appropriate for a more robust application.

3. File Organization
   * All data structure classes are in the same file, which feels sloppy.  I ran into a circular logic problem with import statements that I didn't feel like figuring out.  Partially due to using class inheritance.
