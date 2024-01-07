# You should write a function that will receive a positive integer and return: "Fizz"
# if the number is divisible by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").

# example
# Input: An integer (int).
# Output: A string (str).

# Examples:
# assert checkio(15) == "Fizz"
# assert checkio(6) == "Fizz"
# assert checkio(10) == "10"
# assert checkio(7) == "7"

def Checkio(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    else:
        return str(num)
    return ""

print("Example:")
print(Checkio(3))

# These "asserts" are used for self-checking
assert Checkio(15) == "Fizz"
assert Checkio(6) == "Fizz"
assert Checkio(10) == "10"
assert Checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
