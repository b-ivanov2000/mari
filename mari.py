# Write a function my_function(L) that, given a list of numbers L, returns a new list containing the same numbers without duplicates.
# Numbers in the output list should be sorted from the smallest to the largest.
#
# For example:
#
# Test
# print(my_function([10,2,3,5,2,10,3]))
# Result
# [2, 3, 5, 10]

def my_function(L):
    result = []
    for num in L:
        if num not in result:
            result.append(num)
    result.sort()   # яка функция
    return result

##################
# Write a function my_function(L) that is given a list L of numbers representing distances in kilometers. The function should return the sum of the distances converted to miles, where 1 kilometer corresponds to 0.62 miles. If there are no items in the list, the function should return 0.
#
# For example:
#
# Test
# a = my_function([3,2,4])
# print(a)
#Result
# 5.58

# сама я реших
def my_function(L):
    if len(L)==0:
        return 0
    return sum(L)*0.62

# Write a function my_function(L1, L2), that takes as parameters two lists:
#
# each element in list L1 is the name of a person;
# each element in list L2 is a character (i.e., string of length 1).
# The function shall return a list L3 containing persons whose name begins with a letter in L2. Elements in L3 should appear in the same order in which they appear in L1.
# If L1 is empty or does not contain persons whose name begins with a letter in L2, then L3 must be an empty list.
#
# For example:
#
# Test
# a = my_function(["Giorgio", "Irene", "Antonio", "Giuseppe"], ["I", "G"])
# print(a)
#Result
# ['Giorgio', 'Irene', 'Giuseppe']

def my_function(L1, L2):
    L3 = []
    for name in L1:
        if name[0] in L2:
            L3.append(name)
    return L3

# Let M be an n×m
#  matrix of numbers organized as a list-of-lists with n
#  lists where each inner list has length m
# . You can assume that all inner lists have the same size m
#  and you can assume M to be non-empty.
#
# Write a Python function called my_function(M) that, given a matrix M, returns the sum of its upper triangular part.
#
# Keep in mind the following caveats and definitions:
#
# the upper triangular of a matrix is defined as the portion of the matrix composed by only elements lying above (and including) the main diagonal
#
# normally, triangular matrices are special cases of square matrices (namely matrices whose number of rows is equal to the number of columns): if n
#  is not equal to m
# , the function must return -1
#
# if the matrix is a square matrix but there is at least one negative element (regardless of its position), the function must return -2
#
# For example:
#
# Test	Result
# M = [[1,2,3], [4,5,6], [7,8,9]]
# print(my_function(M))
# 26

solution

# Let M be an n×m
#  matrix of numbers organized as a list-of-lists with n
#  lists where each inner list has length m
# . Write a function called my_function(M) that takes as input a matrix M and returns its transpose.
#
# Keep in mind the following caveats and definitions:
#
# if the input matrix is empty, the function must return -1
#
# the input list-of-lists must indeed be a valid matrix where all rows have the same length m
# : if this does not hold, the function must return -2
#
# the transpose of an n×m
#  matrix is a new m×n
#  matrix where the item in position (i,j)
#  of the original matrix lies in position (j,i)
#  in the transposed matrix
#
# For example:
#
# Test	Result
# M = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# print(my_function(M))
# [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]

solution

# Write a function my_function(M,i) that is given a list of lists of numbers M and an integer number i such that:
#
# M represents a square matrix containing D x D elements: you can assume that all its sublists (corresponding to rows) have the same length and that the number D of rows equals the number D of columns.
#
# Integer i is a row and column index: it is larger than or equal to 0, and strictly smaller than D.
#
# Notice that D is not given as input. The function should modify M by replacing the i-th column with the i-th row and should then return the modified matrix.
#
#
#
# Back-of-the-envelope example: if M = [[1,2,3],[4,5,6],[7,8,9]] and i=1, the returned modified matrix should be [[1,4,3],[4,5,6],[7,6,9]].
#
# For example:
#
# Test	Result
# a = my_function([[1,2,3],[4,5,6],[7,8,9]],1)
# print(a)
# [[1, 4, 3], [4, 5, 6], [7, 6, 9]]

def my_function(M, i):
    for row_index in range(len(M)):
        M[row_index][i] = M[i][row_index]
    return M