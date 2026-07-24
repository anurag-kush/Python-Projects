# EMS v2.py

# Master employee list to store all employee records.
# Each record is stored as a nested list containing: [ID, Name, Department, Age, Salary, Experience]
employees = []

# Function to calculate the employee's grade based on their monthly salary.
# Returns a string indicating their grade (Executive, Senior, Mid-Level, or Junior).
def calculate_grade(monthly_salary):
    if monthly_salary >= 100000:
        return "Executive"
    elif monthly_salary >= 70000:
        return "Senior"
    elif monthly_salary >= 50000:
        return "Mid-Level"
    else:
        return "Junior"

# Function to calculate the employee's experience level based on their years of experience.
# Returns a string representing their experience category.
def calculate_experience(years):
    if years >= 10:
        return "Expert"
    elif years >= 6:
        return "Experienced"
    elif years >= 3:
        return "Intermediate"
    else:
        return "Beginner"

# Function to display the main menu options to the user and prompt for their choice.
# Returns the user's input choice as a string.
def display_menu():
    print("\n==================================")
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("==================================")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Calculate Payroll Summary")
    print("5. Exit")
    
    choice = input("\nEnter your choice: ")
    return choice

# Function to handle adding a new employee to the system.
# Prompts the user for all necessary employee details and appends them to the master list.
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Monthly Salary: "))
    experience = int(input("Enter Years of Experience: "))
    
    # Store the employee details as a list inside the main 'employees' list
    employees.append([emp_id, name, dept, age, salary, experience])
    print(f"Employee {name} added successfully!")

# Function to display all employees currently in the system.
# It iterates through the master list and prints formatted details for each employee.
def view_employees():
    # Check if the list is empty first
    if len(employees) == 0:
        print("No employees found.")
        return
        
    # Use enumerate to display a numbered list of employees
    for index, emp in enumerate(employees, start=1):
        print(f"\n{index}.")
        print(f"ID : {emp[0]}")
        print(f"Name : {emp[1]}")
        print(f"Department : {emp[2]}")
        print(f"Age : {emp[3]}")
        print(f"Monthly Salary : {emp[4]}")
        print(f"Experience : {emp[5]} Years")
        # Bonus: Displaying grade and experience level dynamically
        print(f"Grade : {calculate_grade(emp[4])}")
        print(f"Experience Level : {calculate_experience(emp[5])}")
        print("----------------------")

# Function to search for a specific employee by their ID.
# Iterates through the list and displays the details if a match is found.
def search_employee():
    search_id = int(input("Enter Employee ID to search: "))
    found = False
    
    # Loop through each employee in the master list
    for emp in employees:
        if emp[0] == search_id:
            print("\nEmployee Found:")
            print(f"ID : {emp[0]}")
            print(f"Name : {emp[1]}")
            print(f"Department : {emp[2]}")
            print(f"Age : {emp[3]}")
            print(f"Monthly Salary : {emp[4]}")
            print(f"Experience : {emp[5]} Years")
            print(f"Grade : {calculate_grade(emp[4])}")
            print(f"Experience Level : {calculate_experience(emp[5])}")
            found = True
            # Stop searching once the employee is found
            break
            
    # If the loop finishes and 'found' is still False
    if not found:
        print("Employee not found.")

# Function to calculate and display various payroll and employee statistics.
# Includes total employees, payroll costs, salary extremes, averages, and bonus challenges.
def payroll_summary():
    # Check if there are any employees to process
    if len(employees) == 0:
        print("No employees to calculate payroll.")
        return
        
    total_employees = len(employees)
    
    # Calculate total monthly payroll by summing all salaries
    total_monthly_payroll = 0
    for emp in employees:
        total_monthly_payroll += emp[4]
        
    # Annual payroll is simply the monthly payroll multiplied by 12 months
    total_annual_payroll = total_monthly_payroll * 12
    
    # Initialize variables for finding the highest and lowest salaries
    highest_salary = employees[0][4]
    lowest_salary = employees[0][4]
    highest_paid_employee = employees[0][1]
    
    # Loop through employees to find the highest and lowest salaries
    for emp in employees:
        if emp[4] > highest_salary:
            highest_salary = emp[4]
            highest_paid_employee = emp[1] # Bronze Bonus tracking
        if emp[4] < lowest_salary:
            lowest_salary = emp[4]
            
    # Calculate the average salary
    average_salary = total_monthly_payroll / total_employees
    
    # Display the primary payroll summary
    print("\n--- Payroll Summary ---")
    print(f"Total Employees : {total_employees}")
    print(f"Monthly Payroll : ₹{total_monthly_payroll}")
    print(f"Annual Payroll : ₹{total_annual_payroll}")
    print(f"Highest Salary : ₹{highest_salary} (Highest Paid: {highest_paid_employee})")
    print(f"Lowest Salary : ₹{lowest_salary}")
    print(f"Average Salary : ₹{average_salary}")
    
    # Silver Bonus Challenge: Display employees with more than 5 years of experience
    print("\n--- Employees with > 5 years of experience ---")
    experienced = False
    for emp in employees:
        if emp[5] > 5:
            print(f"- {emp[1]} ({emp[5]} years)")
            experienced = True
    if not experienced:
        print("No employees have more than 5 years of experience.")
            
    # Gold Bonus Challenge: Sort and display employees alphabetically by their name
    print("\n--- Employees Sorted Alphabetically ---")
    # Using sorted() with a lambda function that extracts the employee's name (index 1) for sorting
    sorted_employees = sorted(employees, key=lambda emp: emp[1])
    for emp in sorted_employees:
        print(f"- {emp[1]}")

# Main execution function to run the application in an infinite loop.
# It continually displays the menu and delegates tasks based on user input.
def main():
    while True:
        choice = display_menu()
        
        # Route the user's choice to the corresponding function
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            payroll_summary()
        elif choice == '5':
            print("Exiting Employee Management System. Goodbye!")
            break # Exit the infinite loop
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script: Call the main function to start the application
if __name__ == "__main__":
    main()