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

player_atts = read_csv("data/PlayerAttributes.csv", delimiter=",")
players = read_csv("data/Player.csv", delimiter=",")

player_counter_sum = dict.fromkeys(players["player_api_id"], 0)
player_counter_len = dict.fromkeys(players["player_api_id"], 0)
player_counter_mean = dict.fromkeys(players["player_api_id"], 0)

for player, rating in zip(player_atts["player_api_id"], player_atts["overall_rating"]):
    if rating != '':
        player_counter_sum[player] += int(rating)
        player_counter_len[player] += 1

for player in player_counter_sum.keys():
     player_counter_mean[player] = player_counter_sum[player] / player_counter_len[player]

play_max_rating = max(player_counter_mean, key=player_counter_mean.get)
print(players["player_name"][players["player_api_id"].index(play_max_rating)])

print("TO DO dump in pickle")

with open('query3.pkl', 'wb') as f:
    pickle.dump(players["player_name"][players["player_api_id"].index(play_max_rating)], f)