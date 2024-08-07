"""
Stock object class for Ben graham's method

TODO: write documentations for each method
"""
import numpy as np

class Stock:
    graham_factor = 0.33  # "Graham liked to buy stocks when net assets are 66% of market cap"

    # Attributes
    def __init__(self, stock_name, ticker, assets, liabilities, market_cap, shares,lt_debt,current_price,year):
        self.stock_name = stock_name
        self.ticker = ticker
        #self.EPS_2023 = EPS_2023
        #self.EPS_growth = EPS_growth # Array of 10yr EPS
        #self.avg_EPS = self.get_average_EPS_growth(EPS_growth) # internal method
        #self.PE = PE
        #self.avg_PE = self.get_average_PE() # internal method
        self.current_price = current_price
        self.assets = assets
        self.liabilities = liabilities
        self.lt_debt = lt_debt
        self.net_assets = self.assets-self.liabilities-self.lt_debt
        self.market_cap = market_cap
        self.shares = shares
        self.net_asset_value = self.net_assets/self.shares
        self.current_price_above_nav = (self.current_price-self.net_asset_value)/self.net_asset_value
        self.year = year
        #self.dampener = self.determine_dampener() # internal method
        #self.buy_price = self.target_prices(self.avg_PE) #internal method
        #self.current_price_above_below_buy_price_percent = self.get_current_price_above_below_buy_price_percent() #internal method

    # General Util
    def __str__(self):
        # please print the entire stock object
        return f"Stock: {self.stock_name} ({self.ticker,self.year}) \n" + \
            f"Assets: {self.assets}\n" + \
            f"Liabilities: {self.liabilities}\n" + \
            f"Long-term Debt: {self.lt_debt}\n" + \
            f"Shares Outstanding: {self.shares}\n" + \
            f"Net Assets: {self.net_assets}\n" + \
            f"Current Price: {self.current_price}\n" + \
            f"Net Asset Value: {self.net_asset_value}\n" + \
            f"Above below: {self.current_price_above_nav}\n"

            #f"EPS 2023: {self.EPS_2023}\n" + \
            #f"EPS Growth: {self.EPS_growth}\n" + \
            #f"PE: {self.PE}\n" + \
            #f"Average PE: {self.avg_PE}\n" + \
            #f"Dampener: {self.dampener}\n" + \

        # return f"{self.stock_name} ({self.ticker}) - Current Price: {self.current_price}"

    # EPS Module
    @staticmethod
    # take the average eps growth and if it is lower than negative max eps growth or higher than max eps growth, clip it to the max eps growt
    def get_average_EPS_growth(EPS_growth):
        EPS_growth = np.clip(EPS_growth, -Stock.max_EPS_growth, Stock.max_EPS_growth)
        return np.mean(EPS_growth)
    
    # take the percent above or below the buy price that the current price is at
    def get_current_price_above_below_buy_price_percent(self):
        
        return (self.current_price-self.buy_price)/self.buy_price

    # from the eps_growth array, sum up all the negative eps growth (below zero)
    def determine_num_of_negative_growths(self):
        return len([growth for growth in self.EPS_growth if growth <= 0]) #Edited - stocks without 10 yrs data are showing up because they have 0s for years they did not exist.
        # return sum(1 for growth in self.EPS_growth if growth < 0)
    
    # Buy Sell Module
    def get_average_PE(self):
        return np.mean(self.PE)


    # Buy Sell Util
    ###
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
    ###

    def determine_dampener(self):
        dampener = self.max_dampener
        for growth in self.EPS_growth:
            if growth < 0:
                dampener -= 0.1
        if dampener != self.max_dampener:
            dampener += 0.1
        return dampener

    def target_prices(self, target_PE):
        EPS_avg = self.get_average_EPS_growth(self.EPS_growth)
        adjusted_EPS = EPS_avg * self.dampener
        EPS_2033 = self.exponential_growth(self.EPS_2023, 1 + adjusted_EPS, 10)
        price_2033 = target_PE * EPS_2033
        target_price = price_2033 / (self.target_rate + 1) ** 10
        buy_price = target_price * (1 - self.margin_of_safety)
        sell_price = price_2033 / (self.sell_rate + 1) ** 10
        
        #print(f"Using PE of {target_PE}, the original buy (target rate: {self.target_rate}) is {target_price}.")
        #print(f"After margin of safety of {self.margin_of_safety}, the predicted buy is {buy_price}.")
        #print(f"The predicted sell (sell rate: {self.sell_rate}) is {sell_price}.")
        return buy_price #TODO this only returns the buy price, it should return the sell price and ideally the target price too - or can be made different functions
   
    # TESTING MODULE
    def evaluate_old(self):
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

    def evaluate(self):
        print(self)
        s = f"\nAt the current price of {self.current_price}, the model's projected interest rate is (using average PE) "
        s += str(self.predict_interest_rate())
        s += f"\nUsing the newest PE, {self.PE[-1]}, the model's predicted interest rate is "
        s += str(self.predict_interest_rate(self.PE[-1]))# + f"\nDampener: {self.dampener}\n"
        #s += f"Years of negative EPS Growth: {self.determine_num_of_negative_growths()}\n"
        print(s)



