# Algorthms GUI Project / radix.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad
# Radix Sort

from employee import Employee


class Radix():
    def __init__(self):
        self.emp = []
        self.output = []

    def read_File(self, inputFile):
        fin = open(inputFile, 'r')
        i = 0
        for line in fin.readlines():
            self.emp.append(Employee(i))
            self.output.append(Employee(i))
            a, b, c, d = line.split()
            self.emp[i].putData(a, b, c, d)
            i = i + 1

    def getMax(self):
        max = 0
        for e in self.emp:
            if max < e.getSalary():
                max = e.getSalary()
        return max

    def sort(self):
        max = self.getMax()
        exp = 1
        while (max // exp) > 0:
            count = [0] * (10)
            for i in range(0, len(self.emp)):
                n = (self.emp[i].getSalary() // exp) % 10
                count[n] = count[n] + 1

            for i in range(1, 10):
                count[i] = count[i] + count[i - 1]

            i = len(self.emp) - 1
            while i >= 0:
                n = (self.emp[i].getSalary() // exp) % 10
                self.output[count[n] - 1] = self.emp[i]
                count[n] = count[n] - 1
                i = i - 1

            i = 0
            for o in self.output:
                self.emp[i] = o
                i = i + 1
            exp = exp * 10

    def displayOutput(self):
        output = ''
        for o in self.output:
            output = output + str(o.display()) + '\n'
        return output
