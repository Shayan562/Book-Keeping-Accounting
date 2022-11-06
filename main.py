import PySimpleGUI as sg

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

    debitEntries=[]
    creditEntries=[]

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
        for i in self.debitEntries:
            print(i.description, "|", str(i.amount))

    def getAllCredit(self):
        for i in self.creditEntries:
            print(i.description, "|", str(i.amount))


def isSameDate(oldEntry, date, month, year):
    return (oldEntry.date==date and oldEntry.month == month and oldEntry.year==year)




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

            [sg.Button("Generate Trial Balance",size=(30,1), pad=((122,0),(15,2)) )]
            ]



def main():
    # if __name__ == "__main__":
    generalJournal = []              # for storing all the different entries
    window = sg.Window('Book Keeper', layout)   # Create the Window
    while True:                      # Event Loop to process "events" and get the "values" of the inputs
        event, values = window.read()
        if event == sg.WIN_CLOSED:   # if user closes window or clicks cancel #or event=='cancel'
            break

        elif event=="-add_debit-" and values["-desc_debit-"] and values["-amount_debit-"]:              #button pressed and box not empty
            if(generalJournal):      #when journal is not empty
                if(isSameDate(generalJournal[-1],values['-date-'],values['-month-'],values['-year-'])): #for same date as previous
                    generalJournal[-1].newDebitEntry(values["-desc_debit-"], values["-amount_debit-"])  #update the premade list
                else:                #for different date
                    print("Complete")
               
            else:                    #journal is empty
                newEntry=Entry(values['-date-'],values['-month-'],values['-year-'])
                newEntry.newDebitEntry(values["-desc_debit-"], values["-amount_debit-"])
                generalJournal.append(newEntry)
                print(generalJournal[-1].debitEntries[-1].description)

            print("Updated Debit Entries")
            generalJournal[-1].getAllDebit()
        elif event=="-add_credit-" and values["-desc_credit-"] and values["-amount_credit-"]:           #

            if(generalJournal):       #when journal is not empty
                if(isSameDate(generalJournal[-1],values['-date-'],values['-month-'],values['-year-'])):
                    generalJournal[-1].newCreditEntry(values["-desc_credit-"], values["-amount_credit-"])
                else:
                    print("Complete") #for diffierent date
               
            else:
                newEntry=Entry(values['-date-'],values['-month-'],values['-year-'])
                newEntry.newCreditEntry(values["-desc_credit-"], values["-amount_credit-"])
                generalJournal.append(newEntry)
            print("Updated Credit Entries")
            generalJournal[-1].getAllCredit()

    window.close()

main()