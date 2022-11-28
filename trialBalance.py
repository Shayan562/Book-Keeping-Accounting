import csv

def check(entry):
    if(entry[2]=='-'):
        return -1*int(entry[3])
    return int(entry[2])

def saveToFile(allEntries, month):
    
    month=month[month.find('-')+1:month.find('-',2)]
    if(month.isdigit()):
        allMonths=['January','February','March','April','May','June','July','August','September','October','November','December']
        month=allMonths[int(month)-1] 

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
    
    return trialBalance, saveToFile(trialBalance, journal[0][0])