customer_name = input("Enter the Customer Name: ")
monthly_salary = int(input("Enter the Monthly Salary: "))
credit_score = int(input("Enter your credit score: "))
loan_amount = int(input("How much do you want the loan?: "))


print("=" * 40)
print("LOAN ELIGIBILITY REPORT")
print("=" * 40)

print(f"Customer Name : {customer_name}")
print(f"Monthly Salary : ₹{monthly_salary}")
print(f"Credit Score : {credit_score}")
print(f"Loan Amount Requested : ₹{loan_amount}")

print("-" * 40)
maximum_loan = monthly_salary *10

if monthly_salary >=25000 and credit_score >= 750 and loan_amount <= maximum_loan:
    print("Loan Accepted")
else:
    print("Loan Rejected")



