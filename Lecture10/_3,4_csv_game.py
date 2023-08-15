import csv
import random

players = [
    'Luke', 'Kate','Mark', 'Mary', 'Josh'
]


with open('game_simulator.csv', mode='w') as file:
    fieldnames = ["Player's name", "Score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for name in players:
        score = [random.randint(0,1000) for level in range(100)]
        writer.writerow({"Player's name": name, "Score": score})


with open('game_simulator.csv', mode='r') as inputfile, open('high_scores.csv', mode='w') as outputfile:
    fieldnames = ["Player's name", "High score"]
    writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
    writer.writeheader()

    reader = csv.DictReader(inputfile)
    reader_dict = [row for row in reader]
    
    for row in reader_dict:
        max_score = (max(list(map(int, (row["Score"].strip("[]").split(", "))))))
        writer.writerow({"Player's name": row["Player's name"], "High score": max_score})

