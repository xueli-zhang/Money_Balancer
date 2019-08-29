#This class is to calculate balance of incomes and outcomes
from datetime import date


class Budget_Calculator:

    def __init__(self, incomes_notes, outcomes_notes):

        self.incomes = self.read_notes(incomes_notes, "income")
        self.outcomes = self.read_notes(outcomes_notes, "outcome")
        self.balance = self.calculate_balance()

    def read_notes(self, file_path, note_type):
        f = open(file_path, "r")

        raw_notes = f.readlines()
        notes = []
        for note in raw_notes:
            print(note_type+": "+note)
            notes.append(float(note.replace("\n","")))

        f.close()
        return notes

    def calculate_balance(self):
        
        sumOfIncome = 0

        for income in self.incomes:
            sumOfIncome += income

        sumOfOutcome = 0

        for outcome in self.outcomes:
            sumOfOutcome += outcome
        
        balance = sumOfIncome - sumOfOutcome

        return balance
    
    def update_notes(self, budget_notes):
        f = open(budget_notes, "a+")

        #write date of budget notes
        today = date.today()
        print("Today's date is: "+ today.strftime("%B %d, %Y"))
        f.write("Summary of:"+ today.strftime("%B %d, %Y")+"\n")

        f.write("Incomes: \n")
        for income in self.incomes:
            f.write(str(income)+"\n")
        
        f.write("Outcomes: \n")
        for outcome in self.outcomes:
            f.write(str(outcome)+"\n")
        
        f.write("Balance: "+str(self.balance)+"\n")
        if(self.balance <= 0):
            f.write("WARRNING!!!***You are OVER BUDGET! ! !*** "+str(self.balance)+" AMOUNT OF MONEY!!!\n")
        else:
            f.write("You SAVED: "+str(self.balance)+"\n")
        f.close()

def main():
    income_path = "./income_list.txt"
    outcome_path = "./outcome_list.txt"
    budget_path = "./summary.txt"
    budget_notes = Budget_Calculator(income_path, outcome_path)
    budget_notes.update_notes(budget_path)

if __name__ == "__main__":
    main()
    

        

        
