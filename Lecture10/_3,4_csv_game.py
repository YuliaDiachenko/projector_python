import csv
import random

players = [
    'Luke', 'Kate','Mark', 'Mary', 'Josh'
]


with open('game_simulator.csv', mode='w') as file:
    fieldnames = ["Player's name", "Score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for level in range(100):
        for name in players:
            score = random.randint(0,1000) 
            writer.writerow({"Player's name": name, "Score": score})


with open('game_simulator.csv', mode='r') as inputfile, open('high_scores.csv', mode='w') as outputfile:
    fieldnames = ["Player's name", "High score"]
    writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
    writer.writeheader()

    reader = csv.DictReader(inputfile)
  
    reader_dict = []
    max_dict = {}
    
    for row in reader:
        reader_dict.append(row)
        max_dict[row["Player's name"]] = 0
 
    
    for name in max_dict.keys():
        max = 0 
        for row in reader_dict:
            if (name == row["Player's name"]) and (int(max) < int(row["Score"])):
                max = int(row["Score"])
                max_dict[row["Player's name"]] = max
    
    max_list = list(max_dict.values())
    max_list.sort(reverse=True)
  
    for score in max_list:
        for name in max_dict.keys():
            if score == max_dict[name]: 
                writer.writerow({"Player's name": name, "High score": score})
                max_dict.pop(name)
                break

