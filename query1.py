import pickle
import csv

def read_csv(path: str, delimiter: str):
    """
    Reads the csv file defined in path and gives it as dict of lists
    the dict keys are the variable names and the lists contain the
    observation per variable
    """
    output = {}

    with open(path, newline='') as csvfile:
        data_temp = csv.DictReader(csvfile, delimiter=delimiter)

        for row in data_temp:
                for fieldname in data_temp.fieldnames:  
                    if fieldname not in output.keys():
                        output[fieldname] = [row[fieldname]]
                    else:
                        output[fieldname].append(row[fieldname])

    print("done reading the file!")
    return output

countries = read_csv("data/Country.csv", delimiter=",")

max_length = max(len(item) for item in countries["name"])

longest_elements = [item for item in countries["name"] if len(item) == max_length]

with open('query1.pkl', 'wb') as f:
    pickle.dump(longest_elements, f)
