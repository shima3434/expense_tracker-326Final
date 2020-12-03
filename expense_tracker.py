#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez
import json
import sys
from argparse import ArgumentParser
"""
This is an expense tracker that aims to examine ones monthly expenditures by category and give suggestions on where money may be saved.
"""

class Expenses:
    """
    Determines the monthly expenses of a single user by category(i.e, food, utility entertainment etc) 
    Detemrines the ideal or average monthly expenses for a single person. 
    Compares the ideal expenses to the user expenses to describe where the user should save more and gives where the user is spending the most .
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

    def ideal_expenses(self, total):
        """
        Creates a dictionary of ideal spending amounts per category 
        Args:
            budget(total): The total amount one has to spend on expenses
        Side effects:
            Creates a dictionay with all average expenses per category
        """
        avg_expense_dict = {}
        with open("avgexpenses.txt","r",encoding="utf-8") as f:
            for line in f:
                (key,val) = line.strip().split(':')
                avg_expense_dict[key]= val
                
                
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
    
#Write function ***I think this might be outside of the class***
def write_amounts(self, filename):
    """ Writes and saves previous dictionaries as json files which can be used by the user to track their expenses
    """
    #Filename would be NameofFile.json
    fh = open(filename, "w")
    expenseData = [expense_dict, avg_expense_dict]
    json.dump(expenseData, fh)


def parse_args(arglist):
    """ Parse and validate command-line arguments.
    Parameters: arglist (list of str): list of command-line arguments.
    Returns: namespace
    """  
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("name", type=str,
                        help="Name of user")
    parser.add_argument("total", type=float,
                        help="Monthly budget that is allowed to be spent")
    parser.add_argument("expenses", type=dict,
                        help="Dictionary variable from average_expense class")
    parser.add_argument("filename", type=str,
                        help="Name of the file or path to file")   
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    #Call functions