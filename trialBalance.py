import csv

class Item:
    def __init__(self):
        sNum=1
        desc=''
        amount=0

    def getList(self):
        return [str(self.sNum), self.desc, self.amount]

# journal=[['1-jan-2022', 'Cash', '79000', '-'], ['1-jan-2022', 'Common Stock', '-', '79000'],
#  ['3-jan-2022', 'Office Supplies', '1000', '-'], ['3-jan-2022', 'Furniture', '1300', '-'],
#  ['3-jan-2022', 'Account Payable', '-', '2300'], ['4-jan-2022', 'Cash', '1500', '-'],
#  ['4-jan-2022', 'Service Revenue', '-', '1500'], ['7-jan-2022', 'Building', '80000', '-'],
#  ['7-jan-2022', 'Land', '29000', '-'], ['7-jan-2022', 'Cash', '-', '70000'],
#  ['7-jan-2022', 'Note Payable', '-', '39000'], ['11-jan-2022', 'Account Receivable', '600', '-'],
#  ['11-jan-2022', 'Service Revenue', '-', '600'], ['15-jan-2022', 'Salary Expense', '1130', '-'],
#  ['15-jan-2022', 'Cash', '-', '1130'], ['16-jan-2022', 'Account Payable', '1000', '-'],
#  ['16-jan-2022', 'Cash', '-', '1000'], ['18-jan-2022', 'Cash', '2100', '-'],
#  ['18-jan-2022', 'Service Revenue', '-', '2100'], ['19-jan-2022', 'Account Receivable', '900', '-'],
#  ['19-jan-2022', 'Service Revenue', '-', '900'], ['25-jan-2022', 'Utility Expense', '450', '-'],
#  ['25-jan-2022', 'Cash', '900', '-'], ['25-jan-2022', 'Utility Payable', '-', '450'],
#  ['25-jan-2022', 'Account Payable', '-', '900'], ['31-jan-2022', 'Rent Expense', '1000', '-'],
#  ['31-jan-2022', 'Dividends', '2100', '-'], ['31-jan-2022', 'Cash', '-', '3100']]

def check(entry):
    if(entry[2]=='-'):
        return -1*int(entry[3])
    return int(entry[2])

def saveToFile(allEntries, month):
    
    month=month[month.find('-')+1:month.find('-',2)]
    if(month.isdigit()):
        allMonths=['January','February','March','April','May','June','July','August','September','October','November','December']
        month=allMonths[month-1] 

    with open("./"+month+' Trial Balance.csv', mode='w', newline='') as file:
        csvFile=csv.writer(file)
        csvFile.writerow(['Description','Debit','Credit'])
        csvFile.writerows(allEntries)
    return month

def trial(journal):
    allItems=[]
    for entry in journal:
        flag=False
        if(allItems==[]):
            allItems.append([entry[1],check(entry)])
            # flag=True
            continue
        for item in allItems:
            if(entry[1]==item[0]):#desc in genral journal == desc in trial balance
                flag=True
                item[1]=item[1]+check(entry)
        if(not flag):
            allItems.append([entry[1],check(entry)])

    trialBalance=[]
    for item in allItems:
        if(item[1]>0):
            trialBalance.append([item[0], item[1], '-'])
            continue
        # else:
        trialBalance.append([item[0], '-', item[1]*-1])
    
    debTotal=0
    credTotal=0
    for i in journal:

        if(i[2]!='-'):
            debTotal+=int(i[2])
        if(i[3]!='-'):
            credTotal+=int(i[3])

    trialBalance.append(['Total =',str(debTotal),str(credTotal)])

    for i in trialBalance:
        print(i)
    
    return trialBalance, saveToFile(trialBalance, journal[0][0])


# trial(journal)

    
