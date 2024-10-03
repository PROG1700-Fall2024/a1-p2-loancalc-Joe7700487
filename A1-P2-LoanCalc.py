#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    #define variables
    loan = float(input("Enter loan amount: "))
    rate = float(input("Enter interest rate: "))
    years = int(input("Enter number of years: "))

    #calculate the weekly payment
    interest = rate / 5200
    weeklyPayment = interest / (1 - ((1 + interest) ** (-52 * years))) * loan

    #print the weekly payment
    print("Your weekly payment will be: ${0:.2f}".format(weeklyPayment))
main()