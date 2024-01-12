# LeetCode 541. Reverse String II

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"

def reverseStr(s, k):
    # Initialize an empty string 'result' to store the final reversed string.
    result = ''
    # Iterate through the string with a step of 2k.
    for i in range(0, len(s), 2 * k):
        # Concatenate the reversed first k characters and the next k characters as specified.
        result += s[i:i+k][::-1] + s[i+k:i+2*k]
    # Return the final reversed string.
    return result

s1 = "abcdefg"
k1 = 2
output1 = reverseStr(s1, k1)
print(output1)  # Output: "bacdfeg"

# Example 1:
# Input string: "abcdefg", k: 2
# Output: Reverse the first 2 characters "ab", leave the next 2 characters "cd" unchanged,
# and reverse the next 2 characters "ef". Concatenate the results to get "bacdfeg".

# Example 2:
# Input string: "abcd", k: 2
# Output: Reverse the first 2 characters "ab" and leave the next 2 characters "cd" unchanged.
# Concatenate the results to get "bacd".
s2 = "abcd"
k2 = 2
output2 = reverseStr(s2, k2)
print(output2)  # Output: "bacd
