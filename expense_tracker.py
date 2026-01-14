import os
import json

#function to load expense after program run
def load_expense():  
    if not os.path.exists("expenses.json"):
        return [] #if doesnot exist then returning empty list
    
    try:
        with open("expenses.json", "r") as file:
            return json.load(file) 
        
    except json.JSONDecodeError:
        print("Expenses file is corrupted. Starting fresh.")
        return []
 

#function to save expenses in the file
def save_expenses(expenses):
    with open("expenses.json","w") as file:  #write mode because we loaded the previous data and then added so need to overrite 
        json.dump(expenses, file, indent =2)

#function to take input for which feature to apply
def menu():
    try:
        print("\n----Welcome to Expence Tracker----\n")
        print("1. Add expense\n2. View all expenses\n3. View by category\n4. Calculate total spent\n5. Exit\n")
        choice = int(input("Your choice(1/2/3/4/5): "))
        if choice not in range(1,6):
            print("Please enter a number between 1 and 5")
            return None
        return choice
    except ValueError:
        print("Invaild input! Please enter a number.")
        return None

#function to validate category
def validate_category(category):
    category = category.strip()
    if not category:
        raise ValueError("Category cannot be empty!")
    if len(category) > 50:
        raise ValueError("Category name too long (max 50 chars)")
    return category

#function to validate date
def validate_date(date_str):
    # Simple format check: YYYY/MM/DD
    try:
        year, month, day = date_str.split('/')
        year, month, day = int(year), int(month), int(day)
        if not (1 <= day <= 31):
            raise ValueError("Day must be 1-31")
        if not (1 <= month <= 12):
            raise ValueError("Month must be 1-12")
        if year < 2020 or year > 2030:
            raise ValueError("Year seems unreasonable")
        return date_str
    except ValueError as e:
        raise ValueError(f"Invalid date format. Use YYYY/MM/DD. Error: {e}")

#function to validate note
def validate_note(note):
    note = note.strip()
    if len(note) > 200:
        raise ValueError("Note too long (max 200 chars)")
    return note if note else "No note"

#functin to add expenses on the list
def add_expense(expenses):
    while True: 
        try: 
            print("Enter your expeses details as follows: \n")
            amount = float(input("Amount: "))
            if amount <=0:
                raise ValueError("Amount must be positive")
            
            category = validate_category(input("Category: "))
            date = validate_date(input("Date (YYYY/MM/DD): "))
            note = validate_note(input("Note: "))

            expenses.append({
            "amount" : amount,
            "category" : category,
            "date" : date,
            "note" : note
            })

            save_expenses(expenses)
            print("\n Expenses added")

            more= input("Want to add more expenses (Y/N): ").lower()
            if more != "y":
                break
        
        except ValueError as e:
            print(f"Error: {e}")
    
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
            case 1:
                add_expense(expenses)
            case 2:
                view_expense(expenses)
            case 3:
                view_category(expenses)
            case 4:
                calcu_total(expenses)
            case 5:
                break
            case _:
                print("Wrong Input please cleary state next time!!!\n")
        more_1 = input("Want again to proceed(Y/N): ").lower()
        if more_1 != "y":
            break

if __name__ == "__main__":
    main()


    
