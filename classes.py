# Define a class named 'employee'
class employee():
    # Constructor method to initialize the attributes of the class
    def __init__(self, name, base_salary, bonus_hrs, sales, n_hours, bonus, one_sale, days):

        self.name = name  # Employee name

        self.base_salary = base_salary  # Base salary

        self.bonus_hrs = bonus_hrs  # Extra hours worked

        self.sales = sales  # Total sales made

        self.n_hours = n_hours  # Number of hours worked per day

        self.bonus = bonus  # Added percentage for extra hours

        self.one_sale = one_sale  # Amount earned for each sale

        self.days = days  # Number of working days

    # Method to calculate and print the net salary of the employee
    def calculate_net_salary(self):

        # Formula to calculate net salary: base_salary + bonus for extra hours + bonus for sales
        net_salary = self.base_salary + self.bonus_hrs * (self.base_salary / (self.n_hours * self.days)) * (
                self.bonus / 100) + self.sales * self.one_sale
        
        # Print the result
        print("The salary of", self.name, "is:", net_salary, end="MAD")

# Create empty lists to store employee information
names = []

bonus_hrs = []

sales = []

days = []

# Input the number of employees, base salary, and other parameters
n = int(input("Enter the number of employees: "))

base_salary = float(input("Enter the base salary: "))

n_hours = float(input("Enter the number of hours worked by an employee in a day: "))

bonus = float(input("Enter the added percentage every extra hour: "))

one_sale = float(input("Enter the amount earned for each sale: "))

# Loop to input information for each employee
for i in range(n):

    print("Enter the name of employee number", i + 1, ":")

    a = input()

    names.append(a)  # Add employee name to the 'names' list

    print("Enter the total sales made by", names[i], ":")

    b = float(input())

    sales.append(b)  # Add total sales to the 'sales' list

    print("Enter the number of working days by", names[i], ":")

    c = float(input())

    days.append(c)  # Add number of working days to the 'days' list

    print("Enter the extra hours that", names[i], "worked:")

    d = float(input())

    bonus_hrs.append(d)  # Add extra hours worked to the 'bonus_hrs' list

# Loop to create an 'employee' object for each employee and calculate net salary
for i in range(n):

    e = employee(names[i], base_salary, bonus_hrs[i], sales[i], n_hours, bonus, one_sale, days[i])

    e.calculate_net_salary()





