import csv

def saveToFile(allEntries, month):
    with open("./"+month+' Owners Equity.csv', mode='w', newline='') as file:
        csvFile=csv.writer(file)
        csvFile.writerow(['Description','Amount'])
        csvFile.writerows(allEntries)

def createOwnersEquity(trialBalance, netValue, month):
    ownersEquity=[]
    flag=False
    endingBalance=0
    for entry in trialBalance:
        if(entry[0].find('capital')!=-1 or entry[0].find('Capital')!=-1 or entry[0].find('beginning')!=-1 or entry[0].find('Beginning')!=-1):
            ownersEquity.append(['Beginning Balance', str(entry[2])])
            flag=True
            endingBalance+=int(entry[2])
            break
    if(not(flag)):
        ownersEquity.append(['Beginning Balance', '0'])
    flag=False

    if(netValue[0].find('Profit')!=-1):#add profit
        endingBalance+=int(netValue[2])
        ownersEquity.append(['Net Profit', netValue[2]])
    else:#subtract loss
        endingBalance-=int(netValue[2][1:-1])
        ownersEquity.append(['Net Loss', netValue[2]])

    for entry in trialBalance:
        if(entry[0].find('drawing')!=-1 or entry[0].find('Drawing')!=-1):
            ownersEquity.append(['Drawing', '('+str(entry[1])+')']) #check for drawing
            endingBalance-=int(entry[1])
            flag=True
    if(not(flag)):
        ownersEquity.append(['Drawing', '(0)'])
    if(endingBalance<0):
        bal='('+str(endingBalance*-1)+')'
    else:
        bal=endingBalance
    ownersEquity.append(['Ending Balance', bal])

    saveToFile(ownersEquity, month)
