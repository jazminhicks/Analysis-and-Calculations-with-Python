import os
import csv

csvpath = "election_data.csv"

# read and open file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print (csvreader)
    next(csvreader, None) #skip header

    totalvotes = 0
    candidates = []
    votes = [0, 0, 0, 0]
    
    for row in csvreader:
        totalvotes += 1
        if row [2] not in candidates:
            candidates.append(row[2])

        if row[2] == "Khan":
            votes[0] += 1
        
        elif row[2] == "Correy":
            votes [1] += 1
        
        elif row[2] == "Li":
            votes[2] += 1

        elif row[2] == "O'Tooley":
            votes[3] += 1
        
    
    #print (candidates)
    #print (votes)
    percentage = []
    most_votes = 0
    for i in range (len(candidates)):
        percentage.append(votes[i]/totalvotes)
        if votes[i] > most_votes:
            most_votes = votes[i]
            winner = candidates[i]
    
    #print (candidates)
    #print (votes)
    #print (percentage)
    #print (winner)
    
    print ("")
    print ("Election Results")
    print ("---------------------------")
    print ("Total Votes: " + str(totalvotes))
    print ("---------------------------")
    for i in range (len(candidates)):
        print (candidates[i] + ": " + "{:.3%}".format(percentage[i]) + " (" + str(votes[i]) + ")")
    

    print ("---------------------------")
    print ("Winner: " + winner)
    print ("---------------------------")
