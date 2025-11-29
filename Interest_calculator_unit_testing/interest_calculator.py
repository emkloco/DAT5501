def compound_interest_calculator(savings_amount, annual_interest_rate, number_of_years):
    # convert the interest rate from a percentage (e.g., 5) to a decimal (e.g., 0.05)
    rate_decimal = annual_interest_rate / 100
    current_savings = savings_amount

    # loop through each year to calculate and print the new value
    print(f"starting balance: ${savings_amount:.2f}")
    
    for year in range(1, number_of_years + 1):
        # apply the interest formula for the current year
        current_savings = current_savings * (1 + rate_decimal)
        
        # print the value for this specific year rounded to 2 decimal places
        print(f"year {year}: ${current_savings:.2f}")

    # now we calculate how long it takes to double
    # we use a separate loop for this in case it takes longer than the 'number_of_years' input
    double_goal = savings_amount * 2
    temp_balance = savings_amount
    years_to_double = 0

    while temp_balance < double_goal:
        temp_balance = temp_balance * (1 + rate_decimal)
        years_to_double += 1

    # print the doubling result
    print(f"\nit takes {years_to_double} years for the savings amount to double.")
    
    # returning this value so we can unit test it
    return years_to_double

# EXAMPLE USAGE – change the numbers below to whatever you want
if __name__ == "__main__":
    savings = 500  
    rate = 6        
    years = 20      
    compound_interest_calculator(savings, rate, years)