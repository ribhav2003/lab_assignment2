class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def display_table(self):
        print("{:<10} {:<15} {:<5} {:<10}".format("Employee ID", "Name", "Age", "Salary (PM)"))
        for emp in self.employees:
            print("{:<10} {:<15} {:<5} {:<10}".format(emp.emp_id, emp.name, emp.age, emp.salary))

    def sort_table(self, sort_key):
        if sort_key == 1:
            self.employees.sort(key=lambda emp: emp.age)
        elif sort_key == 2:
            self.employees.sort(key=lambda emp: emp.name)
        elif sort_key == 3:
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter.")

if __name__ == "__main__":
    emp_table = EmployeeTable()

    emp_table.add_employee(Employee("161E90", "Ramu", 35, 59000))
    emp_table.add_employee(Employee("171E22", "Tejas", 30, 82100))
    emp_table.add_employee(Employee("171G55", "Abhi", 25, 100000))
    emp_table.add_employee(Employee("152K46", "Jaya", 32, 85000))

    print("Original Employee Table:")
    emp_table.display_table()

    print("\nChoose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    
    try:
        sort_option = int(input("Enter your choice (1/2/3): "))
        emp_table.sort_table(sort_option)

        print("\nSorted Employee Table:")
        emp_table.display_table()

    except ValueError:
        print("Invalid input. Please enter a valid number.")
