#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez

from argparse import ArgumentParser
import json
import sys


class Expenses:
    """
<<<<<<< HEAD
    Determines the monthly expenses of a single user by category
    (i.e, food, utility entertainment etc) 
=======
    Determines the monthly expenses of a single user by category(i.e, food, housing, entertainment etc) 
>>>>>>> dd0ede0e9c2886df23de857d10b2945cf7d7d168
    Detemrines the ideal or average monthly expenses for a single person. 
    Compares the ideal expenses to the user expenses to describe where the user
    should save more, gives where the user is spending the most, and describes 
    the break down of the monthly expenses in terms of the budget.
    Attributes:
        name (str): Users Name
        monthly_budget (float): (monthly net income)
        user_expenses (dict): [Key] expense category : [Value] user monthly expense
        avg_expense_dict (dict): [Key] expense category : [Value] U.S. avg amount spent

    """
    def __init__(self, name, monthly_budget):
        """
        Create an instance of the Expenses class
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
        self.user_expenses["Housing"] = float(input("What is your total monthly housing bill? "))
        self.user_expenses["Entertainment"] = float(input("How much do you spend on entertainment(i.e going to the movies, iceskating, etc...)? "))
        self.user_expenses["Travel"] = float(input("What is your average monthly travel expense(includes: gas, bus fair etc...)? "))
        self.user_expenses["Extra"] = float(input("What is you monthly expense for other miscellaneous things? "))
        
        
    
    def ideal_expenses(self):
        """
        Creates a dictionary of ideal spending amounts per category 
        Args:
            monthly_budget(float): The total amount one has to spend on expenses
        Side effects:
            Creates a dictionay(dict of str and float, the keys will be string(e.g., "Food", "Housing"), 
            and the values will be float(e.g., "600.00","1573.00") with all ideal (or what we called avg) expenses per category
        """
        self.avg_expense_dict = {}
        with open("avgexpenses.txt","r",encoding="utf-8") as f:
            for line in f:
                (key,val) = line.strip().split(':')
                self.avg_expense_dict[key]= float(val)
                
    def percentage(self):
        """ calculates percentage of your total budget spent per expense category 
        Side effect:
            Prints a string message of the percentage of budget spent and adds a new line
        """
        print("\n")
        for key, value in self.user_expenses.items():
            print(f"You spent {round((value/self.monthly_budget)*100, 2)}% of your budget on {key}")
        print("\n")
        
    def most_expense(self):
        """ finds the single largest expense
        Side effect:
            Prints a string with the largest expense over all the categories and a black line below
        """
        max_exp = max(self.user_expenses, key = lambda x: self.user_expenses[x])
        print(f"The category with the largest expense is the {max_exp} category with a value of {self.user_expenses[max_exp]}")
        print("\n")    
        
    def compare(self):
        """ Compares the user expenses dictionary to the ideal expenses 
            dictionary and gives feedback where neccesary
        Side effect:
            prints a string message with feedback on the spenditure in terms 
            of should the expenses be decreased per category or if they are fine
        """
        for key in self.user_expenses and self.avg_expense_dict:
            if self.user_expenses[key] > self.avg_expense_dict[key]:
                if key in self.user_expenses.keys():
                    print(f"You are spending above the ideal amount for your monthly {key} expense. Spend less next month")
            else:
                if key in self.user_expenses.keys():
                    print(f"The current amount you are spending for your monthly {key} expense is fine.")
        print("\n")

    def write_amounts(self, filename):
        """ Writes and saves previous dictionaries as json files
            which the user can use to track their expenses
        args:
            filename (str): the files name main method defaults filename
        Side effects:
            Writes the json file 
        """
    #Filename would be NameofFile.json
        with open(filename, "w") as fh:
            expenseData = [self.user_expenses, self.avg_expense_dict]
            json.dump(expenseData, fh)

    def read_amounts(self, filename):
        """ Reads and print out the contents of a json file
        args:
            Filename (str): filename/path to a json file
        Side effect:
            prints a message of with that includes the user monthly expenses
            and a seperate message that includes the ideal expenses
        """
        with open(filename) as fh:
            tracker = json.load(fh)
            print (f"Here are your expenses for the month {tracker[0]}")
            print (f"Here are the monthly expenses of the average American {tracker[1]}")

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
    et.percentage()
    et.most_expense()
    et.compare()
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