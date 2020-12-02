#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez
import json
"""
This is an expense tracker that aims to examine ones monthly expenditures by category and give suggestions on where money may be saved.
"""

class UserExpenses:
    """
    Represents the total amount the user has to spend on their expenses
    and the amount that the user actuallly spends per category
    """
    def __init__(self,name):
        self.name = name

    def user_Expense(self, total):
        """"
        Creates a dictionary of the users expenses and the total amount they have to spend
        Args:
            budget(total): The total amount one has to spend on expenses
        Side effect: 
            Fills the user expenses dictionary with their total expenses per category
        """
        food = float(input("How much do you spend on food monthly? "))
        utility_bills = float(input("What is your total utility bill? "))
        entertainment = float(input("How much do you spend on entertainment(i.e going to the movies, iceskating, etc...)? "))
        travel = float(input("What is your average momthly travel expense(includes: gas, bus fair etc...)? "))
        extra = float(input("What is you expense for other miscellaneous things?"))
        
        expense_dict = {}
        
        expense_dict["Food"] = food
        expense_dict["Utility Bills"] = utility_bills
        expense_dict["Entertainment"] = entertainment
        expense_dict["Travel"] = travel
        expense_dict["Extra"] = extra

    

class AverageExpenses:
    """
    Represents the amount the average american spends on the expenses per category
    and the average total amount they have to spend
    """
    def __init__(self,name):
        self.name = name
    def ideal_expenses(self, total):
        """
        Creates a dictionary of ideal spending amounts per category 
        Args:
            budget(total): The total amount one has to spend on expenses
        Side effects:
            Creates a dictionay with all average expenses per category
        """
        food_avg = 0
        util_avg = 0
        entertainment_avg = 0
        travel_avg = 0
        extra_avg = 0
        for key, value in expense_dict:
            if key == "food":
                food_avg = food_avg+ value
            elif key == "Utility Bills":
                util_avg = util_avg + value
            elif key == "Entertainment":
                entertainment_avg = entertainment_avg + value
            elif key == "Travel":
                travel_avg = travel_avg + value
            elif key == "Extra":
                extra_avg = extra_avg + value
        avg_expense_dict = {}
        avg_expense_dict["Food"] = food_avg
        avg_expense_dict["Utility Bills"] = util_avg
        avg_expense_dict["Entertainment"] = entertainment_avg
        avg_expense_dict["Travel"] = travel_avg
        avg_expense_dict["Extra"] = extra_avg
            
    
class ExpenseAnalysis:
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



def write_amounts(self):
    """
    Writes and saves previous dictionaries as json files
    """
    
    # Expense is a dict so assigned variable must be a dict too
    expense = user_expense
    
    #serializing json
    with open ("amounts,txt", "w") as outfile:
        json.dump(expense, outfile)
