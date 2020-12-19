#Names: Shima Abdulla, Do Yun Kim, Burhan Marvi, Joseph Sanchez
""" Test expense tracker script """

import pytest
import builtins
from unittest import mock

import expense_tracker 
from expense_tracker import Expenses 

def test_ideal_expenses():
    """Test ideal expenses"""
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
    e = Expenses("ana", 11500)

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
    with mock.patch("builtins.input", side_effect=[700, 1700, 500, 900, 200]):
        e.record_expenses()
    e.ideal_expenses()
    e.compare()
    captured = capsys.readouterr()
    assert captured.out == ("You're spending too much on Food! Spend less next month\n"
                            "You're spending too much on Housing! Spend less next month\n"
                            "You're spending too much on Entertainment! Spend less next month\n"
                            "You're spending too much on Travel! Spend less next month\n"
                            "You're spending too much on Extra! Spend less next month\n\n\n")
    with mock.patch("builtins.input", side_effect=[601, 1572, 243, 760, 65]):
        e.record_expenses()
    e.ideal_expenses()
    e.compare()
    captured = capsys.readouterr()
    assert captured.out == ("You're spending too much on Food! Spend less next month\n"
                            "Your current monthly Housing expense is fine.\n"
                            "You're spending too much on Entertainment! Spend less next month\n"
                            "You're spending too much on Travel! Spend less next month\n"
                            "Your current monthly Extra expense is fine.\n\n\n")

def test_compare_edge(capsys):
    """ Some edge cases to test the compare function """
    e = Expenses("Tom", 17000)
    with mock.patch("builtins.input", side_effect=[599, 1572, 242, 753, 80]):
        e.record_expenses()
    e.ideal_expenses()
    e.compare()
    captured = capsys.readouterr()
    assert captured.out == ("Your current monthly Food expense is fine.\n"
                            "Your current monthly Housing expense is fine.\n"
                            "Your current monthly Entertainment expense is fine.\n"
                            "Your current monthly Travel expense is fine.\n"
                            "Your current monthly Extra expense is fine.\n\n\n")
    with mock.patch("builtins.input", side_effect=[601, 1574, 243, 755, 90]):
        e.record_expenses()
    e.ideal_expenses()
    e.compare()
    captured = capsys.readouterr()
    assert captured.out == ("You're spending too much on Food! Spend less next month\n"
                            "You're spending too much on Housing! Spend less next month\n"
                            "You're spending too much on Entertainment! Spend less next month\n"
                            "You're spending too much on Travel! Spend less next month\n"
                            "You're spending too much on Extra! Spend less next month\n\n\n")