import math
'''Problem 1
def reverse_sentence(sentence):
    split = sentence.split()
    pointer1 = 0
    pointer2 = len(split) - 1
    for i in range(math.floor(len(split)/2)):
        x = split[pointer1]
        split[pointer1] = split[pointer2]
        split[pointer2] = x
        pointer1 += 1
        pointer2 -= 1
    print(' '.join(split))


sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)
'''
'''Problem 2'''
def goldilocks_approved(nums):
    min = nums [0]
    max = nums[0]
    result = -1
    for i in nums:
        if (i > max):
            max = i
        if (i < min):
            min = i
    for i in nums:
        if (i != max and i != min):
            result = i
            break

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)