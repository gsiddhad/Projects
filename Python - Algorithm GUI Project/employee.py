# Algorthms GUI Project / employee.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad
# Employee Class / Radix Sort

class Employee():
    def __init__(self, name='', id=0, age=0, salary=0):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary

    def getSalary(self):
        return int(self.salary)

    def putData(self, name='', id=0, age=0, salary=0):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary

    def display(self):
        output = ''
        output = output + str(self.name)
        output = output + ' '
        output = output + str(self.id)
        output = output + ' '
        output = output + str(self.age)
        output = output + ' '
        output = output + str(self.salary)
        return output
