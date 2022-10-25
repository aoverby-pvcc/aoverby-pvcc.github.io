# Name: Anton Overby
# Prog Purpose: This program finds the cost of movie tickets 
# Price for one ticket: $10.99
# Sales tax rate: 5.5%

import datetime

# Define global variables
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# Define placeholder variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

# Define program functions
def main():
    get_user_data()
    perform_calculations()
    display_results()

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))
    

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-----------------------------')
    print('*****CINEMA HOUSE MOVIES*****')
    print('Your neighborhood movie house')
    print('-----------------------------')
    print('Tickets      $       ' + format(subtotal, '8,.2f'))
    print('Sales Tax    $       ' + format(sales_tax, '8,.2f'))
    print('Total        $       ' + format(total, '8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

# Call on main program to execute
main()