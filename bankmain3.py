import os
import csv

bank_path = os.path.join('PyBank_Resources.csv')

profit_loss_total = 0
profit_loss_average = 0
months = []
min_value = 0
max_value = 0
max_profit = [max_value]
min_profit = [min_value]
cumulative_total = 0
previous_cumulative_total = 0
cumulative_change = 0
cumulative_changes = []
first_month = 0 
last_month = 0
firstminuslast = 0

with open(bank_path) as bank_file:
	bank_data = csv.reader(bank_file, delimiter=',')
	bank_header = next(bank_data)

	for row in bank_data:
		cumulative_total += int(row[1])
		cumulative_change = cumulative_total - previous_cumulative_total
		previous_cumulative_total += int(row[1])
		cumulative_changes.append(cumulative_change)
		months.append(row[0])
		profit_loss_total += float(row[1])
		last_month = row[1]

		if first_month == 0:
			first_month = int(row[1])

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

	print("last month:",last_month)

	print("minimum profit:",min_value)

	print("maximum profit:",max_value)

	print("average changes:", sum(cumulative_changes)/86)

	print("first month:",first_month)

	print("total profit:", int(profit_loss_total))

	profit_average = (profit_loss_total)/86
	print("profit average:",int(profit_average))

	#for row in bank_data:
		#print("CSV row: {0}". format(row))
	print("months:",len(months))

	firstminuslast = int(first_month) - int(last_month)
	print("first month minus last month:",firstminuslast)

write_bank_path = os.path.join("PyBank_Write_File.csv")
with open(write_bank_path, 'w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')
	csvwriter.writerow(['Summary Stats Name','Summary Stats Value'])
	csvwriter.writerow(['last month:',last_month])
	csvwriter.writerow(["minimum profit:",min_value])
	csvwriter.writerow(["maximum profit:",max_value])
	csvwriter.writerow(["average changes:", sum(cumulative_changes)/86])
	csvwriter.writerow(["total profit:", int(profit_loss_total)])
	csvwriter.writerow(["profit average:",int(profit_average)])
	csvwriter.writerow(["profit average:",int(profit_average)])
	csvwriter.writerow(["months:",len(months)])
	csvwriter.writerow(["first month:",first_month])
	csvwriter.writerow(["first month minus last month:",firstminuslast])

