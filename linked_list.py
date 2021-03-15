# Single node of a singly linked list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node

    def append_array_elements(self, array):
        for data in array:
            self.append(data)
                
    def insert(self, node_idx, data):
        if node_idx == 0:
            cached = self.head 
            self.head = Node(data, cached) 
        else:
            prev_node = self.head
            next_node = prev_node.next
            for i in range(node_idx - 1):
                prev_node = next_node
                next_node = next_node.next
                if next_node is None:
                    raise IndexError('Index out of range')

            prev_node.next = Node(data, next_node)

    def extract(self, node_number):
        pass

    def print_data(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        

if __name__ == '__main__':

    l1_data = [2, 4, 3]
    l1 = LinkedList()
    l1.append_array_elements(l1_data)

    l2_data = [7, 0, 8]
    l2 = LinkedList()
    l2.append_array_elements(l1_data)

    l1.insert(2, 9)
    l1.print_data()
