import re

word = "# Query_time: 11.495009 bla bla"


match = re.match(r"# \S* (\d*.\d*)", word)

if match:
    print match.groups()[0]


print "Replace"
print re.sub("(\d*\.\d*)", "new \\1", word)
