# ========================================
# MONTHLY SALARY REPORT
# ========================================

print("=" * 40)
print("MONTHLY SALARY REPORT")
print("=" * 40)

employee_name = input("Enter Employee Name: ")
company_name = input("Enter Company Name: ")

monthly_salary = 50000
total_expenses = 30000

remaining_salary = monthly_salary - total_expenses

saving_percentage = (remaining_salary / monthly_salary) * 100

print()

print("Employee Name :", employee_name)
print("Company Name :", company_name)
print("Monthly Salary : ₹", monthly_salary)
print("Total Expenses : ₹", total_expenses)
print("Remaining Salary : ₹", remaining_salary)
print(f"Savings Percentage : {saving_percentage:.2f}%")

print()

if saving_percentage > 30:
    print("Excellent Savings!")

elif saving_percentage >= 15:
    print("Good Job!")

else:
    print("Need to Save More!")