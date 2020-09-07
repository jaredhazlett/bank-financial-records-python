import os
import csv


#now we need a file path to the data
poll_path = os.path.join('../DesktopPythonStuff/PyPoll_Data.csv') 
with open(poll_path, 'r') as poll_file:
	poll_data = csv.reader(poll_file, delimiter=',')
	#skip the header using next() function
	poll_header = next(poll_data)
#we've create a list to hold each voter so we can count them later.
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
	
	

	

#we create a for loop to loop through the data - for each 
	for row in poll_data:
		voters.append(row[0])
		candidates.append(row[2])
		if row[2] == "Khan":
			khan_votes_list.append(row[0])
		if row[2] == "Li":
			li_votes_list.append(row[0])
		if row[2] == "Correy":
			correy_votes_list.append(row[0])
		if row[2] == "O'Tooley":
			otooley_votes_list.append(row[0])

	khan_fraction = (len(khan_votes_list)/len(voters))
	khan_percent = "{:.00%}".format(khan_fraction)
	li_fraction = (len(li_votes_list)/len(voters))
	li_percent = "{:.00%}".format(li_fraction)
	correy_fraction = (len(correy_votes_list)/len(voters))
	correy_percent = "{:.00%}".format(correy_fraction)
	otooley_fraction = (len(otooley_votes_list)/len(voters))
	otooley_percent = "{:.00%}".format(otooley_fraction)

	print("Khan votes:",len(khan_votes_list),"-",(khan_percent))
	print("Li votes:",len(li_votes_list),"-",(li_percent))
	print("Correy votes:",len(correy_votes_list),"-",(correy_percent))
	print("O'Tooley votes:",len(otooley_votes_list),"-",(otooley_percent))
	print("total votes:",len(voters))
	print("candidates:",set(candidates))

	winner = max({khan_percent, li_percent, correy_percent, otooley_percent})

	if winner == khan_percent:
		print("winner: Khan")
	if winner == li_percent:
		print("winner: Li")
	if winner == correy_percent:
		print("winner: Correy")
	if winner == otooley_percent:
		print("winner: O'Tooley")

write_poll_path = os.path.join('../DesktopPythonStuff/PyPoll_Write_File.csv')
with open(write_poll_path, 'w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')
	csvwriter.writerow(['Title','Summary Stats','','Percentages'])
	csvwriter.writerow(["Khan votes:",len(khan_votes_list),"-",(khan_percent)])
	csvwriter.writerow(["Li votes:",len(li_votes_list),"-",(li_percent)])
	csvwriter.writerow(["Correy votes:",len(correy_votes_list),"-",(correy_percent)])
	csvwriter.writerow(["O'Tooley votes:",len(otooley_votes_list),"-",(otooley_percent)])
	csvwriter.writerow(["total votes:",len(voters)])
	csvwriter.writerow(["candidates:",set(candidates)])

	winner = max({khan_percent, li_percent, correy_percent, otooley_percent})

	if winner == khan_percent:
		csvwriter.writerow(["winner:", "Khan"])
	if winner == li_percent:
		csvwriter.writerow(["winner:", "Li"])
	if winner == correy_percent:
		csvwriter.writerow(["winner:", "Correy"])
	if winner == otooley_percent:
		csvwriter.writerow(["winner:", "O'Tooley"])


	
