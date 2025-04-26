from datetime import datetime
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%m-%d-%Y")
    
    try: 
        valid_date = datetime.strptime(date_str, "%m-%d-%Y")
        return valid_date.strftime("%m-%d-%Y")
    except ValueError:
        print("Error: Invalid Date format!, please enter (mm-dd-yyyy)")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative number")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid Category, please enter 'I' or 'E' ")
    return get_category()


def get_description():
    return input("Enter Description (optional): ")

