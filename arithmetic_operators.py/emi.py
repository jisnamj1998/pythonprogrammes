loan_amount=200000
interest_rate=9
tenure_in_yrs=20
#monthly emi
#total interest payable
#total payment (principal+interest)
tenure_in_months=tenure_in_yrs*12
interest_rate_monthly=interest_rate/(100*12)
monthly_emi=(loan_amount*interest_rate_monthly*(1+interest_rate_monthly)**tenure_in_months)/((1+interest_rate_monthly)**tenure_in_months-1)
print(monthly_emi)
total_interest_payable=loan_amount*interest_rate*tenure_in_yrs/100
print(total_interest_payable)
total_payment=loan_amount+total_interest_payable
print(total_payment)

