import csv
import random

players = [
    ['Luke', 0],
    ['Kate', 0],
    ['Mark', 0],
    ['Mary', 0],
    ['Josh', 0]
]

for level in range(100):
    for number, player in enumerate(players):
        players[number][1] = random.randint(0,1000)


with open('game_simulator.csv', mode='w') as file:
    fieldnames = ["Player's name", "Score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for name, score in players:
        writer.writerow({"Player's name": name, "Score": score})


with open('game_simulator.csv', mode='r') as inputfile, open('high_scores.csv', mode='w') as outputfile:
    fieldnames = ["Player's name", "High score"]
    writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
    writer.writeheader()

    reader = csv.DictReader(inputfile)
    reader_dict = [row for row in reader]

    list_score = [int(row['Score']) for row in reader_dict]
    list_score.sort(reverse = True)
    
    for points in list_score:
        for row in reader_dict:
            if points == int(row['Score']):
                writer.writerow({"Player's name": row["Player's name"], "High score": row["Score"]})
                break
    
    