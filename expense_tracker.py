import os
import json

#function to load expense after program run
def load_expense():  
    if os.path.exists("expenses.json"):
        with open("expenses.json","r") as file:
            return json.load(file) #returning the whole data inside file to the list of expenses 
    else:
        print("No previous record of Expenses, Lets Start from today\n")
        return [] #if doesnot exist then returning empty list

#function to save expenses in the file
def save_expenses(expenses):
    with open("expenses.json","w") as file:  #write mode because we loaded the previous data and then added so need to overrite 
        json.dump(expenses, file, indent =2)

#function to take input for which feature to apply
def menu():
    print("\n----Welcome to Expence Tracker----\n")
    print("1. Add expense\n2. View all expenses\n3. View by category\n4. Calculate total spent\n5. Exit\n")
    choice = input("Your choice(1/2/3/4/5): ")
    return choice

#functin to add expenses on the list
def add_expense(expenses):
    while True: 
        print("Enter your expeses details as follows: \n")
        amount = float(input("Amount: "))
        category = input("Category: ")
        date = input("Date (YYYY/MM/DD): ")
        note = input("Note: ")
        expenses.append({
        "amount" : amount,
        "category" : category,
        "date" : date,
        "note" : note
        })
        more= input("Want to add more expenses (Y/N): ").lower()
        if more != "y":
            break
    save_expenses(expenses)
    print("\n Expenses added")
    
#function to view expenses
def view_expense(expenses):
    if not expenses:
        print("No expenses recenlty!!!\n")
    else:
        for i, e in enumerate(expenses,1):
            print(f"{i}. Amount: {e['amount']} for Category: {e['category']}, Date: {e['date']}, with a Note: {e['note']}\n")

#function to view expenses caategory wise
def view_category(expenses):
    if not expenses:
        print("No expenses recenlty!!!\n")
    else:
        cat= input("Enter the category!!!").lower()
        found= False
        for i, e in enumerate(expenses,1):
            if(e["category"].lower()==cat):
                print(f"{i}. Amount: {e['amount']} for Category: {e['category']}, Date: {e['date']}, with a Note: {e['note']}\n")
                found=True
        if not found:
            print("No category found!!!\n")

#function to calculate total expenses
def calcu_total(expenses):
    if not expenses:
        print("No expenses recenlty!!!\n")
    else:
        total = sum(e["amount"] for e in expenses)
        print(f"The total amount according to expeneses list is: {total}")


def main():
    expenses = load_expense()
    while True: 
        choice= menu()
        match(choice):
            case '1':
                add_expense(expenses)
            case '2':
                view_expense(expenses)
            case '3':
                view_category(expenses)
            case '4':
                calcu_total(expenses)
            case '5':
                break
            case _:
                print("Wrong Input please cleary state next time!!!\n")
        more_1 = input("Want again to proceed(Y/N): ").lower()
        if more_1 != "y":
            break

if __name__ == "__main__":
    main()


    
