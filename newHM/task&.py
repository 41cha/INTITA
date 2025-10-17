# Завдання 4: Ієрархія працівників
# Створіть базовий клас Employee з методом calculate_salary().
# Кожен підклас має реалізувати свій спосіб розрахунку зарплати.
# Створіть підкласи HourlyEmployee (погодинна оплата) та SalariedEmployee (фіксована зарплата). 
class Employee:
    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class SalariedEmployee(Employee):
    def __init__(self, annual_salary):
        self.annual_salary = annual_salary

    def calculate_salary(self):
        return self.annual_salary / 12

hourly_emp = HourlyEmployee(20, 160)
salaried_emp = SalariedEmployee(60000)

print(hourly_emp.calculate_salary())
print(salaried_emp.calculate_salary())