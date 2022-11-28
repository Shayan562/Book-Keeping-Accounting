import csv

def saveToFile(allEntries ,month):
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

def balanceSheet(trialBalance, retainEarning ,month):
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
    valRetain=str(retainEarning)
    if(not(valRetain.isdigit())):
        valRetain=-1*int(valRetain[1:-1])
    ownersEquity.append(['Ending Balance of Retain Earning','-',retainEarning])
    print(valRetain)
    totalEquity+=int(valRetain)

    total+=totalAssets
    total+=totalLiabilities
    total+=totalEquity
    if(totalAssets<0):
        totalAssets='('+str(-1*totalAssets)+')'
    if(totalLiabilities<0):
        totalLiabilities='('+str(-1*totalLiabilities)+')'
    if(totalEquity<0):
        totalEquity='('+str(-1*totalEquity)+')'
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
