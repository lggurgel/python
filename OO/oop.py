# Python Object-Oriented Programming
import datetime


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

    # used for object recreation
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees if employees else []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('Lucas', 'Gurgel', 50000)
dev_1 = Developer('Lucas', 'Gabriel', 90000, 'python')
mng_1 = Manager('Lucas', 'Gurgel', 120000, [emp_1, dev_1])
emp_str = 'Ana Paula-Gomes-30000'
emp_2 = Employee.from_string(emp_str)

# my_date = datetime.date(2020, 11, 7)
# print(Employee.is_workday(my_date))

# print(isinstance(mng_1, Manager))
# print(isinstance(emp_1, Developer))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Developer))

print(Employee.fullname(emp_1))
print(emp_2.fullname())
print(dev_1.__dict__)
print(mng_1.__dict__)
mng_1.print_emps()

print(emp_1.__repr__())
print(dev_1)
print(dev_1 + mng_1)
