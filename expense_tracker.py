#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez

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

    def insert_meaningful_name(self, total, category):
        """
        Creates a dictionary of the users expenses and the total they have tp spend
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
    
    def insert_meaningful_name(self, total, category)
    """
        Args:
            budget(total): The total amount one has to spend on expenses
            user_expenses(categories): A dictionary with all the categories one can spend money
        Side effects:
            Creates a dictionay with all average expenses per category
    """
    
# Need to insert an analytics class where one takes info from the user expenses(in user class) and compares it to the average expenses (in avg expense class)

# Need to add the part where we write the info to a file
