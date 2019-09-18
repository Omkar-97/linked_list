class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, val):
        self.next_node = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add_node(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def del_node(self, key):
        temp = self.head
        if temp is not None:
            if temp is not None:
                if temp.data == key:
                    self.head = temp.next_node
                    temp = None
                    self.size -= 1
                    return
            while temp is not None:
                if temp.data == key:
                    print("Deleting [{}]".format(key))
                    break
                prev = temp
                temp = temp.next_node
            if temp is None:
                return "Not found"
            prev.next_node = temp.next_node
            self.size -= 1

    def get_size(self):
        return self.size

    def print_node(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.get_next_node()
        print()


def singly_list():

    choice = True
    my_list = LinkedList()
    for i in range(ord("A"), ord("Z") + 1):
        my_list.add_node(chr(i))
    my_list.print_node()
    print("Initial size: ", my_list.get_size())

    while choice:
        print("Node to be deleted?:", end=" ")
        node_del = input()
        my_list.del_node(node_del)
        my_list.print_node()
        print("Updated size: ", my_list.get_size())
        print("\nWant to continue [y/n]:", end=" ")
        val = input()
        if val != 'y':
            choice = False


if __name__ == '__main__':
    singly_list()
