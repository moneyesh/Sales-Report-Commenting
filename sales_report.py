"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #blank list
melons_sold = [] #blank list

f = open('sales-report.txt') #pen file

for line in f:      #for each line in the file we are opening...
    line = line.rstrip()  #removes white space to the right and makes each line seperate
    entries = line.split('|')  # the | is where it breaks up the line in to seperate entries
    salesperson = entries[0] #salesperson will be the first entry in entries line
    melons = int(entries[2]) #melons will be an integer pulled from third spot in the entry line for how many melons sold

    if salesperson in salespeople:  #if the salesperson in the salespeople list...
        position = salespeople.index(salesperson) #the position will tell the index number of the sales person in salespeople
        melons_sold[position] += melons #the melons_sold list will have the position number and the count of melons the sales person sold
        
    else:  #if the sales person isn't in the salespeople list...
        salespeople.append(salesperson) #append salesperson to salespeople list
        melons_sold.append(melons) #append melons to the melons_sold list... this creates a new entry since the sales person had no info listed


for i in range(len(salespeople)): #for the every person in salespeople
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #print the sales person name, sold, how many melons