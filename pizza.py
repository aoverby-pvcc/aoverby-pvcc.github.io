# Name: Anton Overby
# Prog Purpose: This program will take user input to display a receipt of a pizza order 

import datetime

prices_dict = {"S": 9.99, "M": 12.99, "L": 14.99, "X": 17.99}
SALES_TAX = .055

order_list = []
price_list = []

subtotal = 0
sales_tax = 0
total = 0

def main():
    get_user_input()
    do_math()
    display_results()

def get_user_input():
    global order_list
   
    another_pizza = True
    while another_pizza:
        order = input("What size pizza would you like?\nEnter from the following choices:\n\tS, M, L, X\n\tPizza Size: ")
        order = order.upper()
        order_list.append(order)
        yesno = input("\nWould you like another pizza? Y/N: ")
        if yesno.upper() != "Y":
            print("OK, great! Thanks for your order. Here's your receipt: ")
            another_pizza = False
        else:
            print("OK great! We would love to continue your order.")
            
def do_math():
    global order_list, price_list, prices_dict, SALES_TAX, subtotal, total, sales_tax

    for i in order_list:
        price_list.append(prices_dict[i])

    subtotal = sum(price_list)
    sales_tax = subtotal * SALES_TAX
    total = subtotal + sales_tax
    

def display_results():
    print('-----------------------------')
    print('********PALERMO PIZZA********')
    print('Your neighborhood pizza joint')
    if len(order_list) == 1:
        print(f'You ordered {len(order_list)} pizza:')
    else:
        print(f'You ordered {len(order_list)} pizzas:')
    print('-----------------------------')
    for i in order_list:
        print(f'{i} pizza   $       ' + f'{prices_dict[i]:8,.2f}')
    print('-----------------------------')
    print('Subtotal     $       ' + format(subtotal, '8,.2f'))
    print('Sales Tax    $       ' + format(sales_tax, '8,.2f'))
    print('Total        $       ' + format(total, '8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

main()