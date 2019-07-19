import random
import datetime

"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        splurge_price = random.randint(5,9)

        # rush hour pricing
        date = datetime.datetime.now()
        formatted = '{:%w %I %p}'.format(date)
        date_info = formatted.split(" ")

        day = date_info[0]
        time = date_info[1]
        time_period = date_info[2]

        if day > 5 and time > 8 and time < 11 and time_period == 'AM':
            splurge_price += 4
            
        return splurge_price

    def get_total(self):
        """Calculate price, including tax."""
        
        # if melon species is a christmas melon, change the base price
        base_price = self.get_base_price()

        if self.species == 'Christmas melon':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""


    tax = 0.17
    order_type = "international"

    # enforce the passing of a country code with international melon
    # orders by using init and super
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    
    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total = total + 3
        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order"""

    tax = 0

    def __init__(self, species, qty, passed_inspection=False):
        super().__init__(species, qty)
        self.passed_inspection = passed_inspection
        

    def mark_inspection(self, passed):
        # if passed(which is either True or False) is true, update the passed inspection var
        self.passed_inspection = passed