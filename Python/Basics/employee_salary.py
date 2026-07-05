employee_name = input("Enter Employee Name: ")
company_name = input("Enter Company Name: ")

monthly_salary = int(input("Enter Monthly Salary: "))
monthly_rent = int(input("Enter Monthly Rent: "))
monthly_food_expense = int(input("Enter Monthly Food Expense: "))
monthly_travel_expense = int(input("Enter Monthly Travel Expense: "))

remaining_salary = (
    monthly_salary
    - monthly_rent
    - monthly_food_expense
    - monthly_travel_expense
)

saving_percentage = (remaining_salary / monthly_salary) * 100

print("=" * 40)
print("MONTHLY SALARY REPORT")
print("=" * 40)

print("Employee Name :", employee_name)
print("Company Name :", company_name)
print("Remaining Salary : ₹", remaining_salary)
print(f"Savings Percentage : {saving_percentage:.2f}%")