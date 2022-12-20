# ==================================================================================================================================================================
# The self keyword:
# 1. Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
# 2. If we have a method that takes no arguments, then we still have to have one argument(self).
# ==================================================================================================================================================================

# How to create a class in Python
class Employee:
	# Class attribute
	empCount = 0
	
    # Constructor of class. It is mainly used for assignment of instance variables.
	def __init__(self, name, salary ):
		# Instance variable or Instance attributes
		self.emp_name = name
		self.emp_salary = salary
		Employee.empCount += 1  # Incrementing a class attribute for each class object creation
		
	# Method of a class - To print instance variables
	def displayEmployeeInfo(self):
		print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)
		
	# Method of a class - To print class variables
	def displayEmployeeCount(self):
		print("Employee Count : ",Employee.empCount) # Note thatwe use class name instead of self while accessing Class Variables

# Object instantiation - Creating class objects
emp1 = Employee('Vivek', 1000)  
emp2 = Employee('Jadhav', 2000)

# Calling Class methods to print values
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()

emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()

# Accessing & printing the instance variables
print(emp1.emp_name)
print(emp2.emp_name)

# ==================================================================================================================================================================
# Accessing & printing the Class variable

# Using class name
print(Employee.empCount) 

# Using object
print(emp1.empCount)
print(emp2.empCount)
# ==================================================================================================================================================================

# ==================================================================================================================================================================
# Updating Class variable

# Using class name
Employee.empCount = 10

# Using object
emp1.empCount = 20

# Note that separate instance of empCount has been ctreated for emp1 object, but for emp2 as there is no instance of empCount it uses the value from Class variable
print(emp1.empCount) # Output -> 20
print(emp2.empCount) # Output -> 10

# Note that Class varibale value is not changed and has no effect of "emp1.empCount = 20" on it.
print(Employee.empCount) # Output -> 10
# ==================================================================================================================================================================
