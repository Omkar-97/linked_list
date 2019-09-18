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
            if temp.data == key:
                self.head = temp.next_node
                temp = None
                self.size -= 1
                return
            else:
                print("[{}] not found".format(key))
            while temp is not None:
                if temp.data == key:
                    print("[{}] deleted".format(key))
                    break
                else:
                    print("[{}] not found".format(key))
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
            print("[", curr.data, "]", end=" ")
            curr = curr.get_next_node()
        print()


def singly_list():

    choice = True
    my_list = LinkedList()
    print("Linked List operations")
    print("[a] Add\t[d] Delete\t[p] Print\t[s] Size")
    while choice:
        print("Enter operation code: ", end="")
        op = input()
        if op == "a" or op == "A":
            print("Enter new node: ", end=" ")
            new_node = input()
            my_list.add_node(new_node)
        if op == "d" or op == "D":
            if my_list.get_size() > 0:
                my_list.print_node()
                print("\nNode to be deleted?:", end=" ")
                node_del = input()
                my_list.del_node(node_del)
            else:
                print("List empty")
        if op == "p" or op == "P":
            if my_list.get_size() > 0:
                my_list.print_node()
            else:
                print("List empty")
        if op == "s" or op == "S":
            if my_list.get_size() > 0:
                print("List size: ", my_list.get_size())
            else:
                print("List empty")

        print("\nWant to continue [y/n]:", end=" ")
        val = input()
        if val == "y":
            print("[a] Add\t[d] Delete\t[p] Print\t[s] Size")
        if val != 'y':
            choice = False


if __name__ == '__main__':
    singly_list()
