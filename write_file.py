import json

def write_amounts(self):
    """
    Writes and saves previous dictionaries as json files
    """
    # Expense is a dict so assigned variable must be a dict too
    expense = user_expenses
    
    #serializing json
    with open ("amounts,txt", "w") as outfile:
        json.dump(expense, outfile)
    