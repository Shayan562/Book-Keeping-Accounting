import PySimpleGUI as sg
import csv

class item:
    description =  str
    amount = float

    def __init__(self, desc, cost):
        self.description=desc
        self.amount=cost


class Entry:
    date=int
    month=int
    year=int

    debitEntries, creditEntries = ([],[])

    def __init__(self, date, month, year):
        self.date=date
        self.month=month
        self.year=year

    def newDebitEntry(self, desc, cost):
        self.debitEntries.append(item(desc,cost))

    def newCreditEntry(self, desc, cost):
        self.creditEntries.append(item(desc,cost))

    def deleteCreditEntry(self, desc):
        index=0
        for i in self.debitEntries:
            if(i.description==desc):
                self.debitEntries.pop(index)
                break
            index+=1

    def deleteCreditEntry(self, desc):
        index=0
        for i in self.creditEntries:
            if(i.description==desc):
                self.creditEntries.pop(index)
                break
            index+=1

    def getAllDebit(self):
        debitList = []
        for i in self.debitEntries:
            new = [i.description, str(i.amount)]
            debitList.append(new)
        return debitList

    def getAllCredit(self):
        creditList = []
        for i in self.creditEntries:
            new = [i.description, str(i.amount)]
            creditList.append(new)
        return creditList
    
    def convertToList(self, entry):
        dateStr=str(self.date)+"-"+str(self.month)+"-"+str(self.year)
        for i in self.debitEntries:
            entry.append([dateStr, i.description, str(i.amount), "-"])
        for i in self.creditEntries: 
            entry.append([dateStr, i.description, "-", str(i.amount)])
        return entry


def isSameDate(oldEntry, date, month, year):
    return (oldEntry.date==date and oldEntry.month==month and oldEntry.year==year)


def saveToFile(allEntries):
    month=allEntries[0][0]
    month=month[month.find('-')+1:month.find('-',2)]
    if(month.isdigit()):
        allMonths=['January','February','March','April','May','June','July','August','September','October','November','December']
        month=allMonths[month-1] 

    # debTotal=0
    # credTotal=0
    # for i in allEntries:

    #     if(i[2]!='-'):
    #         debTotal+=int(i[2])
    #     if(i[3]!='-'):
    #         credTotal+=int(i[3])

    # allEntries.append([' ','Total =',str(debTotal),str(credTotal)])
    # print("debTotal: "+str(debTotal))
    # print("credTotal: "+str(credTotal))

    with open("./"+month+' General Journal.csv', mode='w', newline='') as file:
        csvFile=csv.writer(file)
        csvFile.writerow(['Date','Description','Debit','Credit'])
        csvFile.writerows(allEntries)


def createGeneralJournal():
    sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
    layout = [  [sg.Text("Enter Transactions",expand_x=True, justification=("center"))], 

                [sg.Text('Date'),sg.InputText(key="-date-", do_not_clear=True, size=(15,1)), 
                sg.Text('Month'),sg.InputText(key="-month-", do_not_clear=True, size=(15,1)), 
                sg.Text('Year'), sg.InputText(key="-year-", do_not_clear=True, size=(15,1))],

                [sg.Text("Debit", expand_x=True, justification=("center"), pad=((2,2),(15,0)))],  #debit section
                [sg.Text('Description'), sg.InputText(size=(34,1), key="-desc_debit-", do_not_clear=False), 
                 sg.Text("Amount"), sg.InputText(size=(12,1), key="-amount_debit-", do_not_clear=False)],
                [sg.Button('Add', key="-add_debit-" ,size=(26,1),pad=((136,0),(2,2)) )] ,

                [sg.Text("Credit", expand_x=True, justification=("center"), pad=((2,2),(15,0)))],   #credit section
                [sg.Text('Description'), sg.InputText(size=(34,1), key="-desc_credit-", do_not_clear=False), 
                 sg.Text("Amount"), sg.InputText(size=(12,1), key="-amount_credit-", do_not_clear=False)],
                [sg.Button('Add' , key="-add_credit-" ,size=(26,1),pad=((137,0),(2,2)) )] ,

                [sg.Button("Done", k='-generate_trial_balance-', size=(30,1), pad=((122,0),(15,2)) )]
             ]
    generalJournalEntry=Entry(0,0,0)          # for storing all the different entries
    allEntries=[]
    updateFlag=False
    window = sg.Window('Book Keeper', layout)   # Create the Window
    while True:                      # Event Loop to process "events" and get the "values" of the inputs
        event, values = window.read()
        if event == sg.WIN_CLOSED:   # if user closes window or clicks cancel #or event=='cancel'
            break

        elif event=="-add_debit-" and values["-desc_debit-"] and values["-amount_debit-"]:              #button pressed and box not empty
  
            if(isSameDate(generalJournalEntry,values['-date-'],values['-month-'],values['-year-'])): #for same date as previous
                generalJournalEntry.newDebitEntry(values["-desc_debit-"], values["-amount_debit-"])  #update the premade list
                updateFlag=True

            else:                #for different date
                #saving code
                allEntries=generalJournalEntry.convertToList(allEntries)
                updateFlag=False
                newEntry=Entry(values['-date-'],values['-month-'],values['-year-'])
                newEntry.creditEntries.clear()
                newEntry.debitEntries.clear()
                newEntry.newDebitEntry(values["-desc_debit-"], values["-amount_debit-"])
                generalJournalEntry=newEntry
               
        elif event=="-add_credit-" and values["-desc_credit-"] and values["-amount_credit-"]:           #
            if(isSameDate(generalJournalEntry,values['-date-'],values['-month-'],values['-year-'])):
                generalJournalEntry.newCreditEntry(values["-desc_credit-"], values["-amount_credit-"])
                updateFlag=True
            else:
                allEntries=generalJournalEntry.convertToList(allEntries)
                updateFlag=False
                #write to file
                newEntry=Entry(values['-date-'],values['-month-'],values['-year-'])
                newEntry.creditEntries.clear()
                newEntry.debitEntries.clear()
                newEntry.newCreditEntry(values["-desc_credit-"], values["-amount_credit-"])
                generalJournalEntry=newEntry
        
        elif event=="-generate_trial_balance-":
            break
               
    if(updateFlag):
        allEntries=generalJournalEntry.convertToList(allEntries)

    window.close()
    saveToFile(allEntries)
    # print(allEntries)
    return allEntries
# createGeneralJournal()