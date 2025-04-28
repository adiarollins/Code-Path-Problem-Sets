class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def findMiddle(head):
    slow = fast = head

    while fast:
        fast = fast.next.next
        slow = slow.next