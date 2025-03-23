"""
investment.py 

This module consists of investment returns of fixed deposit and SIP

"""
class investment :
    """
        This Class is a parent class
        This contains operations to calculate investment returns

        Attributes:
            amount(float): The amount we are investing at the time of investing
            returns_rate(float): The returns we are getting in return
            time(int): The total peroid of time we are investing

    """    
    def __init__(self,amount,returns_rate,time):
        """ 
            This initalizes the investment

            Attributes:
            amount(float): The amount we are investing at the time of investing
            returns_rate(float): The returns we are getting in return
            time(int): The total peroid of time we are investing

        """
        self._amount = amount
        self._returns_rate = returns_rate
        self._time = time
    
    @property
    def amount(self):
        """
            Getter property for amount 

        Returns:
            float: The value of investment amount
        """
        return self.amount
    
    @property
    def returns_rate(self):
        """
            Getter property for returns_rate 

        Returns:
            float: The value of returns_rate
        """
        return self.returns_rate
    
    @property
    def time(self):
        """
            Getter property for time 

        Returns:
            float: The value of time
        """
        return self.time
    
    def calculate(self):
        """
            This method calculates the investement returns

        Returns:
            float: The value after investment

        """
        pass

class FixedDeposit(investment):
    """
        This is a FixedDeposit class
        This Class is a child class of investment

    """
    def calculate(self):
        """
            This method calculates FD Returns

        Returns:
            float: The total value post investment

        """
        returns = self.returns_rate/100
        total_amount = self.amount * (1 + returns) ** self.time
        return total_amount
    
class SIP(investment):
    """
        This is a Sip class  
    This Class is a child class of investment

    """
    def calculate(self):
        """
            This method calculates SIP

    Returns:
        float: The total value post investment

        """
        months = self.time * 12
        yearly_returns = self.returns_rate/100
        returns = yearly_returns/12
        total_amount = (
            self.amount
            * (((1 + returns) ** months - 1) / returns)
            * (1 + returns)
        )
        return total_amount


FD = FixedDeposit(100,7,1)
TOTAL = FixedDeposit.calculate
print(f"fd returns :{TOTAL:.2f}")

sip_example = SIP(1000,10,20)
total = SIP.calculate
print(f"sip returns: {total:.2f}")
