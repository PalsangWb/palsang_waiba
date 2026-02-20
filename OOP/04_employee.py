# Modelling of a problem in OOPs
"""
Noun == Class == Employee
Adjective == Attributes == name, age, salary
Verbs == Methods == getSalary(), increment()
"""
# Class Attributes - An attribut that belongs to the class rather than a particular object.
# Example:
class Employee:
    company = "Google"  #Specific to each class

palsang = Employee()  #Object instantiation
nischay = Employee() 
palsang.salary = "30k"
nischay.salary = "40k"

print(palsang.company)
print(nischay.company)

Employee.company = "Youtube"  #Changing the class attribute
print(palsang.company)
print(nischay.company)

print(palsang.salary)
print(nischay.salary)

