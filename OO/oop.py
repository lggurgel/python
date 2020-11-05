# Python Object-Oriented Programming


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        days = [5, 6]
        return True if day.weekday() in days else False
    

emp_1 = Employee('Lucas', 'Gurgel', 50000)

emp_str = 'Ana Paula-Gomes-30000'

emp_2 = Employee.from_string(emp_str)

print(Employee.fullname(emp_1))
print(emp_2.fullname())

import datetime

my_date = datetime.date(2020, 11, 7)
print(Employee.is_workday(my_date))