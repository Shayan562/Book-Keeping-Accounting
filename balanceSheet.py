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

# retainEarnings=[['Retain Earnings', '0'],
# ['Net Profit', '2520'],
# ['Dividends', '(2100)'],
# ['Ending Balance of Retained Earning', 420]]

# month='jan'

def saveToFile(allEntries, month):
    with open("./"+month+' Balance Sheet.csv', mode='w', newline='') as file:
        csvFile=csv.writer(file)
        # csvFile.writerow(['Description','Debit'])
        csvFile.writerows(allEntries)

def isAsset(entry):
    checkValues=['payable', 'Payable', 'unearned', 'Unearned', 'expense', 'Expense', 'capital', 
                 'Capital', 'beginning', 'Beginnings', 'revenue', 'Revenue', 'dividend', 'Dividend',
                 'stock', 'Stock', 'retain', 'Retain', 'total', 'Total']
    for i in checkValues:
        if(entry.find(i)!=-1):
            return False
    return True

def isLiability(entry):
    checkValues=['payable', 'Payable', 'unearned', 'Unearned']
    for i in checkValues:
        if(entry.find(i)!=-1):
            return True
    return False

def isEquity(entry):
    checkValues=['stock', 'Stock', 'capital', 'Capital', 'retain', 'Retain']
    for i in checkValues:
        if(entry.find(i)!=-1):
            return True
    return False

def balanceSheet(trialBalance, month):
    assets=[['Assets']]
    liabilities=[['Liabilities']]
    ownersEquity=[['Owners Equity']]
    balance=[['Description', 'Debit', 'Credit']]
    totalAssets=0
    totalLiabilities=0
    totalEquity=0
    total=0

    for entry in trialBalance:
        if(isAsset(entry[0])):
            if(entry[1]=='-'):
                assets.append([entry[0],entry[1],'('+str(entry[2])+')'])
                totalAssets-=int(entry[2])
            else:
                assets.append(entry)
                totalAssets+=int(entry[1])

        elif(isLiability(entry[0])):
            if(entry[2]=='-'):
                liabilities.append([entry[0],'('+str(entry[1])+')', entry[2]])
                totalLiabilities-=int(entry[1])
            else:
                liabilities.append(entry)
                totalLiabilities+=int(entry[2])

        elif(isEquity(entry[0])):
            if(entry[2]=='-'):
                ownersEquity.append([entry[0],'('+str(entry[1])+')', entry[2]])
                totalEquity-=int(entry[1])
            else:
                ownersEquity.append(entry)
                totalEquity+=int(entry[2])

    total+=totalAssets
    total+=totalLiabilities
    total+=totalEquity
    if(totalAssets<0):
        totalAssets='('+str(totalAssets)+')'
    if(totalLiabilities<0):
        totalLiabilities='('+str(totalLiabilities)+')'
    if(totalEquity<0):
        totalEquity='('+str(totalEquity)+')'
    assets.append(['', 'Total Assets', totalAssets])
    liabilities.append(['', 'Total Liabilities', totalLiabilities])
    ownersEquity.append(['', 'Total Equity', totalEquity])
    for values in assets:
        balance.append(values)
    for values in liabilities:
        balance.append(values)
    for values in ownersEquity:
        balance.append(values)

    saveToFile(balance, month)

    for i in balance:
        print(i)


        


# balanceSheet(trialBalance, month)
