#simple payment calculator for loan interest
#not perfect yet still works though

from sys import exit
import math

def main():

    borrowed, rate, term = 0,0,0 
    print("Welcome to the Loan Calculator!")
    print("Please input the following, or type exit at any time")
    while (borrowed or term or rate) != "exit":
        borrowed = input("Amount borrowed ($): ")
        rate = input("Interest rate (%): ")
        term = input("Term (years): ")
        if isinstance(borrowed,int) and isinstance(rate,int) and isinstance(term,int):
            break
        print("Please enter your values as integers.")
    if (borrowed or term or rate) == "exit":
        exit()
    if borrowed < 1000:
        print("Banks will not give approve a loan valued at less than $1,000.")
        main()
    interest = borrowed*rate*term
    interest /= 100
    
    print("\nAmmount Borrowed = $%.2f" % borrowed)
    print("Total Payment = $%.2f" % (interest + borrowed))
    calculatePayments((interest+borrowed),term)

def calculatePayments(total,term):
    payments = term*12
    paymentAmount = math.ceil(float(total)/payments)
    remaining = total
    printGrid(payments,paymentAmount,remaining)
    
    
def printGrid(payments,paymentAmount,remaining):
    count = 0
    print("\n\t\t\tAmount\t\tRemaining\n\tPymt#\t\tPaid\t\tBalance")
    print("\t-----\t\t------\t\t---------")
    while count <= payments:
        if remaining < paymentAmount:
            paymentAmount = remaining
            remaining -= paymentAmount
            print("\t%d\t\t$%.2f\t\t$%.2f" % (count,paymentAmount,remaining))
            if remaining == 0:
                break
        else:
            print("\t%d\t\t$%.2f\t\t$%.2f" % (count,paymentAmount,remaining))
        remaining -= paymentAmount
        count += 1

if __name__ == "__main__":
    main()
