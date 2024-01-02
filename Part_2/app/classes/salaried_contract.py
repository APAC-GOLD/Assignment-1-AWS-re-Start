# salaried_contract.py
from classes.contract import Contract


class SalariedContract(Contract):
    """Contract type for an employee being paid a monthly salary."""

    def __init__(self, monthly_salary, percentage=1):
        self.monthly_salary = monthly_salary
        self.percentage = percentage

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage
