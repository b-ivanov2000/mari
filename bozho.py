#Which of the following statements about dictionaries in Python is true?
#c. Dictionaries are mutable and can be modified after creation.

#There are two main methods to remove items from a list: remove() and pop(). Which of the following statements are true?


def calculate_student_averages(gradebook_input):
    return_list = []
    counter = 0
    for i in gradebook_input:
        if len(i) == 0:
            student_avg = 0
        else:
            student_avg = round(sum(i) / len(i), 2)
        return_list.append((counter, student_avg))
        counter += 1
    return return_list

gradebook = [[78, 82, 85], [92, 88, 91], [83, 76, 79], [95, 92]]
student_averages = calculate_student_averages(gradebook)
print(student_averages)

def update_library(current_status, transactions):
    for (book, transaction) in transactions:
        current_status[book] = transaction
    return current_status

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