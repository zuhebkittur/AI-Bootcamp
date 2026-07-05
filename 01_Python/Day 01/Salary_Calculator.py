# ⬜ Ask for Employee Name
# ⬜ Ask for Company Name
# ⬜ Ask for Monthly Salary
# ⬜ Ask for Monthly Rent
# ⬜ Ask for Monthly Food Expense
# ⬜ Ask for Monthly Travel Expense
# ⬜ Calculate Total Expenses
# ⬜ Calculate Remaining Salary
# ⬜ Calculate Savings Percentage
# ⬜ Print a Salary Report
# ⬜ Display a message using if, elif, else

employee_name = input("Enter the Employee Name: ")
company_name = input("Enter the Company Name: ")
monthly_salary = int(input("Enter you Monthly Salary: "))
monthly_rent = int(input("Enter your Monthly Rent: "))
monthly_food_expense = int(input("Enter your Monthly Food Expense: "))
monthly_travel_expense = int(input("Enter the Monthly Travel Expense: "))
month_saving = int(input("How many months you want to save: "))

total_expense = monthly_rent + monthly_food_expense + monthly_travel_expense
remaining_salary = monthly_salary - total_expense
saving_percentage = (remaining_salary / monthly_salary) *100
total_savings = remaining_salary * month_saving


print("=" *40)
print("Salary Report")
print("=" *40)

print("\n-------------")

print("Employee Name: ", employee_name)
print("Company Name: ", company_name )

print("\n-------------")

print("Monthly Salary: ", monthly_salary )
print("Total Expense: ", total_expense )
print(f"Savings Percentage: {saving_percentage:.2f}%")
print("Remaining Salary: ", remaining_salary)
print(f"Your total saving for the:{month_saving}:{total_savings} ")
if saving_percentage >30:
    print("You had done good savings")
elif saving_percentage > 15:
    print("You can save more")
else:
    print("You had saved very less")