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

def saveToFile(allEntries, month):
    with open("./"+month+' Income Statement.csv', mode='w', newline='') as file:
        csvFile=csv.writer(file)
        csvFile.writerow(['Description','Debit','Credit'])
        csvFile.writerows(allEntries)


def createIncomeStatement(trialBalance, month):
    # trialBalance
    netValue=0
    for entry in trialBalance:
        if(entry[0].find('revenue')!=-1 or entry[0].find('Revenue')!=-1 or entry[0].find('rev')!=-1 or entry[0].find('Rev')!=-1):
            if(entry[2]=='-'):
                netValue-=int(entry[1])
            else:
                netValue+=int(entry[2])

        elif(entry[0].find('expense')!=-1 or entry[0].find('Expense')!=-1 or entry[0].find('exp')!=-1 or entry[0].find('Exp')!=-1):
            if(entry[2]=='-'):
                netValue-=int(entry[1])
            else:
                netValue+=int(entry[2])

    income=[['Revenue']]
    for entry in trialBalance:
        if(entry[0].find('revenue')!=-1 or entry[0].find('Revenue')!=-1 or entry[0].find('rev')!=-1 or entry[0].find('Rev')!=-1):
            income.append(entry)
    income.append(['Expense'])
    for entry in trialBalance:
        if(entry[0].find('expense')!=-1 or entry[0].find('Expense')!=-1 or entry[0].find('exp')!=-1 or entry[0].find('Exp')!=-1):
            income.append(entry)
    if(netValue<0):
        income.append(['Net Loss','','('+str(netValue*-1)+')'])
    else:
        income.append(['Net Profit','',str(netValue)])


    saveToFile(income, month)
    for i in income:
        print(i)
    return income[-1]

# createIncomeStatement(trialBalance, month)
                