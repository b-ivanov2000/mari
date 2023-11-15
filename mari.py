Which of the following statements about dictionaries in Python is true?

Select one:
a. Dictionaries are ordered collections of elements.
b. Dictionaries can only store values of the same data type.
c. Dictionaries are mutable and can be modified after creation.
d. Dictionaries cannot be nested inside other dictionaries.

There are two main methods to remove items from a list: remove() and pop(). Which of the following statements are true?

Select one or more:
a. lst.remove(v) deletes all occurrences of v in the list lst
b. lst.remove(v) yields an error if v is not in lst
c. pop() by default removes the last item of the list
d. pop() returns the index of the item being removed

Which of the following claims are true?
Select one or more:
a. After the two Python statements first = [] and second = [], second is an alias of first
b. After the two Python statements first = [] and second = first, second is an alias of first
c. After the execution of the Python statement first = [], the statements second = [] and second = first will produce the same references in memory
d. While using new_list = my_list, any modifications to new_list will also change my_list
e. After the statement new_list = my_list, new_list is a clone of my_list

At DataVille High School, Mr. Alan, a dedicated math teacher, is looking to digitalize his grading system. He maintains a gradebook where each student's test scores are recorded. This gradebook is organized like a matrix - each row for a student, each column for a test score.

Assignment
Your task is to write a Python function, calculate_student_averages(), that computes the average score for each student. The function should accept a 2D list (list of lists) representing students' test scores. Each sublist contains the scores of one student.

The function should return a list of tuples, with each tuple containing a student's index (position in the list, starting from 0) and their average score.

Caveats
Round the average scores to two decimal places.
Student not having any scores are represented by an empty inner list: its average is trivially 0.
For example:

Test	Result
gradebook = [[78, 82, 85], [92, 88, 91], [83, 76, 79], [95, 92]]

student_averages = calculate_student_averages(gradebook)
print(student_averages)
[(0, 81.67), (1, 90.33), (2, 79.33), (3, 93.5)]

In the quaint town of Bookville, there's a charming library beloved by all. However, the librarian, Mrs. Ella, faces a challenge. With so many books being borrowed and returned daily, it's hard to keep track of which books are in and which are out. To solve this, she's seeking help from aspiring Python programmers to create a digital tracking system.

Assignment
Your task is to write a Python function, update_library(), that will help Mrs. Ella manage her library more efficiently. The function should take two arguments:
A dictionary representing the current status of books (whether they're 'in' or 'out').
A list of tuples, where each tuple contains a book title and a status ('in' or 'out').
The function should update the library's status based on the list of tuples and return the updated dictionary. Each tuple in the list represents a new transaction (either borrowing or returning a book).

Caveats
it may happen that a book is not in the dictionary: if so, add it.
For example:

Test	Result
current_status = {
    "The Great Gatsby": "in",
    "To Kill a Mockingbird": "out",
    "1984": "in",
}

transactions = [
    ("To Kill a Mockingbird", "in"),
    ("The Catcher in the Rye", "out"),
    ("1984", "out"),
]

updated_status = update_library(current_status, transactions)
updated_skills = dict(sorted(updated_status.items()))   # HACK, ignore this
print(updated_status)
{'The Great Gatsby': 'in', 'To Kill a Mockingbird': 'in', '1984': 'out', 'The Catcher in the Rye': 'out'}



