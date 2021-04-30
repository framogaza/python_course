# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:16:55 2021

@author: Juan Carlos
"""
class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)

empleado1=Employee("Juan Carlos Domínguez",2000)
empleado2=Employee("Sandra Vargas",2500)
empleado3=Employee("Jhonathan Salas",1500)

empleado1.displayEmployee()
empleado2.displayEmployee()
empleado3.displayEmployee()
print("Total de empleados ", Employee.empCount)
