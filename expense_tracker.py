#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez
import json
import sys
from argparse import ArgumentParser


class Expenses:
    """
    Determines the monthly expenses of a single user by category(i.e, food, utility entertainment etc) 
    Detemrines the ideal or average monthly expenses for a single person. 
    Compares the ideal expenses to the user expenses to describe where the user should save more and gives where the user is spending the most .
    """
    def __init__(self, name, monthly_budget):
        self.name = name
        self.monthly_budget = monthly_budget
        
    def user_Expense(self):
        """"
        Creates a dictionary of the users expenses and the total amount they have to spend
        Args:
            total (float): The total amount one has to spend on expenses
        Side effect: 
            Fills the user expenses dictionary with their total expenses per category
        """
        self.monthly_expenses = {}
        food = float(input("How much do you spend on food monthly? "))
        utility_bills = float(input("What is your total utility bill? "))
        entertainment = float(input("How much do you spend on entertainment(i.e going to the movies, iceskating, etc...)? "))
        travel = float(input("What is your average momthly travel expense(includes: gas, bus fair etc...)? "))
        extra = float(input("What is you expense for other miscellaneous things?"))
        self.monthly_expenses["Food"] = food
        self.monthly_expenses["Utility Bills"] = utility_bills
        self.monthly_expenses["Entertainment"] = entertainment
        self.monthly_expenses["Travel"] = travel
        self.monthly_expenses["Extra"] = extra
        

    def ideal_expenses(self, total):
        """
        Creates a dictionary of ideal spending amounts per category 
        Args:
            budget(total): The total amount one has to spend on expenses
        Side effects:
            Creates a dictionay with all average expenses per category
        """
        self.avg_expense_dict = {}
        with open("avgexpenses.txt","r",encoding="utf-8") as f:
            for line in f:
                (key,val) = line.strip().split(':')
                self.avg_expense_dict[key]= val
                
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
        
    def write_amounts(self, filename):
        """ Writes and saves previous dictionaries as json files which the user can use to track their expenses
        """
    #Filename would be NameofFile.json
        fh = open(filename, "a+")
        expenseData = [self.monthly_expenses, self.avg_expense_dict]
        json.dump(expenseData, fh)

    def read_amounts(self, filename):
        """
        Reads and print out the contents of a json file
        args:
            filename (str): filename/path to a json file
        """
        fh = open(filename)
        tracker = json.load(fh)
        for item in tracker:
            print([item[:]])

def main():
    """ The actual program
    """
    
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
    if args.name != str:
        raise TypeError("Name must be a word")
    if args.total < 0:
        raise ValueError("Your budget must be a positive number")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    #Call functions