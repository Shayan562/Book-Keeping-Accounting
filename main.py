class debit:
    desc =  str
    amount = float

    def __init__(self, description, cost):
        self.desc=description
        self.amount=cost


class credit:
    desc=str
    amount=float

    def __init__(self, description, cost):
        self.desc=description
        self.amount=cost

class Entry:
    date=int
    month=str
    year=int

    debitEntries=[]
    creditEntries=[]

    def __init__(self, date, month, year):
        self.date=date
        self.month=month
        self.year=year

    def newDebitEntry(self, desc, cost):
        self.debitEntries.append(debit(desc,cost))







def main():
    if __name__ == "__main__":
        # obj=debit("This is the description", 20.8)
        # print(obj.desc, obj.amount)
        obj = Entry(2,"November", 2022)
        obj.newDebitEntry("Entry 1", 300)
        obj.newDebitEntry("Entry 2", 500)

        for i in obj.debitEntries:
            print(i.desc + "\t\t|\t" + str(i.amount))

main()