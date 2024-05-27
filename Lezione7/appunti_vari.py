'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

An input string is valid if: 

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

For example:
Test 	Result

print(is_valid_parenthesis("()"))

	

True

print(is_valid_parenthesis("(]"))

	

False'''





from collections import Counter


l=[1,2,3,4]
c=Counter(l)

for i in enumerate(l):
    print(i)

for i in c:
    print (i)














