# 1. Create a function to calculate finances
def calculate_finances(monthly_income, tax_rate, currency):

    # 2. Do the math for each field
    yearly_salary = monthly_income * 12
    monthly_tax = monthly_income * (tax_rate/100)
    yearly_tax = monthly_tax * 12
    monthly_net_income = monthly_income - monthly_tax
    yearly_net_income = yearly_salary - yearly_tax

    # 3. Format the calculated finances information for the user
    print('-----------------------------')
    print(f'Monthly Income: {monthly_income:,.2f} {currency}')
    print(f'Tax Rate: {tax_rate:,.0f}%')
    print(f'Monthly Tax: {monthly_tax:,.2f} {currency}')
    print(f'Monthly Net Income: {monthly_net_income:,.2f} {currency}')
    print(f'Yearly Salary: {yearly_salary:,.2f} {currency}')
    print(f'Yearly Tax Paid: {yearly_tax:,.2f} {currency} ')
    print(f'Yearly Net Income: {yearly_net_income:,.2f} {currency}')
    print('-----------------------------')

#calculate_finances(100, 20, '$')

# 4. Create a main entry point for the program
def main():
    # 5. To Gather user input
    monthly_income = float(input('Enter your monthly income: '))
    tax_rate = float(input('Enter your tax rate (%): '))
    # 6. Call the function
    calculate_finances(monthly_income, tax_rate, currency='RS')

if __name__ == '__main__':
    main()

