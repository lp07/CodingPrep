class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to store the frequency of each character in the string s.
        char_map = {}

        for char in s:  # Loop through the string s to add the data in char_freq.
            if char not in char_map:  # If the character is not in the char_map, add it with a value of 1.
                char_map[char] = 1
            else:  # If the character is already in the char_map, increment its value by 1.
                char_map[char] += 1

        for i in range(len(s)):  # Loop through the string s again to find the first unique character.
            if char_map[
                s[i]] == 1:  # if the frequency of the character at index i is 1, it is the first unique character.
                return i  # Return the index of the first unique character.
        return -1  # If no unique character is found, return -1.
