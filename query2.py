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

teams = read_csv("data/Team.csv", delimiter=",")
matches = read_csv("data/Match.csv", delimiter=",")

teams_counter = dict.fromkeys(teams["team_api_id"], 0)


for team_home, team_away, idx in zip(matches["home_team_api_id"], matches["away_team_api_id"], range(len(matches["home_team_api_id"]))):
    if int(matches["home_team_goal"][idx]) == 0:
         teams_counter[team_away] += 1
    if int(matches["away_team_goal"][idx]) == 0:
         teams_counter[team_home] += 1
    # teams_counter[team_away] += int(matches["home_team_goal"][idx])
    # teams_counter[team_home] += int(matches["away_team_goal"][idx])

team_max_without_goal = max(teams_counter, key=teams_counter.get)
print(teams["team_long_name"][teams["team_api_id"].index(team_max_without_goal)])

with open('query2.pkl', 'wb') as f:
    pickle.dump(teams["team_long_name"][teams["team_api_id"].index(team_max_without_goal)], f)