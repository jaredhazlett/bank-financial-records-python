#import our dependencies.
import os
import csv


#now we need a file path to the data.
poll_path = os.path.join('PyPoll_Data.csv')
with open(poll_path, 'r') as poll_file:
	poll_data = csv.reader(poll_file, delimiter=',')
#skip the header using next() function.
	poll_header = next(poll_data)
#we've create empty lists to hold values we'll need to count later. We've also create empty variables we'll input numbers into later.
	voters = []
	candidates = []
	khan_votes_list = []
	li_votes_list = []
	correy_votes_list = []
	otooley_votes_list = []
	khan_fraction = 0
	li_fraction = 0
	correy_fraction = 0
	otooley_fraction = 0
	
#we create a for loop to loop through the data. We'll add our tasks that need a loop below.
	for row in poll_data:
 #in the list voters we append each in row 0. We'll later print the len of this list to count all of the entries.
		voters.append(row[0])
  #we append the candidates into the list candidates. We'll print the set of this list to find the unique values e.g. no duplicates.
		candidates.append(row[2])
  #we append votes for khan, li, correy, and otooley into separate lists we'll count later.
		if row[2] == "Khan":
			khan_votes_list.append(row[0])
		if row[2] == "Li":
			li_votes_list.append(row[0])
		if row[2] == "Correy":
			correy_votes_list.append(row[0])
		if row[2] == "O'Tooley":
			otooley_votes_list.append(row[0])
#we create a fraction from the lists we've appended each vote into.
	khan_fraction = (len(khan_votes_list)/len(voters))
	khan_percent = "{:.00%}".format(khan_fraction)
	li_fraction = (len(li_votes_list)/len(voters))
	li_percent = "{:.00%}".format(li_fraction)
	correy_fraction = (len(correy_votes_list)/len(voters))
	correy_percent = "{:.00%}".format(correy_fraction)
	otooley_fraction = (len(otooley_votes_list)/len(voters))
	otooley_percent = "{:.00%}".format(otooley_fraction)
#we want to print everyone's vote and percent.
print("candidates:",set(candidates))
print("Khan votes:",len(khan_votes_list),"-",(khan_percent))
print("Li votes:",len(li_votes_list),"-",(li_percent))
print("Correy votes:",len(correy_votes_list),"-",(correy_percent))
print("O'Tooley votes:",len(otooley_votes_list),"-",(otooley_percent))
print("total votes:",len(voters))

#in order to select a winner, we use the max() function and a set {} to choose the max percent and to reduce dublicates. There shouldn't be any duplicates and therefore no reason to use a set now that we've already done the math and each percent is fixed.
winner = max({khan_percent, li_percent, correy_percent, otooley_percent})
#based on the max function selecting a winner, the below are if statements that print the required statement. We could use elif and end with else, but I found many if statements works too.
if winner == khan_percent:
    print("winner: Khan")
if winner == li_percent:
    print("winner: Li")
if winner == correy_percent:
    print("winner: Correy")
if winner == otooley_percent:
    print("winner: O'Tooley")

#we below use csvwriter.writerow to write into our blank file PyPoll_Write_File.csv.
write_poll_path = os.path.join('PyPoll_Write_File.csv')
with open(write_poll_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Title','Summary Stats','','Percentages'])
    csvwriter.writerow(["candidates:",set(candidates)])
    csvwriter.writerow(["Khan votes:",len(khan_votes_list),"-",(khan_percent)])
    csvwriter.writerow(["Li votes:",len(li_votes_list),"-",(li_percent)])
    csvwriter.writerow(["Correy votes:",len(correy_votes_list),"-",(correy_percent)])
    csvwriter.writerow(["O'Tooley votes:",len(otooley_votes_list),"-",(otooley_percent)])
    csvwriter.writerow(["total votes:",len(voters)])



    winner = max({khan_percent, li_percent, correy_percent, otooley_percent})

    if winner == khan_percent:
        csvwriter.writerow(["winner:", "Khan"])
    if winner == li_percent:
        csvwriter.writerow(["winner:", "Li"])
    if winner == correy_percent:
        csvwriter.writerow(["winner:", "Correy"])
    if winner == otooley_percent:
        csvwriter.writerow(["winner:", "O'Tooley"])


#we rewrite everything as a writerow so that all the values print as they would in our terminal. 
