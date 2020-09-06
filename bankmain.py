#we need to import os and csv reader in order to read our data
import os
import csv

#now we need a file path to the data
bank_path = os.path.join('PyBank_Resources.csv') 


#now we need to create variables based on our data
profit_loss_total = 0
profit_loss_average = 0
months = []
max_value = 0
min_value = 0
max_profit = [max_value]
min_profit = [min_value]
cumulative_total = 0
previous_cumulative_total = 0
cumulative_change = 0
cumulative_changes = []
first_month = 
last_month = 


#here we read our code
with open(bank_path) as bank_file:
	bank_data = csv.reader(bank_file, delimiter=',')

	bank_header = next(bank_data)
	
	#create a for loop to loop through each list (each row is a list based on type())
	#we loop through and add the numbers, making sure to add value to the second number after our calculation
	for row in bank_data:
		cumulative_total += int(row[1])
		cumulative_change = cumulative_total - previous_cumulative_total
		previous_cumulative_total += int(row[1])
		cumulative_changes.append(cumulative_change)
		months.append(row[0])
		profit_loss_total += float(row[1])
#for max & min value, we need to sort through the data row by row. That means we'll need to be part of the for loop.
#as we see a value higher or lower than the value stored, we need to erase the previous value, and add the new one.
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
	print("minimum profit:",min_value)

	print("maximum profit:",max_value)

	print("average changes:", sum(cumulative_changes)/86)

	print("total profit:", int(profit_loss_total))

	profit_average = (profit_loss_total)/86
	print("profit average:",int(profit_average))

	#for row in bank_data:
		#print("CSV row: {0}". format(row))
	print("months:",len(months))







		


	





