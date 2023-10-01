"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class EmployeeMs(Employee):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}."

class EmployeeC(Employee):
    def __init__(self,name,hours,hour_sal):
        super().__init__(name)
        self.hours = hours
        self.hour_sal = hour_sal

    def get_pay(self):
        return self.hours * self.hour_sal

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hour_sal}/hour.  Their total pay is {self.get_pay()}."

class EmployeeMsCm(EmployeeMs,Employee):
    def __init__(self, name, salary,contract_num,contract_sal):
        super().__init__(name,salary)
        self.contract_num = contract_num
        self.contract_sal = contract_sal

    def get_pay(self):
        return self.salary + self.contract_num * self.contract_sal

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contract_num} " \
               f"contract(s) at {self.contract_sal}/contract.  Their total pay is {self.get_pay()}."

class EmployeeCCm(EmployeeC,Employee):
    def __init__(self, name, hours, hour_sal,contract_num, contract_sal):
        super().__init__(name,hours,hour_sal)
        self.contract_num = contract_num
        self.contract_sal = contract_sal

    def get_pay(self):
        return self.hours* self.hour_sal + self.contract_num * self.contract_sal

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hour_sal}/hour and receives a " \
               f"commission for {self.contract_num} contract(s) at {self.contract_sal}/contract.  Their total pay " \
               f"is {self.get_pay()}."

class EmployeeMsB(EmployeeMs,Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def get_pay(self):
        return self.salary + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}." \
               f"  Their total pay is {self.get_pay()}."

class EmployeeCB(EmployeeC, Employee):
    def __init__(self,name, hours, hour_salary, bonus):
        super().__init__(name, hours, hour_salary)
        self.bonus = bonus

    def get_pay(self):
        return self.hours * self.hour_sal + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hour_sal}/hour and receives a bonus " \
               f"commission of {self.bonus}.  Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = EmployeeMs('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = EmployeeC('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = EmployeeMsCm('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = EmployeeCCm('Jan', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = EmployeeMsB('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = EmployeeCB('Ariel', 120, 30, 600)


