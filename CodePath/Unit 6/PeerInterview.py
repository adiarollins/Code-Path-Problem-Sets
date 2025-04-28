'''
U: Fuction return middle node of a linked list
 - if it is a even number for nodes im returning the second middle node
M: Singly linked List
P: Create a linked list
pointer - to find how many nodes are in the linked list
dif pointer - find the middle node and return it.
'''

class SinglyLinkedListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = SinglyLinkedListNode(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

# def findMiddleNode(LL_head):
#     currentlen = 0
#     current1 = LL_head
#     current2 = LL_head

#     while current1 != None:
#         currentlen += 1

#         if current1.next == None:
#             continue
          
#         current1 = current1.next

def findMiddleNode(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    if fast.next:
        return slow.next
    else:
        return slow
    
example1 = SinglyLinkedListNode(1)

example2 = SinglyLinkedListNode(2)

example3 = SinglyLinkedListNode(3)

example4 = SinglyLinkedListNode(1)

    

