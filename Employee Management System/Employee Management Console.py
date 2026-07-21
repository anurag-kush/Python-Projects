# Employee Management System
# Capstone Version 1.0
# Getting the Employee details from the user
employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ")
employee_department = input("Enter Employee Department: ")
employee_age = input("Enter Employee Age: ")
monthly_salary = input("Enter Employee Monthly Salary: ")

# Salary Calculations
annual_salary = float(monthly_salary) * 12
monthly_tax = float(monthly_salary) * 0.1  # 10% tax
annual_tax = monthly_tax * 12
net_annual_salary = annual_salary - annual_tax

# Employee Grade based on salary
if annual_salary >= 1000000:
    employee_grade = "Executive"
elif annual_salary >= 700000:
    employee_grade = "Senior"
elif annual_salary >= 500000:
    employee_grade = "Mid-level"
else:
    employee_grade = "Junior"

# Experience Category
employee_experience = input("Enter Employee Experience in years: ")
if int(employee_experience) >= 10:
    experience_category = "Expert"
elif int(employee_experience) >= 6:
    experience_category = "Experienced"
elif int(employee_experience) >= 3:
    experience_category = "Intermediate"
else:
    experience_category = "Beginner"

# Department Code based on employee department
department_codes = {
    "Information Technology": "IT",
    "Human Resources": "HR",
    "Finance": "FIN",
    "Operations": "OPS",
    "Sales": "SAL",
}
department_code = department_codes.get(employee_department, "N/A")

# Displaying Employee ID Card
print("==========================================\n")
print("        EMPLOYEE MANAGEMENT SYSTEM        \n")
print("==========================================\n")
print(f"ID: {employee_id}\n")
print(f"Name: {employee_name}\n")
print(f"Department: {employee_department} ({department_code})\n")
print(f"Experience: {employee_experience} years ({experience_category})\n")
print(f"Monthly Pay: INR{monthly_salary}\n")
print(f"Annual Pay: INR{annual_salary}\n")
print(f"Annual Tax: INR{annual_tax}\n")
print(f"Net Salary: INR{net_annual_salary}\n")
print(f"Designation: {employee_grade}\n")
print("==========================================\n")

# Bonus Eligibility Check
if float(monthly_salary) < 100000 and int(employee_experience) > 5:
    print("Note: Employee is eligible for a bonus.")
else:
    print("Note: Employee is not eligible for a bonus.")

# Saving the Employee Details to a File
save_details = input("Would you like to print the report? (Y/N): ")