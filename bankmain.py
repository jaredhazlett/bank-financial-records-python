#we need to import os and csv reader in order to read our data
import os
import csv

#now we need a file path to the data
bank_path = os.path.join('PyBank_Resources.csv') 


#now we need to create variables based on our data
profit_loss_total = 0
profit_loss_average = 0
months = 0
max_profit = []
min_profit = []
with open(bank_path) as bank_file:
	bank_data = csv.reader(bank_file, delimiter=',')

	bank_header = next(bank_data)
	
	for row in bank_data:
		profit_loss_total += float(row[1])
	print("total profit: " + str(int(profit_loss_total)))

	profit_average = (profit_loss_total)/86
	print("profit average: " + str(int(profit_average)))

	for row in bank_data:
		print("CSV row: {0}". format(row))
		


		


	





