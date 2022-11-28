import login
import journal
import trialBalance
import incomeStatement
import ownersEquity
import retainEarning
import balanceSheet

if __name__=='__main__':
    login.login()
    generalJournal=journal.createGeneralJournal()
    trial, month=trialBalance.trial(generalJournal)
    netIncome=incomeStatement.createIncomeStatement(trial, month)
    ownersEquity.createOwnersEquity(trial, netIncome, month)
    retain=retainEarning.createRetainEarning(trial, netIncome, month)
    balanceSheet.balanceSheet(trial, retain ,month)