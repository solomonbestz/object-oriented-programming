class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def connect_nodes(self):
        self.next_node = self.next_node

if __name__=='__main__':
    pass