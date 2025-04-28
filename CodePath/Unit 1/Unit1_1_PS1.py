''' Problem 1
def welcome():
print("Welcome to The Hundred Acre Wood!")

welcome()
'''
''' Problem 2
def greeting(name):
	print(f"Welcome to the Hundred Acre Wood {name}! My name is Christopher Robin")
greeting("Michael")
greeting("Winnie the Pooh")
'''
''' Problem 3
def print_catchphrase(character):
	if(character == "Pooh"):
		print("Oh bother!")
	elif(character == "Tigger"):
		print("TTFN: Ta-ta for now!")
	elif(character == "Eeyore"):
		print("Thanks for noticing me.")
	elif(character == "Christopher Robin"):
		print("Silly old bear")
	else:
		print(f"Sorry! I don't know {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)
'''
''' Problem 4
def get_item(items, x):
	if x < 0 or x > len(items) - 1:
		print("None")
	else:
	    print(items[x])

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)
'''
''' Problem 5
def sum_honey(hunny_jars):
	sum = 0
	for i in hunny_jars:
		sum += i
	print(sum)


hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)
'''
''' Problem 6
def doubled(hunny_jars):
	for i in range(len(hunny_jars)) :
		hunny_jars[i] = hunny_jars[i]*2
	print (hunny_jars)


hunny_jars = [1, 2, 3]
doubled(hunny_jars)
'''
''' Problem 7
def count_less_than(race_times, threshold):
	players = 0
	for i in race_times:
		if (i < threshold):
			players += 1
	print (players)

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)
'''
''' Problem 8
def print_todo_list(task):
	print("Pooh's To Do:")
	for i in range(len(task)):
		print(f"{i}. {task[i]}")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
'''  
''' Problem 9
def can_pair(item_quantities):
	even = True
	for i in item_quantities:
		if (i%2 != 0):
			even = False
	print(even)

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)
'''
'''Problem 10
def split_haycorns(quantity):
	divisors = []
	k = 0
	for i in range(quantity):
		if (quantity%(i+1) == 0):
			divisors.append(i+1)
			k += 1
	print(divisors)


quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)
'''
'''Problem 11
def triggerfy(s):
	result = ""
	for i in s:
		if i.lower() not in "tiger":
			result += i
	print (result)


s = "suspicerous"
triggerfy(s)

s = "Trigger"
triggerfy(s)

s = "Hunny"
triggerfy(s)
'''
'''Problem 12'''
def locate_thistles(items):
	list = []
	for x in range(len(items)):
		if items[x] == "thistle":
			list.append(x)
	print(list)


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)