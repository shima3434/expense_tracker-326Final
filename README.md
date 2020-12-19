# expense_tracker-326Final
Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez # expense_tracker-326Final

File(s) purpose:
avgexpenses.txt -The data in this file includes data on the average American monthly expenses. We found this data on USATODAY.
expense_tracker.py - This is the main script for our program. It takes into account the user's name and monthly budget alongside the user's monthly expenses for a series of categories. Ideally at the end of each month a user would input their name, monthly budget and expenditure per expense category. The program then performs a series of analytical tasks on the user’s expenditures including comparing the user's monthly expense per category with that of the average or ideal American, determining what percent of their budget is used per category, and identifying where a user’s highest expenditure is.
expenses.json - The purpose of this function is to open, write, and read json objects from a json file. Ideally our program will write the user's expenses to this file. This will deem useful in late months when a person is looking back at the previous months expenditures/inputs as now that information is easily accessible in one location.
test_expense_tracker.py - This is the test script for our expense_tracker.py file. It includes a series of test cases for our analytical methods and our ideal expenses method.
LICENSE - License from GitHub
README.PDF - Explain the purpose of each file in the repository, explain the instructions to use our program, explain the output of the program, and present an annotated bibliography.

Instructions to use the program
*This program will require two arguments to run the program* The two arguments are the user's name (str) and their monthly budget amount (float)
1) Enter python expense_tracker.py <name> <monthlybudget>

Explanation of the program
1) If you entered the parameters correctly then the program will ask you how much money you have spent five expenses: Food, utility bills, entertainment, travel, and extra
2) Enter for each prompt a value
3) The program will then print out an analysis of your spending in comparison to your budget and all your expenses compared to the average American expenses.
4) The program will also write the users monthly expenditure inputs that you gave to a json file for easy retrieval and future reference if needed by the user
Bibliography
Frankel, M. (2020). How does the average American spend their paycheck? See how you compare. Retrieved 4 December 2020, from https://www.usatoday.com/story/money/personalfinance/budget-and-spending/2018/05/08/how- does-average-american-spend-paycheck/34378157/

   This source was utilized to create the avg_expense_dict which is a dictionary on the average American expenses per category. We chose five categories and their corresponding expenses to represent throughout our code. Information from this site was written to a .txt file which was then read into our code.
