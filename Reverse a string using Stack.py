# Push all the elements into the stack
# pop the element from the stack and store it in the initial string, as stack works as last in first out approach
# so the string formed will be reversed of original string

def reverseByStack(str):
    stack = []
    for i in range(len(str)):
        stack.append(str[i])

    reversed_string = " "
    while stack:
        reversed_string += stack.pop()

    return reversed_string

original_string = "Hello World!"
result = reverseByStack(original_string)
print(result)

# op: !dlroW olleH

# TC : O(n)
# SC : O(n)

