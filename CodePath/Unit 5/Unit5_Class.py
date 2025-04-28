class Dog:
    def __init__(self, name, breed, language='English'):
        self.name = name
        self.breed = breed
        self.language = language
    
    def bark(self):
        if self.language == "English":
            return "Woof"
        elif self.language == "Korean":
            return "Mong Mong"
        else:
            return "..."



fido = Dog('fido', 'lab', 'English')
mandoo = Dog("mandoo","jindo","Korean")
ladoo = Dog("ladoo", "Himalayan", "Hindi")

print(f"{fido.name} is a {fido.breed} and speaks {fido.bark()}")
print(f"{mandoo.name} is a {mandoo.breed} and speaks {mandoo.bark()}")
print(f"{ladoo.name} is a {ladoo.breed} and speaks {ladoo.bark()}")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
    
    def add(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def print(self):
        result = ''

        current = self.head

        while current:
            result += str(current.value)
            if current.next:
                result += ' -> '

            current = current.next

        print(result)

# dog_node1 = Node(f"{fido.name})

# print(f"{dog_node1.value}")

pet_list = LinkedList()
pet_list.add(f"{fido.name} says {fido.bark()}")
pet_list.add(f"{ladoo.name} says {ladoo.bark()}")
pet_list.add(f"{mandoo.name} says {mandoo.bark()}")

pet_list.print()

print(pet_list.tail.next)



