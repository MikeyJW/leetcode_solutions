# Problem 2. 
# Add two numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, list_):
        self.linked_list = iter(list_)
    
    @property    
    def next(self):
        try: 
            return next(self.linked_list)
        except:
            return None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return l1 + l2

if __name__ == '__main__':
    
    pass