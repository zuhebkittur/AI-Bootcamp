employees = []

while True:

    print("\n" + "=" * 40)
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":

        employee_name = input("Enter Employee Name: ")
        employees.append(employee_name)

        print(f"{employee_name} added successfully!")

    elif choice == "2":

        print("\n------ EMPLOYEE LIST ------")

        if len(employees) == 0:
            print("No employees found.")
        else:
            for employee in employees:
                print(employee)

    elif choice == "3":
        search = input("Search for the employess: ")
        if search in employees:
            print("Employee Found")
        else:
            print("Employee Not Found")

        # print("Thank you for using Employee Management System.")
        # break
    elif choice == "4":
        delete = input("Enter Employee Name to delete: ")

        if delete in employees:
            employees.remove(delete)
            print("Employee Deleted Successfully!")
        else:
            print("Employee Not Found!")
    
    elif choice == "5":

        old_employee = input("Enter Old Employee Name: ")

        if old_employee in employees:

            new_employee = input("Enter New Employee Name: ")

            index = employees.index(old_employee)

            employees[index] = new_employee

            print("Employee Updated Successfully!")

        else:
            print("Employee Not Found!")

        print("Invalid Choice. Please try again.")