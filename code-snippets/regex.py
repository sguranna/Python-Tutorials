string1='hello 12 hi 89. Howdy 34'
string2='Twelve 12 Eighty nine uhrqohi 74 kgsag89.'
string3='Twelve:12 Eighty nine:89 Nine:9.'
string4='abc 12\n de 23 \n f45 6'
string5="Python is fun"
string6='39801 356, 2102 1111'
string = "bhdgs afhss abhds"

import re
# result=re.match("a(\w+)", string)
# print(result)
# res = re.search("a(\w+)", string)
# print(res)
# res1 = re.findall("a(\w+)", string)
# print(res1)

# split the string based on condition - re.split()
a=re.sub("\d+", "HI",string2)
print(a)

