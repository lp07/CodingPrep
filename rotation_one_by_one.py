""" Here we are consider left rotation
    At each iteration, shift the elements by one position to the left circularly
    (i.e., first element becomes the last)
    Perform this operation d times to rotate the elements to the left by d position
    """
"""
Let us take arr[] = [1, 2, 3, 4, 5, 6], d = 2

First Step:
        => Rotate to left by one position
        => arr[] = {2, 3, 4, 5, 6, 1}
Second Step:
        => Rotate again to left by one position
        => arr[] = {3, 4, 5, 6, 1, 2}
Rotation is done 2 times
So the array becomes arr[] = {3, 4, 5, 6, 1, 2}

Below are the steps to solve using the above approach:

Rotate the array to left by one position. For that do the following:

Store the first element of the array in a temporary variable
Shift the rest of the elements in the original array by one place
Update the last index of the array with the temporary variable
Repeat the above steps for the number of left rotations required

"""

def OneOneOneLeftRotation(arr, d):
    n = len(arr)
    # Take the remainder to handle cases where d is greater than the array length
    d = d % n
    # Rotate the array using slicing
    # arr[2:] + arr[:2] -> [3, 4, 5] + [1, 2]
    rotated_array = arr[d:] + arr[:d]
    return rotated_array

original_array = [1, 2, 3, 4, 5]
rotation_count = 2
rotated_array = OneOneOneLeftRotation(original_array, rotation_count)
print(rotated_array)

# op: [3, 4, 5, 1, 2]




