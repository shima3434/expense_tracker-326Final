#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez

from argparse import ArgumentParser
import json
import sys


class Expenses:
    """
    Determines the monthly expenses of a single user by category(i.e, food, utility entertainment etc) 
    Detemrines the ideal or average monthly expenses for a single person. 
    Compares the ideal expenses to the user expenses to describe where the user should save more and gives where the user is spending the most .
    """
    def __init__(self, name, monthly_budget):
        """ Create an instance of the Expenses class
        args:
            name (str): Name of user
            monthly_budget(float): Monthly Budget or take-home pay
        """
        self.name = name
        self.monthly_budget = monthly_budget
        
    def record_expenses(self):
        """"
        Creates a dictionary of the users expenses and the total amount they have to spend
        Args:
            monthly_budget(float): The total amount one has to spend on expenses
        Side effect: 
            Fills the user expenses dictionary with their total expenses per category
        """
        self.user_expenses = {}
        self.user_expenses["Food"] = float(input("How much do you spend on food monthly? "))
        self.user_expenses["Utility Bills"] = float(input("What is your total utility bill? "))
        self.user_expenses["Entertainment"] = float(input("How much do you spend on entertainment(i.e going to the movies, iceskating, etc...)? "))
        self.user_expenses["Travel"] = float(input("What is your average momthly travel expense(includes: gas, bus fair etc...)? "))
        self.user_expenses["Extra"] = float(input("What is you expense for other miscellaneous things? "))
        
        
    
    def ideal_expenses(self):
        """
        Creates a dictionary of ideal spending amounts per category 
        Args:
            monthly_budget(float): The total amount one has to spend on expenses
        Side effects:
            Creates a dictionay(dict of str and float, the keys will be string(e.g., "Food", "Utility), 
            and the values will be float(e.g., "600.00","1573.00") with all ideal (or what we called avg) expenses per category
        """
        self.avg_expense_dict = {}
        with open("avgexpenses.txt","r",encoding="utf-8") as f:
            for line in f:
                (key,val) = line.strip().split(':')
                self.avg_expense_dict[key]= val
                
    def percentage(self):
        """ calculates percentage of your total budget spent per expense category 
        returns:
            string messgae of the percentage of budget spent
        """
        for key, value in self.user_expenses:
            return(f"you spent {(value/self.monthly_budget)*100}% of your budget on {key}")
        
        
    def most_expense(self):
        """ finds the single largest expense
        return:
            largest expense over all the categories
        """
        max_exp = max(self.user_expenses, key = lambda x: self.user_expenses[x])
        return(f"The category with the largest expense is {max_exp} with a value of {self.user_expenses[max_exp]}")
            
        
    def compare(self):
        """ Compares the user expenses dictionary to the ideal expenses dictionary and gives feedback where neccesary
        args:
            expenses(dict) 
        return:
            String-Feedback on the spenditure in terms of should the expenses be decreased per category or if they are fine
        """
        for key, value in self.user_expenses and self.avg_expense_dict:
            if self.user_expenses[key] > self.avg_expense_dict[key]:
                if key in self.user_expenses.keys():
                    if self.user_expenses[value] > self.avg_expense_dict[value]:
                        return (f"You are spending above ideal amounts for you monthly {key} expense. Spend less next month")
                else:
                    if key in self.user_expenses.keys():
                        return(f"The amount you are spending is great for your monthly {key} expense.")
        
    def write_amounts(self, filename):
        """ Writes and saves previous dictionaries as json files which the user can use to track their expenses
        args:
            filename (str): the files name main method defaults filename
        """
    #Filename would be NameofFile.json
        with open("expenses.json", "a+") as fh:
            expenseData = [self.user_expenses, self.avg_expense_dict]
            json.dump(expenseData, fh)

    def read_amounts(self, filename):
        """ Reads and print out the contents of a json file
        args:
            filename (str): filename/path to a json file
        """
        with open(filename) as fh:
            tracker = json.load(fh)
            for item in tracker:
                print(item)

def main(name, monthly_budget, filename="expenses.json"):
    """ Display the users name, budget, expenses for each category
    Args:  
        name (str)
        monthly_budget ()
    """
    #et is short for expense tracker
    et = Expenses(name,monthly_budget)
    et.record_expenses()
    et.ideal_expenses()
    et.write_amounts(filename)
    et.read_amounts(filename)    
    
def parse_args(arglist):
    """ Parse and validate command-line arguments.
    Args: arglist (list of str): list of command-line arguments.
    Returns: namespace
    """  
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("name", type=str,
                        help="Name of user")
    parser.add_argument("monthly_budget", type=float,
                        help="Monthly budget that is allowed to be spent")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name, args.monthly_budget)