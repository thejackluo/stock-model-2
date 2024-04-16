# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:00:53 2024

@author: atom2
"""

import numpy as np

class Stock:
    margin_of_safety = 0.25  # this should be experimented with
    max_dampener = 0.8  # this should be experimented with
    sell_rate = 0.15
    max_EPS_growth = 0.60  # this should be experimented with, but less priority
    target_rate = 0.18  # Define target_rate as a class attribute

    def __init__(self, stock_name, ticker, EPS_2023, EPS_growth, PE, current_price):
        self.stock_name = stock_name
        self.ticker = ticker
        self.EPS_2023 = EPS_2023
        self.EPS_growth = EPS_growth
        self.PE = PE
        self.avg_PE = self.get_average_PE()
        self.current_price = current_price
        self.dampener = self.determine_dampener()


    def get_average_PE(self):
        return np.mean(self.PE)

    @staticmethod
    def get_average_EPS_growth(EPS_growth):
        max_EPS_growth = 0.60
        EPS_growth = np.clip(EPS_growth, -max_EPS_growth, max_EPS_growth)
        return np.mean(EPS_growth)

    def predict_interest_rate(self, PE=None):
        EPS_avg = self.get_average_EPS_growth(self.EPS_growth)
        adjusted_EPS = EPS_avg * self.dampener
        if PE is None:
            PE = self.avg_PE
        EPS_2033 = self.exponential_growth(self.EPS_2023, 1 + adjusted_EPS, 10)
        price_2033 = PE * EPS_2033
        growth_rate = (price_2033 / self.current_price) ** (0.1)
        return growth_rate

    @staticmethod
    def exponential_growth(initial_value, growth_rate, num_iterations):
        current_value = initial_value
        for _ in range(num_iterations):
            current_value *= growth_rate  # Apply growth rate
        return current_value

    def target_prices(self, target_PE):
        EPS_avg = self.get_average_EPS_growth(self.EPS_growth)
        adjusted_EPS = EPS_avg * self.dampener
        EPS_2033 = self.exponential_growth(self.EPS_2023, 1 + adjusted_EPS, 10)
        price_2033 = target_PE * EPS_2033
        target_price = price_2033 / (self.target_rate + 1) ** 10
        sell_price = price_2033 / (self.sell_rate + 1) ** 10

        print(f"Using PE of {target_PE}, the original buy (target rate: {self.target_rate}) is {target_price}.")
        print(f"After margin of safety of {self.margin_of_safety}, the predicted buy is {target_price * (1 - self.margin_of_safety)}.")
        print(f"The predicted sell (sell rate: {self.sell_rate}) is {sell_price}.")
        return target_price

    def __str__(self):
        return f"{self.stock_name} ({self.ticker}) - Current Price: {self.current_price}"

    def evaluate(self):
        print(self)
        s = f"\nAt the current price of {self.current_price}, the model's projected interest rate is "
        s += str(self.predict_interest_rate())
        s += f"\nUsing the newest PE, {self.PE[-1]}, the model's predicted interest rate is "
        s += str(self.predict_interest_rate(self.PE[-1])) + f"\nDampener: {self.dampener}\n"
        s += f"Years of negative EPS Growth: {self.determine_num_of_negative_growths()}\n"
        print(s)

        while True:
            PE = float(input("Enter PE to evaluate, -997 for average, -998 for FYMost recent, -999 to exit: "))
            if PE == -997:
                print(f"Using Average PE of {self.get_average_PE()} and most recent EPS of {self.EPS_2023}, the model's predicted interest rate is ")
                print(self.predict_interest_rate(self.get_average_PE()))
            elif PE == -998:
                print(f"Using the most recent PE of {self.PE[-1]} and most recent EPS of {self.EPS_2023}, the model's predicted interest rate is ")
                print(self.predict_interest_rate(self.PE[-1]))
            elif PE == -999:
                break
            else:
                print(f"Using PE of {PE} and most recent EPS of {self.EPS_2023}, the model's predicted interest rate is ")
                print(self.predict_interest_rate(PE))
                self.target_prices(PE)
    
    def determine_dampener(self):
        dampener = self.max_dampener
        for growth in self.EPS_growth:
            if growth < 0:
                dampener -= 0.1
        if dampener != self.max_dampener:
            dampener += 0.1
        return dampener

    # Determine the number of years with negative EPS growth
    def determine_num_of_negative_growths(self):
        return sum(1 for growth in self.EPS_growth if growth < 0)


if __name__ == "__main__":
    # Input is a list of Earnings per Share (EPS) and Price to Earnings (PE) ratios
    TPLEPS = [0.31, 0.4730, -0.1330, 1.3400, 1.1750, 0.5260, -0.4480, 0.5340, 0.6590, -0.0870]
    TPLPE = [28.25, 21.24, 55.65, 35.93, 20.04, 19.01, 32.03, 35.88, 40.42, 29.73]

    # Input the stock's name, ticker, EPS for 2023, EPS growth, PE, and current price
    tpl = Stock("Texas Pacific Land", "TPL", 52.77, TPLEPS, TPLPE, 1650)
    tpl.evaluate()