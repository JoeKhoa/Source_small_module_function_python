"""
A Regular Expression (RegEx) is a sequence of characters that defines a search pattern
https://www.programiz.com/python-programming/regex
"""
import re

# print(re.__doc__)

pattern = '^a...s$'
test_Str = [ 'a123s', 'adz', 'a f']

for num,item in enumerate(test_Str):
    result = re.match(pattern,item)
    # if result:
    #     print(result)
    #     print("{0} is match {1}".format(item,pattern))
"""
    [] _ Square brackets ->a SET of characters you wish to match.
        [abc]:  	a, ac, abc de ca | FAIL: Hey Jude

    () _ Group  ->  group sub-patterns.
    (a|b|c)xz match any string that matches either a or b or c followed by xz
    (a|b|c)xz   :  abxz, abxz    |   FAIL:   ab xz

    + _ Plus   ->  one or more occurrences of the pattern left to it.
    ma+n	:  man, maaan, woman       | FAIL: mn,main

    $ _ Dollar  ->   ends with a certain character.
    a$	    :    a,formula             | FAIL:cab

    * _ Star    ->   zero or more occurrences of the pattern left to it.
    ma*n	:  mn, man, maaan, woman   |   FAIL:   main

    ^ _ Caret   ->     starts with a certain character.
        ^a	:    a,abc               |   FAIL : bac
        ^ab :   abc, abfsfs          | FAIL :acb

    + _ specify a RANGE of characters using _ inside square brackets.
        [a-e] is the same as [abcde].
        [1-4] is the same as [1234].
        [0-39] is the same as [01239].

    | _ Alternation ->  Vertical bar | is used for alternation (or operator).
    a|b		:  ade, man,       |   FAIL:   cde

******************************************************

    . _ Period  -> any single character (except newline '\n').
        ..	:  	ac, abc,abcdw        | FAIL: a



    {} _ Braces {n,m}. This means at least n, and at most m
    a{2,3}	:  abc daat, aabc daaat, aabc daaat	 | FAIL: abc dat

    ? _ Question Mark -> zero or one occurrence of the pattern left to
    ma?n	:  mn, man, woman  |   FAIL:   main, maaan

    ? _ Question Mark -> zero or one occurrence of the pattern left to
    ma?n	:  mn, man, woman  |   FAIL:   main, maaan



    \ _ Backslash -> scape various characters including all metacharacters.
    \$a match if a string contains $ followed by a.
     Here, $ is not interpreted by a RegEx engine in a special way.
     f you are unsure if a character has special meaning or not,
     you can put \ in front of it.
     This makes sure the character is not treated in a special way.





"""


import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

# result = re.findall(pattern, string)
# print(result)

# Output: ['12', '89', '34']



import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

# result = re.split(pattern, string)
# print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']


# import re
#
# string = 'Twelve:12 Eighty nine:89 Nine:9.'
# pattern = '\d+'
#
# # maxsplit = 1
# # split only at the first occurrence
# result = re.split(pattern, string, 2)
# print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']
# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']    #   2



# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12 de 23  f45 6'

# matches all whitespace characters
pattern = '\s+'
replace = ''

# newstring = re.sub(r'\s+',replace,string,3)
# print(newstring)

# 'abc 12de 23  f45 6'
# Output: 1
#  abc12 de 23  f45 6
# Output: 2
#  abc12de23  f45 6


# new_string = re.subn(pattern, replace, string)
# print(new_string)
#   ('abc12de23f456', 5)


string = "Python is fun"

# check if 'Python' is at the beginning
# match = re.search('\APython', string)
#
# if match:
#   print("pattern found inside the string")
# else:
#   print("pattern not found")

string = '39801 356, 2102 1111'

# Three digit number followed by space THAT followed by two digit number
pattern = '(\d{3}) (\d{2})' #   123 45
# Three digit number
pattern_2 = '(\d{2})(\d{2})'#   1234    # no-space

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
  print(match.group())
else:
  print("pattern not found")
# Output: 801 35

# print(match.group(1))
# print(match.group(2))
# print(match.group(1,2))

# (\d{3}) (\d{2})       # _group1_ _group2_
# 801 35
# 801
# 35
# ('801', '35')
# print(match.start())
# print(match.end())

print(match.re)
# print(match.string)


string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r.]', string)
print(result)
# ['\n', '\r', '.']
