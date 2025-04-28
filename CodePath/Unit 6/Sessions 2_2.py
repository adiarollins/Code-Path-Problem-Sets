# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


# def trail_length(trailhead):
#     cur = trailhead
#     count = 1
#     while cur.next != trailhead:
#         count+=1
#         cur = cur.next
    
#     return count


# marker1 = Node("Marker 1")
# marker2 = Node("Marker 2")
# marker3 = Node("Marker 3")
# marker1.next = marker2
# marker2.next = marker3
# marker3.next = marker1

# print(trail_length(marker1))


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing - careful this will cause an infinite loop when used on a list w/cycles
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def clear_trail(trailhead):
#     current = trailhead
#     visited = []
#     while current and current.next != None:
#         if current.next.value in visited:
#             current.next = None
#         else:
#             visited.append(current.value)
#             current = current.next
#     return trailhead


# # 1 -> 2 -> 3 -> 4 -> -> 2  


# marker1 = Node("Trailhead")
# marker2 = Node("Trail Fork")
# marker3 = Node("The Falls")
# marker4 = Node("Peak")
# marker1.next = marker2
# marker2.next = marker3
# marker3.next = marker4
# marker4.next = marker2

# print_linked_list(clear_trail(marker1))\

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def remove_duplicate_markers(trailhead):
#     curr = trailhead 
#     visited = [] 
#     while curr.next.next != None: 
#         if curr.next.next.value in visited:
#             curr.next = curr.next.next.next
#         else: 
#             visited.append(curr.next.next.value) 
#             curr = curr.next
#     return trailhead 
# #vi = [2]
# #    1 -> 2 -> 3 -> 3 -> 4
# #p1  ^   
# #p2       ^ ----------->
# trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))
# print_linked_list(remove_duplicate_markers(trailhead))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def selective_trail_clearing(trailhead, m, n):
    cur = trailhead
    while cur:
        for i in range(m):
            if cur and cur.next:
                cur = cur.next
            else:
                return trailhead
            
            skip = cur
            for i in range(n):
                if skip and skip.next:
                    skip = skip.next
            
            

trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))

print_linked_list(selective_trail_clearing(trailhead, 2, 3))