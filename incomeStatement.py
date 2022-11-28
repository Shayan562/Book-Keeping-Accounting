import csv

def saveToFile(allEntries, month):
    with open("./"+month+' Income Statement.csv', mode='w', newline='') as file:
        csvFile=csv.writer(file)
        csvFile.writerow(['Description','Debit','Credit'])
        csvFile.writerows(allEntries)

def createIncomeStatement(trialBalance, month):
    netValue=0
    for entry in trialBalance:
        if((entry[0].find('revenue')!=-1 or entry[0].find('Revenue')!=-1 or entry[0].find('rev')!=-1 or entry[0].find('Rev')!=-1) and (entry[0].find('unearned')==-1 and entry[0].find('Unearned')==-1)):
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
        if((entry[0].find('revenue')!=-1 or entry[0].find('Revenue')!=-1 or entry[0].find('rev')!=-1 or entry[0].find('Rev')!=-1) and (entry[0].find('unearned')==-1 and entry[0].find('Unearned')==-1)):
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
    return income[-1]