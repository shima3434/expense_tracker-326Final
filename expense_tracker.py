#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez
import json
"""
This is an expense tracker that aims to examine ones monthly expenditures by category and give suggestions on where money may be saved.
"""

class user_expenses:
    """
    Represents the total amount the user has to spend on their expenses
    and the amount that the user actuallly spends per category
    """
    def __init__(self,name):
        self.name = name

    def user_expenses(self, total, category):
        """
        Creates a dictionary of the users expenses and the total amount they have to spend
        Args:
            budget(total): The total amount one has to spend on expenses
            user_expenses(categories): A dictionary with all the categories one can spend money
        
        Side effect: 
            Fills the user expenses dictionary with their total expenses per category
        """
    

class average_expenses:
    """
    Represents the amount the average american spends on the expenses per category
    and the average total amount they have to spend
    """
    def __init__(self,name):
        super().__init__()
    def ideal_expenses(self, total, category):
        """
        Creates a dictionary of ideal spending amounts per category 
        Args:
            budget(total): The total amount one has to spend on expenses
            user_expenses(categories): A dictionary with all the categories one can spend money
        Side effects:
            Creates a dictionay with all average expenses per category
    """
    
# Need to insert an analytics class where one takes info from the user expenses(in user class) and compares it to the average expenses (in avg expense class)

class expense_analysis:
    """
    represents the methods used in various analytics for tracking
    
    track percentage of categorical spending over the total
    track what single expense was the highest
    track which category has the highest spending
    """
    
    def percentage(self,expenses):
        """ calculates percentage of categorical spending over the total
        args:
            expenses (dict) - dictionary from average_expenese class
        returns:
            output of categorical spending
        """
    def most_expense(self,expenses):
        """ finds the single largest expense
        args:
            expenses (dict)
        return:
            largest expense over all the categories
        """
    def highest_category(self,expenses):
        """ finds which category has the highest spending in terms of amount spent
        args:
            expenses (dict)
        return:
            highest spending category
        """

    

# Need to add the part where we write the info to a file


def write_amounts(self):
    """
    Writes and saves previous dictionaries as json files
    """
    
    # Expense is a dict so assigned variable must be a dict too
    expense = user_expense
    
    #serializing json
    with open ("amounts,txt", "w") as outfile:
        json.dump(expense, outfile)
    
                      