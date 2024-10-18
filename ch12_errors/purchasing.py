"""
Purchasing

There's a bug in the current vendor system that is letting players buy items from the shop even when they don't have enough gold.
Assignment

Complete the purchase_item function. If the character doesn't have enough gold raise an exception with the text not enough gold. Don't handle the exception.

Otherwise, return the amount of money the customer has leftover after completing the purchase.
"""

def purchase_item(price, gold_available):
    if price > gold_available:
        raise Exception('not enough gold')
    return gold_available - price


"""
---------------------------------
Inputs:
 * price: 10.00
 * gold_available: 20.00
Expected: 10.00
  Actual: 10.00
Pass
---------------------------------
Inputs:
 * price: 30.00
 * gold_available: 20.00
Expected Exception: not enough gold
  Actual Exception: not enough gold
Pass
---------------------------------
Inputs:
 * price: 15.10
 * gold_available: 15.10
Expected: 0.00
  Actual: 0.00
Pass
---------------------------------
Inputs:
 * price: 1430.00
 * gold_available: 69.00
Expected Exception: not enough gold
  Actual Exception: not enough gold
Pass
---------------------------------
Inputs:
 * price: 7.50
 * gold_available: 7.50
Expected: 0.00
  Actual: 0.00
Pass
---------------------------------
Inputs:
 * price: 100.00
 * gold_available: 99.99
Expected Exception: not enough gold
  Actual Exception: not enough gold
Pass
---------------------------------
Inputs:
 * price: 0.00
 * gold_available: 0.00
Expected: 0.00
  Actual: 0.00
Pass
============= PASS ==============
7 passed, 0 failed
"""