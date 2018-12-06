class Node:
    def __init__(self, key, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        # use LinkedList class to make next_node a Node object.
        self.next_node = next_node

    # if self.value is namedtuple, stringify fields & values
    def stringify_node(self):
        delimiter = "-" * 30
        node_as_string = '\n' + delimiter + '\n'
        fields = self.value._fields
        vals = list(self.value)
        zipped = zip(fields, vals)
        for item in zipped:
            if item[0] != 'cuisine':
                node_as_string += f"{item[0].capitalize()}: {item[1]}\n"
        node_as_string += delimiter + '\n'
        return node_as_string


class CuisineNode(Node):
    def __init__(self, key, value=None, next_node=None):
        super().__init__(key, value, next_node)
        self.value = HashMap_SC()


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def __iter__(self):
        cur_node = self.head_node
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.get_next_node()

    def insert_beginning(self, key, value=None):
        if self.head_node is None:
            self.head_node = Node(key, value)
        else:
            new_node = Node(key, value)
            new_node.set_next_node(self.head_node)
            self.head_node = new_node

    def search(self, key):
        cur_node = self.head_node
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node
            cur_node = cur_node.get_next_node()
        print("Your search returned no results.")
        return None

    def stringify_list(self):
        cur_node = self.head_node
        list_as_string = ""
        while cur_node:
            if type(cur_node.value) is not str:
                # cur_node.value is namedtuple here
                list_as_string += cur_node.stringify_node()
            else:
                list_as_string += cur_node.key + '\n'
            cur_node = cur_node.get_next_node()
        return list_as_string


class CuisineList(LinkedList):
    def __init__(self, head_node=None):
        super().__init__(head_node)

    def insert_beginning(self, new_node):
        if self.head_node is None:
            self.head_node = CuisineNode(new_node)
        else:
            new_node = CuisineNode(new_node)
            new_node.set_next_node(self.head_node)
            self.head_node = new_node


# HashMap_SC uses separate chaining of LinkedLists to resolve collisions
class HashMap_SC:
    def __init__(self, array_size=10):
        self.array_size = array_size
        self.array = [LinkedList() for x in range(array_size)]

    def _hash(self, key):
        hash_code = sum(key.encode())
        return hash_code

    def _compress(self, hash_code):
        array_index = hash_code % self.array_size
        return array_index

    def assign(self, key, value):
        array_index = self._compress(self._hash(key))
        list_at_index = self.array[array_index]  # LinkedList() instance
        # If LinkedList() is empty (no head_node), program never enters
        # this for loop.
        for node in list_at_index:
            if node.key == key:  # Overwrite existing
                node.value = value
                return
        list_at_index.insert_beginning(key, value)    # First-time assignment

    def retrieve(self, key):
        array_index = self._compressor(self._hash(key))
        list_at_index = self.array[array_index]
        for node_value in list_at_index:
            if node.key == key:
                return node.value  # Successful retrieval.
        return None  # Retrieving an un-assigned key

    def stringify_array(self):
        delimiter = "=" * 30
        array_as_string = delimiter
        for ll in self.array:
            if ll is not None:
                array_as_string += ll.stringify_list()
        array_as_string += delimiter
        return array_as_string
