import os
import csv

csvpath = "election_data.csv"

# read and open file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print (csvreader)
    next(csvreader, None) #skip header

    #initiate variables and lists to be used later on
    totalvotes = 0
    candidates = []
    votes = [0, 0, 0, 0]
    
    #loop through each row of the csv file
    #collect all unique values in the 3 column (Candidates) and append to list [candidates]
    #also find the total sum of votes for each candidates and append to a separate list [votes]
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
        
    

    percentage = []
    most_votes = 0
    # calculate percentage of votes and append to list [percentage]
    # also compare all values in votes list to find the largest one. Largest vote should match index of winning candidate
    for i in range (len(candidates)):
        percentage.append(votes[i]/totalvotes)
        if votes[i] > most_votes:
            most_votes = votes[i]
            winner = candidates[i]
    
    # specify the file to write to
    output_file = os.path.join("..", "PyPoll", "Output", "election_results.txt")

    # open the output file
    with open(output_file, 'w', newline='') as text_file:
        
        # write output to the specified file
        text_file.write("\n" +  "Election Results\n" 
        + "---------------------------\n" +  
        "Total Votes: " + str(totalvotes) + "\n" + 
        "---------------------------\n")
        

        for i in range (len(candidates)):
            text_file.write(candidates[i] + ": " + "{:.3%}".format(percentage[i]) + " (" + str(votes[i]) + ")" + "\n")
        
        text_file.write("---------------------------\n" +
         "Winner: " +  winner + "\n" +
          "---------------------------\n")


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
