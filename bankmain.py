#import our dependencies
import os
import csv
#path to our csv file
bank_path = os.path.join('Resources', 'PyBank_Resources.csv')
#most if not all of my variables and lsits
profit_loss_total = 0
profit_loss_average = 0
months = []
min_value = 0
max_value = 0
max_profit = [max_value]
min_profit = [min_value]
cumulative_total = 0
cumulative_change = 0
previous_cumulative_total = 0
cumulative_changes = []
first_month = 0
last_month = 0
firstminuslast = 0
#we open the file path and read it using csv.reader() with a delimiter to separate the columns of data
#we also skip the header of the data
with open(bank_path) as bank_file:
	bank_data = csv.reader(bank_file, delimiter=',')
	bank_header = next(bank_data)
#our for loop to loop through the data
#for lines 33-36 we find the average change for each row, ultimately divided by the total months. We subtract the row by the previous row, starting counting for the second row after we've already calculated, ensuring our cumulative total is the row after our previous cumulative total
	for row in bank_data:
		cumulative_total += int(row[1])
		cumulative_change = cumulative_total - previous_cumulative_total
		previous_cumulative_total += int(row[1])
		cumulative_changes.append(cumulative_change)
#for lines 38 we append each line each line into the months list so that we can count the months by printing the len(months)later on in row 74
		months.append(row[0])
		profit_loss_total += float(row[1])
		last_month = row[1]
#we set the first_month = 0, and then if it's == to 0, we add the first row in column 2. Once the condition is no longer satisfied, we break the if statement and first_month stays as the first month in the row.
		if first_month == 0:
			first_month = int(row[1])
#with our for statement we cycle through each row. If the max_value is less than the integer in column 2, then we remove the max value from our lsit max_profit, make max_value the new integer, and append it to our list. We do the same with min_value and min_profit but rather with a less than sign.
		if max_value < int(row[1]):
			max_profit.remove(max_value)
			max_value = int(row[1])
			max_profit.append(max_value)
		else:
			next
		if min_value > int(row[1]):
			min_profit.remove(min_value)
			min_value = int(row[1])
			min_profit.append(min_value)
		else:
			next
#we take the average profit per month
profit_average = (profit_loss_total)/86
#now we print our values:

print("maximum profit:",max_value)
print("minimum profit:",min_value)
print("average changes(average):", sum(cumulative_changes)/86)
print("profit average:",int(profit_average))
print("first month:",first_month)
print("last month:",last_month)
print("total profit/losses:", int(profit_loss_total))
print("total months:",len(months))
#here we take the first month minus the last month
firstminuslast = int(first_month) - int(last_month)
print("first month minus last month:",firstminuslast)

#finally we rewrite all the statements in another csv file we labeled "PyBank_Write_File.csv" - it's a blank file that our code will write in. We use csvwriter.writerow and rewrite all of our print statements
write_bank_path = os.path.join('Analysis', 'PyBank_Write_File.csv')
with open(write_bank_path, 'w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')
	csvwriter.writerow(['Summary Stats Name','Summary Stats Value'])
	csvwriter.writerow(["maximum profit:",max_value])
	csvwriter.writerow(["minimum profit:",min_value])
	csvwriter.writerow(["average changes:", sum(cumulative_changes)/86])
	csvwriter.writerow(["total profit/losses:", int(profit_loss_total)])
	csvwriter.writerow(["profit average:",int(profit_average)])
	csvwriter.writerow(["profit average:",int(profit_average)])
	csvwriter.writerow(["total months:",len(months)])
	csvwriter.writerow(["first month:",first_month])
	csvwriter.writerow(['last month:',last_month])
	csvwriter.writerow(["first month minus last month:",firstminuslast])
#now all answers should show up in the terminal and the empty file. 
