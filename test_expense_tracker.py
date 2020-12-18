#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez
""" Test expense tracker script """

import pytest
import builtins
from unittest import mock

import expense_tracker 
from expense_tracker import Expenses 

        
def test_ideal_expenses():
    """Test ideal_expenses"""
    e = Expenses("bob", 3249.75)
    assert isinstance(e.avg_expense_dict, dict)
    assert e.ideal_expenses() == {"Food":600.00,
                                  "Housing":1573.0,
                                  "Entertainment":242.75,
                                  "Travel":754.00,
                                  "Extra":80.00}
     
def test_percentage(capsys):
    """Test percentage()"""
    e = Expenses("bob", 3249.75)
    assert isinstance(e.monthly_budget, float)
    e.percentage()
    captured = capsys.readouterr()
    assert captured.out == ('\n\nYou spent 18.46% of your budget on Food\n'
                            'You spent 48.4% of your budget on Housing\n'
                            'You spent 7.47% of your budget on Entertainment\n'
                            'You spent 23.2% of your budget on Travel\n'
                            'You spent 2.46% of your budget on Extra\n\n\n')

def test_most_expense(capsys):
    """Test most_expense"""
    e = Expenses("bob", 3249.75)
    e.most_expense()
    captured = capsys.readouterr()
    assert captured.out == ("The category with the largest expense is the Housing category with a value of 1573.0\n\n\n")

def test_compare_happy_path(capsys):
    """ Some happy path cases to test the compare function """
    e = Expenses("bob", 3249.75)

    with mock.patch("builtins.input", side_effect=[400, 1400, 200, 400, 70]):
        e.record_expenses()
    e.ideal_expenses()
    e.compare()
    captured = capsys.readouterr()
    assert captured.out == ("Your current monthly Food expense is fine.\n"
                            "Your current monthly Housing expense is fine.\n"
                            "Your current monthly Entertainment expense is fine.\n"
                            "Your current monthly Travel expense is fine.\n"
                            "Your current monthly Extra expense is fine.\n\n\n")


