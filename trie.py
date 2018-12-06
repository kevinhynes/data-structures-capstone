class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}  # TODO: Use HashMap
        self.is_word = False

    def get_child(self, letter):
        # Using .get will return None if key does not exist
        return self.children.get(letter)

    def list_children(self):
        print(list(self.children.keys()))

    def add_child(self, letter, new_node):
        self.children[letter] = new_node

    @property
    def has_children(self):
        return self.children != {}


class Trie:
    def __init__(self):
        self.root_node = TrieNode("")

    def insert(self, word):
        cur_node = self.root_node
        for letter in word:
            if cur_node.get_child(letter):
                cur_node = cur_node.get_child(letter)
            else:
                new_node = TrieNode(letter)
                cur_node.add_child(letter, new_node)
                cur_node = new_node
        cur_node.is_word = True

    def search(self, search_string):
        # Does the search string exist within the trie?
        cur_node = self.root_node
        for letter in search_string:
            if cur_node.get_child(letter):
                cur_node = cur_node.get_child(letter)
            else:
                return None
        search_matches = []
        return self._search(cur_node, search_string[:-1], search_matches)

    def _search(self, cur_node, word_so_far, search_matches):
        word_so_far += cur_node.letter
        if cur_node.is_word:
            search_matches.append(word_so_far)
        if cur_node.has_children:
            for child_node in cur_node.children.values():
                self._search(child_node, word_so_far, search_matches)
        return search_matches
