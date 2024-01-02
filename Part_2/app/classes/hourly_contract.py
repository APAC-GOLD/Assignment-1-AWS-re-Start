# hourly_contract.py
from classes.contract import Contract


class HourlyContract(Contract):
    """Contract type for an employee being paid on an hourly basis."""

    def __init__(self, pay_rate, hours_worked=0, employer_cost=1000):
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.employer_cost = employer_cost

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost
