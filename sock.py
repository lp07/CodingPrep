
# Yellow -> 1, Blue -> 2, Red -> 3, Green -> 4, Orange -> 5
socks = [1, 2, 2, 1, 1, 3, 5, 1, 4, 4]
print(socks)

sock_pair = dict()
for s in socks:
    if s in sock_pair:
        sock_pair[s] += 1
    else:
        sock_pair[s] = 1

total_pair = 0
for value in sock_pair.values():
    total_pair += value // 2

print("Number of pairs:", total_pair)

# Idea: Yellow (1) sock * 4 times = 2 pairs
#       Blue (2) sock * 2 times = 1 pair
#       Red (3) sock *  1 time = 0 pair
#       Green (4) sock * 2 times = 1 pair
#       Orange (5) sock * 1 time = 0 pair
# Total pairs = 4


# Output: Number of pairs: 4


#if value % 2 == 1:
#print(key, value)
