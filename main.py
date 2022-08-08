#Import csv 
import os
import csv
#Create variables 
months = 0
Profit_Loss = 0
previous_net_pl = 0
net_pl = 0
current_pl = 0 
change_list = []
months_changes = []
#average_change = change_list / months
greatest_change = []
greatest_decrease = []
csv_path = os.path.join("./budget_data.csv")
#open with handling 
with open (csv_path) as csvfile: 
    csvreader =csv.reader(csvfile, delimiter= ",")
    print(csvreader)
    csv_header = next(csvreader)
  # Read each row of data after the header
    months = 1 + months 
    row = next(csvreader)
    previous_net_pl = int(row[1])
    net_pl = net_pl + int(row[1])
     
    for row in csvreader:
        #total months and total P/L
            months = 1 + months 
            net_pl = net_pl + int(row[1])
           
        #calculate the change in P/L  and months
            pl_change = int(row[1]) - previous_net_pl
            previous_net_pl = int(row[1]) 
            change_list.append(pl_change)
            months_changes.append(row[0])     
            #current_pl = int(row[1])
            #pl_change = (current_pl - Profit_Loss - previous_net_pl)/months
            #int(change_list.append(pl_change))
if pl_change > greatest_change[row(1)]:
    greatest_change[row(1)] = pl_change
    greatest_change[row (0)] = row[""]
    
print(months)
print(net_pl)
print(pl_change)
print(months_changes)
print(change_list)