# пробни

Write a recursive function my_function(L, K) that, given a list L of numbers and a number K strictly larger than 0, returns a new list obtained by decreasing every element of L by K. If L is empty, the function should return an empty list.



Back-of-the-envelope example: my_function([2,12,3,7], 2) should return [0, 10, 1, 5]

For example:

Test	Result
a = my_function([2,12,3,7], 2)
print(a)
[0, 10, 1, 5]


def my_function(L, K):
    if len(L) == 0:
        return []
    else:
        x = L[0] - K
        x = [x]

        return x + my_function(L[1:], K)

Write a recursive function my_function(S) that, given a lower-case string S, returns the list containing all vowels in S. Each vowel should appear in the output list as many times and in the same order in which it appears in S. If the string is empty or there are no vowels in S, the function should return an empty list.



Back-of-the-envelope example: my_function("luiss learn is the best") should return ['u', 'i', 'e' , 'a', 'i', 'e', 'e' ]

For example:

Test	Result
a = my_function("luiss learn is the best")
print(a)
['u', 'i', 'e', 'a', 'i', 'e', 'e']


def my_function(S):
    if S == '':
        return []
    v = "aeiou"
    if S[0] in v:
        return [S[0]] + my_function(S[1:])
    else:
        return [] + my_function(S[1:])

a = my_function("luiss learn is the best")
print(a)

Write a recusive function my_function(s) that, given a string s composed by 0's and 1's representing a binary number, converts the binary number into base 10. You can assume the string to be non-empty.

For example:

Test	Result
print(my_function("1010"))
10

def my_function(s):
    if s == "":
        return 0
    bit = int(s[0])
    return bit*(2**len(s)-1 + my_function(s[1:]))