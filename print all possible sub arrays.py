# Generate all possible sub arrays using recursion

def generateSubarrays(arr, start, end):
    # Base case: stop if we have reached the end of the array
    if start > end or end >= len(arr):
        return

    # Print the subarray from index start to end
    print(arr[start:end + 1])

    # Increment the starting index and call the function recursively
    generateSubarrays(arr, start + 1, end)

    # Increment the ending index and call the function recursively
    generateSubarrays(arr, start, end + 1)

arr1 = [1, 2, 3]
arr2 = [1, 2]

print("Subarrays for arr1:")
generateSubarrays(arr1, 0, 0)

print("\nSubarrays for arr2:")
generateSubarrays(arr2, 0, 0)

