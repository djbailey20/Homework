import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

# csvpath = "C:\Users\shado\Documents\LearnPython\Day3\Stu_CerealCleaner\Resources\cereal.csv"
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    votes = 0
    candidates = []
    winner = ""
    winnerVotes = 0
    for row in csvreader:
        votes = votes+1
        if len(candidates) > 0:
            if any(i["name"] == row[2] for i in candidates):
                for x in candidates:
                    if(x["name"] == row[2]):
                        x["votes"] = x["votes"]+1
            else:
                candidates.append({"name": row[2], "votes": 1})
        else:
            candidates.append({"name": row[2], "votes": 1})
    print("Election Results")
    print("-----------------------------------")
    print(f"Total Votes: {votes}")
    print("-----------------------------------")
    for candidateInfo in candidates:
        if candidateInfo['votes'] > winnerVotes:
            winnerVotes = candidateInfo['votes']
            winner = candidateInfo['name']
        print(
            f"{candidateInfo['name']}: {round(candidateInfo['votes']/votes*100,3)}% ({candidateInfo['votes']})")
    print("-----------------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------------")

    f = open('info.txt', 'w')
    f.write("Election Results\n")
    f.write("-----------------------------------\n")
    f.write(f"Total Votes: {votes}\n")
    f.write("-----------------------------------\n")
    for candidateInfo in candidates:
        f.write(
            f"{candidateInfo['name']}: {round(candidateInfo['votes']/votes*100,3)}% ({candidateInfo['votes']})\n")
    f.write("-----------------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-----------------------------------\n")
    f.close()
