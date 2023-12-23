# 1st method:
a = 'clcoding'
a1 = a.replace('cl', '')
print(a1)
# op: coding

# 2nd method:
b = 'clcoding'
b1 = b[0:2] # from include 0 to 2, (includes 0th but not 2nd)
print(b1)
# op: cl

# 3rd method:
c = 'clcoding'
c1 = c.partition('cl')[2]
# Using the partition() method to split the string into three parts based on the first occurrence of 'cl'
# The first part is everything before 'cl', the second part is 'cl' itself, and the third part is everything after 'cl'
# The [2] index is used to get the third part, which is everything after 'cl'
c1 = c.partition('cl')[2]
print(c1)
# op: coding

# 4th method:
import re
d = 'clcoding'
d1 = re.sub(r'cl','',d)
# Using the re.sub() function to substitute 'cl' with an empty string in the original string
# The pattern 'cl' is matched and replaced with an empty string ('')
print(d1)
# op: coding

# 5th method:
e = 'clcoding'
e1 = e.strip('cl') # strinp(), to remove any leading and white spaces
print(e1)
# op: oding







