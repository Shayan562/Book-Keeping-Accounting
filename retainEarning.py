import csv

# trialBalance=[['Cash', 8270, '-'],
# ['Common Stock', '-', 79000],
# ['Office Supplies', 1000, '-'],
# ['Furniture', 1300, '-'],
# ['Account Payable', '-', 2200],
# ['Service Revenue', '-', 5100],
# ['Building', 80000, '-'],
# ['Land', 29000, '-'],
# ['Note Payable', '-', 39000],
# ['Account Receivable', 1500, '-'],
# ['Salary Expense', 1130, '-'],
# ['Utility Expense', 450, '-'],
# ['Utility Payable', '-', 450],
# ['Rent Expense', 1000, '-'],
# ['Dividends', 2100, '-'],
# ['Total =', '201980', '201980']]

# month='jan'
# netValue=['Net Profit', '', '2520']

def saveToFile(allEntries, month):
    with open("./"+month+' Retained Earning.csv', mode='w', newline='') as file:
        csvFile=csv.writer(file)
        csvFile.writerow(['Description','Amount'])
        csvFile.writerows(allEntries)

def createRetainEarning(trialBalance, netValue, month):
    retainEarnings=[]
    flag=False
    endingBalance=0
    for entry in trialBalance:
        if(entry[0].find('retain')!=-1 or entry[0].find('Retain')!=-1):
            retainEarnings.append(['Retain Earnings', str(entry[2])])
            flag=True
            endingBalance+=int(entry[2])
            break
    if(not(flag)):
        retainEarnings.append(['Retain Earnings', '0'])
    flag=False

    if(netValue[0].find('Profit')!=-1):#add profit
        endingBalance+=int(netValue[2])
        retainEarnings.append(['Net Profit', netValue[2]])
    else:#subtract loss
        endingBalance-=int(netValue[2][1:-1])
        retainEarnings.append(['Net Loss', netValue[2]])


    for entry in trialBalance:
        if(entry[0].find('dividend')!=-1 or entry[0].find('Dividend')!=-1):
            retainEarnings.append(['Dividends', '('+str(entry[1])+')']) #check for drawing
            endingBalance-=int(entry[1])
            flag=True
    if(not(flag)):
        retainEarnings.append(['Dividends', '(0)'])
    if(endingBalance<0):
        bal='('+str(endingBalance*-1)+')'
    else:
        bal=endingBalance
    retainEarnings.append(['Ending Balance of Retained Earning', bal])

    saveToFile(retainEarnings, month)

    for i in retainEarnings:
        print(i)


# createRetainEarning(trialBalance, netValue, month)
