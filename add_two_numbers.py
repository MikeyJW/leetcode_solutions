# Problem 2. 
# Add two numbers

# Definition for singly-linked list.
class LinkedList:
    def __init__(self, list_=None):
        if type(list_) == list:
            self.linked_list = iter(list_)
        else:
            pass
    
    @property
    def next(self):
        try: 
            return next(self.linked_list)
        except:
            return None

    @next.setter
    def next(self, val):
        # Evaluate linked_list attr
        temp_list = list(self.linked_list)
        # Append val
        temp_list.append(val)
        # Chuck back linked_list iter
        self.linked_list = iter(temp_list)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Init some stuff
        n_l1 = l1.next
        n_l2 = l2.next
        carry = 0
        output = LinkedList()

        while (n_l1 or n_l2) or carry == 1:
            sum_ = carry + n_l1 + n_l2

            # Extract carry
            if sum_ >= 10:
                sum_ =- 10
                carry = 1

            output.next = sum_

        return output




if __name__ == '__main__':
    
    l1 = LinkedList([2, 4, 3])
    l2 = LinkedList([5, 6, 4])
    
    sol = Solution().addTwoNumbers(l1, l2)
    print(sol)
