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
                    raise IndexError('Index out of range, use append '
                                     'or try new value')
            prev_node.next = Node(data, next_node)

    def extract(self, node_idx):
        curr_node = self.head
        if node_idx == 0:
            return curr_node.data
        else:
            for i in range(node_idx):
                curr_node = curr_node.next
                if curr_node == None:
                    raise IndexError('Index out of range')
            return curr_node.data

    def print_data(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Init some stuff
        n_l1 = l1
        n_l2 = l2
        carry = 0
        out = LinkedList()

        while n_l1 or n_l2 or carry == 1:
            
            # Extract values from list nodes if applicable
            if n_l1:
                l1_val = n_l1.data
            else:
                l1_val = 0
            if n_l2:
                l2_val = n_l2.data
            else:
                l2_val = 0

            # Sum values
            sum_ = carry + l1_val + l2_val
            
            # Extract carry
            carry = 0
            if sum_ >= 10:
                sum_ -= 10
                carry = 1
            
            out.append(sum_) 

            # Move on to next value in linked lists
            if n_l1:
                n_l1 = n_l1.next
            else:
                n_l1 = None
            
            if n_l2:
                n_l2 = n_l2.next
            else:
                n_l2 = None

        return out


if __name__ == '__main__':

    # Init example linked lists
    ll1_data = [2, 4, 3]
    ll1 = LinkedList()
    ll1.append_array_elements(ll1_data)
    l1 = ll1.head

    ll2_data = [5, 6, 4]
    ll2 = LinkedList()
    ll2.append_array_elements(ll2_data)
    l2 = ll2.head

    sol = Solution().addTwoNumbers(l1, l2)
    
    sol.print_data()
