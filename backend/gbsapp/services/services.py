from decimal import Decimal

class BillingCalculators:
    """
        Utility class for billing calculations in the Gig Billing System.

        This class cannot be instantiated. Use static methods directly:

            platFormFee = BillingCalculators.calculate_platform_fee(Decimal('300'), 2)
            CustomerPortion = BillingCalculators.calculate_customer_portion(Decimal('300'), 2)

        Methods:
            calculate_platform_fee(payment, members): Returns the platform fee.
            calculate_customer_portion(payment, members): Returns the customer's portion.
    """
    
    def __init__(self):
        raise TypeError("BillingCalculators cannot be instantiated. use static methods directly")

    def __repr__(self) -> str:
        return 'Billing Calculator'
   
    @staticmethod
    def calculate_platform_fee(payment:Decimal, members:int):
        """
        Calculates the profit amount for an invoice

        Parameters:
            payment (Decimal): Invoice Payment amount (ex vat)
            members (Integer): Number of group members

        Returns:
            Decimal: Platform fee amount

        Raises:
            TypeError: If payment is not a Decimal.
            ValueError: If payment or members are negative, or members
                is 0 for payments over 100€.
        """ 
        #Guarding due to Python calculation bug
        payment = Decimal(str(payment))

        if not isinstance(payment, Decimal):
            raise TypeError("payment must be a Decimal, not float or int")

        if payment < 0 or members < 0:
            raise ValueError("Payment and members must be non-negative")
        
        if payment > 100 and members <= 0:
            raise ValueError("Payments over 100 require at least one member")

        if payment <= 100:
            profit = Decimal('5.00')
        elif payment <= 500:
            profit = Decimal('10.00') * members
        else:
            profit = (payment*Decimal('0.03')) * members
        
        return Decimal(profit)
    
    @staticmethod
    def calculate_customer_portion(payment:Decimal, members:int):
        """
        Calculates the amount a customer is liable to receive in the invoice

        Parameters:
            Decimal: Invoice Payment amount (ex vat)
            Integer: Number of group members

        Returns:
            Decimal: Amount of profit for the customer
        """
        return Decimal(payment - BillingCalculators.calculate_platform_fee(payment, members))