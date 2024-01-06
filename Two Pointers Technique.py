""" Two Pointer Technique to find a pair in the array whose sum equals the target.

- arr (list) -> The input array
- target (int) -> The target sum.

Returns:
tuple or None: A tuple containing the pair of indices whose elements sum up to the target.
Returns None if no such pair is found.
"""

def two_pointers(arr, target_sum):
    # sort the array in ascending order
    arr.sort()

    # Initialize two pointers at the beginning of the array and end of the array
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            # Found a pair with the required sum
            return left, right
        elif current_sum < target_sum:
            # If the sum is smaller, move the left pointer to the right
            left += 1
        else:
            # If the sum is greater, move the right pointer to the left
            right -= 1
    # No pair found
    return None

arr = [1, 2, 3, 5, 8, 10]
target_sum = 13
result = two_pointers(arr, target_sum)
print(result)
