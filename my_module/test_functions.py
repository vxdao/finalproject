"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import *

def test_lose_bet():
    """ I will make a test for lose_bet function 
    by choose a betting  money =100 , then when we lost the game , the total money now supposed to be 200 ( original money )- 100 (betting money)= 100 
    """
    chips = Chips()
    chips.bet = 100
    chips.lose_bet()
    assert chips.total == 100
test_lose_bet()





    


