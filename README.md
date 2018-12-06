# data structures-capstone

###### The purpose of this project was to implement data structures in python for a small 'toy' restaurant search application.

#### Inputs: 
1. list of cuisine types:
		`['chinese', thai', 'german,' ...]`
2. list of restaurant data including cuisine type, name, price, rating and address:
		`[['chinese', "Mr.Wong's", '3', '3', '123 Fake St'], ...]`

#### Output:
1. user enters search string, app outputs list of cuisine types matching string
		search: `'c'`		results: `['chinese', 'czech', 'cafe']`
2. if only one cuisine type found, print all restaurant info of that type to terminal
		search: `'chin'`	results: `'chinese'`  ---->  print all chinese restaurant info

#### Data Structures Used:
1. Trie Tree
2. Nodes & Linked Lists
3. HashMap with Separate Chaining for collision resolution
4. collections.namedtuple 

