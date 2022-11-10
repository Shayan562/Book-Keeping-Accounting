import csv
import PySimpleGUI as sg

class Credentials:
    name = str
    password = str
    flag = str

    def getList(self):
        return [self.name, self.password, self.flag]
    


def getCredentialsFromFile():
    with open("login credentials.csv", mode='r') as file:
        csvFile=csv.reader(file)
 
        storedCredentials=[]
        for i in csvFile:
            if(i==[]):
                continue
            temp = Credentials()
            temp.name=i[0].lower()
            temp.password=i[1]
            temp.flag=i[2]
            storedCredentials.append(temp)
    return storedCredentials




def valueCheck(storedValues, username, password, flag):
    for i in storedValues:
        if(i.name==username):
            if(i.flag=="True"):
                i.flag=flag
                return True, storedValues
            else:
                if(i.password==password):
                    i.flag=flag
                    return True, storedValues

    return False, storedValues

def updateCredentialsInFile(storedValues):
    with open("login credentials.csv", mode='w', newline='') as file:
        csvFile=csv.writer(file)
        for i in storedValues:    
            csvFile.writerow(i.getList())

            

def login():
    sg.theme('DarkAmber')

    loginLayout = [ [sg.Text("Login", expand_x=True, justification="center")],
                [sg.Text("Username", expand_x=True, justification=("center"))],
                [sg.InputText(size=(34,1), key="-username-", do_not_clear=True)], 

                [sg.Text("Password", expand_x=True, justification=("center"), pad=((2,2),(15,0)))],
                [sg.InputText(size=(34,1), key="-password-", do_not_clear=False)], 
                [sg.Text("Remember Pass: "), sg.Radio("True","autoLogin",True,k="-flag_value-"), sg.Radio("False","autoLogin",k="-flagValue-")],
                [sg.Text("If password is saved, enter username only", expand_x=True, justification="center", k="-display_msg-")],
                [sg.Button("Login", expand_x=True, key="-login_button-")]
                ]

    storedValues=getCredentialsFromFile()
    Loginflag=False
    window = sg.Window("Book Keeper", loginLayout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or Loginflag:
            break
        elif event=="-login_button-" :
            Loginflag, storedValues=valueCheck(storedValues,values["-username-"],values["-password-"],values["-flag_value-"])
            if(Loginflag):
                updateCredentialsInFile(storedValues)
                break
            else:
                window.Element("-display_msg-").update("Incorrect Username or Password")

    window.close()