import os
import csv

csvpath = "budget_data.csv"

# read and open file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print (csvreader)
    next(csvreader, None) #skip header
    months = 0
    total = 0
    profit_losses = []
    dates = []
    
    # loop through each row in the file

    for row in csvreader:
        #print (row)
        months += 1     # find total number of row/months

        total = total + int(row[1]) # sum all profits/losses

        pl = int(row[1])
        profit_losses.append(pl) #create a new list of just the profit/loss data and 
                                 #store information as integers

        dates.append(row[0]) #create a new list of all dates in the file
    

    difference = []
    
    for i in range (len (profit_losses) - 1):
        # calculate the difference between current and next month profit/losses
        # store these values into a new list called difference
        difference.append(profit_losses[i + 1] - profit_losses[i]) 
    
    #calculate average of all values in differnce and format
    average_change = '{:02.2f}'.format(sum(difference)/len(difference)) 

    greatest_increase = 0
    greatest_decrease = 0
    

    #loop through difference find the highest and lowest value
    #also saving the corresponding month that both took place
    for i in range (len(difference)):
        
        if (difference[i] > greatest_increase):
            greatest_increase = difference [i]
            increase_date = dates[i + 1]
        elif (difference[i] < greatest_decrease):
            greatest_decrease = difference[i]
            decrease_date = dates[i + 1]
    
    # specify the file to write to
    output_file = os.path.join("..", "PyBank", "Output", "financial_analysis.txt")

    # open the output file
    with open(output_file, 'w', newline='') as text_file:
        
        # text to be added
        text = ["\n", "Financial Analysis\n", "-------------------------------\n",
        "Total: $" + str(total) + "\n",
        "Total Months: " + str(months) + "\n", 
        "Average Change: $" + str(average_change) + "\n", 
        "Greatest Increase in Profits: " + increase_date + " ($" + str(greatest_increase) + ")" + "\n",
        "Greatest Decrease in Profits: " + decrease_date + " ($" + str(greatest_decrease) + ")" + "\n"]
        
        # write to the file
        text_file.writelines(text)


    print ("")
    print ("Financial Analysis")
    print ("-------------------------------")
    print ("Total Months: " + str(months))
    print ("Total: $" + str(total))
    print ("Average Change: $" + str(average_change))
    print ("Greatest Increase in Profits: " + increase_date + " ($" + str(greatest_increase) + ")")
    print ("Greatest Decrease in Profits: " + decrease_date + " ($" + str(greatest_decrease) + ")")
