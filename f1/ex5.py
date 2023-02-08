import re
s = "1h 50m"
s1 = "1h"
s2 = "40m"

p = "(\d+)(h) (\d+)(m)"
result = re.search(p, s)
print(result.group())
print(result.group(1))
result = re.search(p, s)
print(result.group(1))
print(result.group(2))

