# Example: HR System
# The HR system needs to process payroll for the company’s employees, but there are different types of employees
# depending on how their payroll is calculated.
# The PayrollSystem implements a .calculate_payroll() method that takes a collection of employees
# and prints their id, name, and check amount using the .calculate_payroll() method exposed on each employee object.


from abc import ABC, abstractmethod  # Python provides the abc module to define abstract base classes.


class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print("")


# Employee is the base class for all employee types. It is constructed with an id and a name.
# This would be an abstract class: in this way all the derived classes can be initiated, instead no Employee instance
# would be possible to be created
class Employee(ABC):  # Deriving the ABC (Abstract Base Class) so no one can init Employee
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod  # This decorator force to implement this method in derived classes
    def calculate_payroll(self):
        pass


# The HR system requires that every Employee processed must provide a .calculate_payroll() interface that returns
# the weekly salary for the employee. The implementation of that interface differs depending on the type of Employee.
# For example, administrative workers have a fixed salary, so every week they get paid the same amount:
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)  # Calling Super Class `Employee` constructor
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


# The company also employs manufacturing workers that are paid by the hour,
# so you add an HourlyEmployee to the HR system:
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


# Finally, the company employs sales associates that are paid through a fixed salary plus a commission
# based on their sales, so you create a CommissionEmployee class:
class CommissionEmployee(
    SalaryEmployee
):  # Is derived from `SalaryEmployee` because both need to consider weekly salary in payroll calculation
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


# In Python, you don’t have to explicitly declare an interface. Any object that implements the desired interface can be
# used in place of another object. This is known as duck typing. Duck typing is usually explained as
# “if it behaves like a duck, then it’s a duck”.
# The DisgruntledEmployee class doesn’t derive from Employee, but it exposes the same interface required
# by the PayrollSystem then it can calculate its payroll.
class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1000000


# Python is one of the few modern programming languages that supports multiple inheritance.
# Multiple inheritance is the ability to derive a class from multiple base classes at the same time.
class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours doing office paperwork.")


# It turns out that sometimes temporary secretaries are hired when there is too much paperwork to do.
# The TemporarySecretary class performs the role of a Secretary in the context of the ProductivitySystem,
# but for payroll purposes, it is an HourlyEmployee.
# During multiple inheritance is fundamental to prevent TypeError runtime exceptions:
# 1. Explicitly implement the __init__ method in the derived class
# 2. Manage the Method Resolution Order (MRO) and check if the order of resolution is what you expect
class TemporarySecretary(Secretary, HourlyEmployee):
    # The following implementation show the `Diamond problem`
    # TemporarySecretary uses multiple inheritance to derive from two classes that ultimately also derive from Employee.
    # This causes two paths to reach the Employee base class, which is something you want to avoid in your designs.
    # Python offers way to force the right method to be invoked, nonetheless the design should be re-think
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
        # You need to specify `HourlyEmployee init` method and not `super` as usual because the MRO will point to
        # the wrong implementation: Secretary.__init__ --> SalaryEmployee.__init__ this latter accepts a number
        # of arguments that mismatch with the TemporarySecretary init arguments so you get a TypeError

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)
        # Same as above: MRO will result in calling Secretary.calculate_payroll() which is wrong because you need
        # to get the payroll based on the HourlyEmployee.calculate_payroll() method


# You can evaluate TemporarySecretary's MRO like that
def check_temporary_secretary_mro():
    print(TemporarySecretary.__mro__)


if __name__ == "__main__":
    secretary = Secretary(2, "John Smith", 1500)
    salary_employee = SalaryEmployee(1, "John Smith", 1500)
    hourly_employee = HourlyEmployee(2, "Jane Doe", 40, 15)
    commission_employee = CommissionEmployee(3, "Kevin Bacon", 1000, 250)
    payroll_system = PayrollSystem()
    payroll_system.calculate_payroll([secretary, salary_employee, hourly_employee, commission_employee])
