#Written by Shiven Desai
class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

# create three Employee objects with the given data
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# display the data for each employee on the screen
print("Employee 1:")
print("Name:", employee1.name)
print("ID Number:", employee1.id_number)
print("Department:", employee1.department)
print("Job Title:", employee1.job_title)

print("\nEmployee 2:")
print("Name:", employee2.name)
print("ID Number:", employee2.id_number)
print("Department:", employee2.department)
print("Job Title:", employee2.job_title)

print("\nEmployee 3:")
print("Name:", employee3.name)
print("ID Number:", employee3.id_number)
print("Department:", employee3.department)
print("Job Title:", employee3.job_title)
