# employee.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Contract(ABC):
    """Represents a contract and a payment process for a particular employeee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""


@dataclass
class Commission(ABC):
    """Represents a commission payment process."""

    @abstractmethod
    def get_payment(self) -> float:
        """Returns the commission to be paid out."""


@dataclass
class ContractCommission(Commission):
    """Represents a commission payment process based on the number of contracts landed."""

    commission: float = 100
    contracts_landed: int = 0

    def get_payment(self) -> float:
        """Returns the commission to be paid out."""
        return self.commission * self.contracts_landed


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout


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


# salaried_contract.py
from classes.contract import Contract


class SalariedContract(Contract):
    """Contract type for an employee being paid a monthly salary."""

    def __init__(self, monthly_salary, percentage=1):
        self.monthly_salary = monthly_salary
        self.percentage = percentage

    def get_payment(self) -> float:
        return self.monthly_salary * self.percenta
