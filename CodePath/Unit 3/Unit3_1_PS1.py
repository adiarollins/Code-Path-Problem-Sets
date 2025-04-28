'''Problem 1
def is_valid_post_format(posts):
    dict = {')':'(', '}':'{', ']':'['}
    stack = []
    for p in posts:
        if p in dict.values():
            stack.append(p)
        elif p in dict.keys():    
            if not stack or stack.pop() != dict[p]:
                return False
        #print (stack)
    
    return not stack

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
Problem 2
def reverse_comments_queue(comments):
    stack = []
    reverse_list = []

    for i in comments:
        stack.append(i)
    
    for i in range(len(stack)):
        reverse_list.append(stack.pop())
    
    return reverse_list


print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
Problem 3

def is_symmetrical_title(title):
    title_stripped = title.strip(" ").lower()
    point1 = 0
    point2 = len(title_stripped) -1
    while point1 < point2:
        if title_stripped[point1].isalpha() and title_stripped[point2].isalpha():
            if title_stripped[point1] == title_stripped[point2]:
                point1 += 1
                point2 -= 1
            else:
                return False
        elif title_stripped[point1].isalpha() == False:
            point1 += 1
        elif title_stripped[point2].isalpha() == False:
            point2 -= 1
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
Problem 4
def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    print(squared_engagements)
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
Problem 5
def clean_post(post):
    post_list = list(post)
    point1 = 0
    point2 = 1

    while point2 < len(post_list):
        if post_list[point1].lower() == post_list[point2].lower():
            if post_list[point1].islower() and post_list[point2].isupper():
                del post_list[point2]
                del post_list[point1]
                point1 = 0
                point2 = 1
            elif post_list[point2].islower() and post_list[point1].isupper():
                del post_list[point2]
                del post_list[point1]
                point1 = 0
                point2 = 1
            else:
                point1 += 1
                point2 += 1
        else:
            point1 += 1
            point2 += 1
    return "".join(post_list)
                

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
Problem 5
def clean_post(post):
    post_list = list(post)
    stack = []
    x = 0
    while x < len(post_list):
        if len(stack) < 2:
            stack.append(post_list[x])
            x += 1
        if stack[len(stack) - 1].lower() == stack[len(stack) - 2].lower():
            if stack[len(stack)-1].islower() and stack[len(stack) - 2].isupper():
                del stack[len(stack)-1]
                del stack[len(stack)-1]
            elif stack[len(stack)-1].isupper() and stack[len(stack) - 2].islower():
                del stack[len(stack)-1]
                del stack[len(stack)-1]
        else:
            stack.append(post_list[x])
            x += 1
    return stack


print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
'''