# Reverse a string using Two Pointers

# The left pointer is placed at the beginning of the string and right pointer is placed at the end of the string
# Now, swap the character at left and right pointers, after that left pointer moves forward by 1 step and right pointer
# moves backward by 1 step
# This operation is continued till right pointer is ahead of the left pointer

def reverse_string_using_two_pointers(str):

    list_str = list(str)

    left = 0
    right = len(list_str) - 1

    while left < right:
        list_str[left], list_str[right] = list_str[right], list_str[left]
        left += 1
        right -= 1

    reversed_string = ''.join(list_str)
    return reversed_string

original_string = "Hello World!"
result = reverse_string_using_two_pointers(original_string)
print(result)

# op: !dlroW olleH

# TC: O(n),  in each iteration, the left pointer moves one step towards the center, and the right pointer moves one step
# backward.Therefore, the time complexity is proportional to the length of the string, making it O(n),
# where n is the length of the input string.

# SC: O(1), The algorithm uses a constant amount of extra space for the two pointers. Therefore, the space complexity is
# O(1), indicating constant space usage.




