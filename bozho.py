"""
Write a function my_function(M,i,j) that is given a list of lists M of numbers and two integer numbers i and j such that:

M represents a square matrix containing D x D elements: you can assume that all its sublists (corresponding to rows) have the same length and that the number D of rows equals the number D of columns.

Integer i is a row index: it is larger than or equal to 0, and strictly smaller than D.

Integer j is a column index: it is larger than or equal to 0, and strictly smaller than D.

Notice that D is not given as input. The function should modify M by replacing the i-th row with the j-th column and should then return the modified matrix.

For example:

Test
a = my_function([[1,2,3],[4,5,6],[7,8,9]],1,2)
print(a)
Result
[[1, 2, 3], [3, 6, 9], [7, 8, 9]]

"""

def my_function(M,i,j):
    list_replace = []
    for i_th in M:
        list_replace.append(i_th[j])
    M[i] = list_replace
    return M

a = my_function([[1,2,3],[4,5,6],[7,8,9]],1,2)
print(a)

#####

"""
You have a string a as input, along with two integer numbers s and e. Define a function my_function(a,s,e) that returns how many vowels are in the substring starting at position s and ending at position e (both included). Consider that the only vowels to consider are a, e, i, o, u. These should be considered both lowercase and uppercase.

For example:

Test	Result
# Test case 1 (Example)
a = "I study at Luiss"
s = 0
e = 15

b = my_function(a,s,e)

print(b)
# Expected output: 5
5
"""

def my_function(a, s, e):
    substring = a[s : e+1]
    counter = 0
    for i in substring:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            counter += 1
    return counter

a = "I study at Luiss"
s = 0
e = 15

b = my_function(a,s,e)

print(b)

#####

"""
Write a function my_function(L,i,j) that is given a list of lists of numbers L and two integer numbers i and j. L represents a matrix with R rows and C columns (R and C are not given as input). You can assume that all the R sublists have the same length C, with 0<=i<R and 0<=j<R.

The function shall return the sum of items in rows between row i and row j, or 0 if the matrix is empty or i > j.



Back-of-the-envelope example: my_function([[1,2,3,4],[10,20,30,40],[5,6,7,8]],1,2)) should return 10+20+30+40+5+6+7+8 = 126.

For example:

Test
a = my_function([[1,2,3,4],[10,20,30,40],[5,6,7,8]],1,2)
print(a)
Result
126
"""

def my_function(L,i,j):
    if (i > j) or (len(L) == 0):
        return 0
    sum_list = []
    for i_th in L[i : j+1]:
        sum_list.extend(i_th)
    return sum(sum_list)

a = my_function([[1,2,3,4],[10,20,30,40],[5,6,7,8]],1,2)
print(a)


# tralalalala

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

def my_function(M):
    if len(M) != len(M[0]):
        return -1
    
    summ = 0
    for row_i in range(len(M)):
        current_row = M[row_i]
        for col_i in range(len(current_row)):
            current_elem = current_row[col_i]
            if current_elem < 0:
                return -2
            if col_i >= row_i:
                summ += current_elem

    return summ

M = [[1,2,3], [4,5,6], [7,8,9]]
print(my_function(M))

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

def my_function(M):
    if len(M) == 0:
        return -1
    
    row_len = len(M[0])

    for row in M:
        if len(row) != row_len:
            return -2
        
    return [list(i) for i in zip(*M)]

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(my_function(M))

# mozhe bi po lesno shte rezberesh tova no e mn po trudno

def my_function(M):
    if len(M) == 0:
        return -1
    

    rows = len(M)
    cols = len(M[0])

    transposed = [[0] * rows] * cols

    for i in range(cols):
        temp_list = []
        for j in range(rows):
            value = M[j][i]
            temp_list.append(value)
        transposed[i] = temp_list
        
    return transposed

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(my_function(M))