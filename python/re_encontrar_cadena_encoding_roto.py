import re

name1 = r"LUCERO SILVANA NOEM"
name2 = r"LUCERO SILVANA"
name3 = r"LUCERO"

expression = "^[A-Z ]*$"

print re.match(expression, name1)
print re.match(expression, name2)
print re.match(expression, name3)
