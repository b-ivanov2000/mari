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

#####

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


#####

Write a function my_function(L,i,j) that is given a list of lists of numbers L and two integer numbers i and j. L represents a matrix with R rows and C columns (R and C are not given as input). You can assume that all the R sublists have the same length C, with 0<=i<R and 0<=j<R.

The function shall return the sum of items in rows between row i and row j, or 0 if the matrix is empty or i > j.



Back-of-the-envelope example: my_function([[1,2,3,4],[10,20,30,40],[5,6,7,8]],1,2)) should return 10+20+30+40+5+6+7+8 = 126.

For example:

Test
a = my_function([[1,2,3,4],[10,20,30,40],[5,6,7,8]],1,2)
print(a)
Result
126


# tralalalala
# solution for 1:
def my_function(M,i,j):
    # Save j-th column in column_jth
    column_jth = []
    for row_index in range(len(M)):
        for column_index in range(len(M[row_index])):
            if column_index == j:
                column_jth.append(M[row_index][column_index])
    M[i] = column_jth
    return M

#proba

### exercises

