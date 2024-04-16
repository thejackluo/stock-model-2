# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:00:53 2024

@author: atom2
"""

"""
DOCUMENTATION: input.py

Input: An array of stock objects
Output: An array of stock objects (w/ buy sell price)

STOCK Object (input):
    - stock_name
    - ticker
    - current_price
    - PE
    - EPS
    - EPS_growth
    - Years_with_positive_EPS
    - dampener

STOCK Object (output):
    - stock_name
    - ticker
    - current_price
    - PE
    - EPS
    - EPS_growth
    - Years_with_positive_EPS
    - buy_price
    - sell_price
    - projedted_interest_rate (givenc current price)
    - dampener
FUNCTION
Our goal is to go through an API and get all the data and produce

"""

import numpy as np

if __name__ == "__main__":
    # Input is a list of Earnings per Share (EPS) and Price to Earnings (PE) ratios (test stocks)
    TPLEPS = [0.31, 0.4730, -0.1330, 1.3400, 1.1750, 0.5260, -0.4480, 0.5340, 0.6590, -0.0870]
    TPLPE = [28.25, 21.24, 55.65, 35.93, 20.04, 19.01, 32.03, 35.88, 40.42, 29.73]

    # Input the stock's name, ticker, EPS for 2023, EPS growth, PE, and current price
    tpl = Stock("Texas Pacific Land", "TPL", 52.77, TPLEPS, TPLPE, 1650)
    tpl.evaluate()
