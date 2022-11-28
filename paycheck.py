# Name: Anton Overby
# Prog Purpose: To calculate and display employee gross pay, deductions and net pay for different types of salaries and hours worked.

import datetime
now = datetime.datetime.now()


job_abbrev = {"C": "Cashier", "S": "Stocker", "J": "Janitor", "M": "Maintenance"}
pay_rates = {"Cashier": 16.50, "Stocker": 15.75, "Janitor": 15.75, "Maintenance": 19.50}

fed_inc = 0.12
state_inc = 0.03
soc_sec = 0.062
medicare = 0.0145

emp_code = 0
hours = 0

gross = 0
fed_ded = 0
state_ded = 0
ss_ded = 0
med_ded = 0
total_ded = 0
net_pay = 0

def get_user_input():
    global emp_code, hours
    emp_code = str(input("WELCOME TO PAYCHECK GENERATOR 5000\n\nWhat type of employee? Choose from the selections below: \n\tC - Cashier\n\tS - Stocker\n\tJ - Janitor\n\tM - Maintenance\n").upper())

    hours = int(input("Number of hours worked: "))


def calc_paycheck():
    global emp_code, hours, gross, fed_inc, fed_ded, state_inc, state_ded, soc_sec, ss_ded, medicare, med_ded, total_ded, net_pay
    job = job_abbrev[emp_code]
    hourly_pay = pay_rates[job]
    gross = hourly_pay * hours
    fed_ded = gross * fed_inc
    state_ded = gross * state_inc
    ss_ded = gross * soc_sec
    med_ded = gross * medicare
    total_ded = fed_ded + state_ded + ss_ded + med_ded
    net_pay  = gross - total_ded

def display_results():
    global hours, gross, fed_ded, state_ded, ss_ded, med_ded, total_ded, net_pay
    print('-----------------------------------')
    print('******PAYCHECK GENERATOR 5000******')
    print('***** Fresh Food Marketplace ******')
    print('-----------------------------------')
    print(f"{'Job Title:':<20} {job_abbrev[emp_code]:>12}")
    print(f"{'Hours worked:':<20} {hours:>12}")
    print('-----------------------------------')
    print(f"{'Gross pay:':<20} ${gross:>12,.2f}")
    print(f"{'Federal Deduction:':<20} ${fed_ded:>12,.2f}")
    print(f"{'State Deduction:':<20} ${state_ded:>12,.2f}")
    print(f"{'SS Deduction:':<20} ${ss_ded:>12,.2f}")
    print(f"{'Medicare Deduction:':<20} ${med_ded:>12,.2f}")
    print(f"{'Total Deductions:':<20} ${total_ded:>12,.2f}")
    print('-----------------------------------')
    print(f"{'Net Pay:':<20} ${net_pay:>12,.2f}")
    print('-----------------------------------')
    print('Date and Time: ' + now.strftime("%m-%d-%Y %H:%M:%S"))
    print('-----------------------------------')
    

def main():
    another_employee = True
    while another_employee:
        get_user_input()
        calc_paycheck()
        display_results()
        yesno = input("\nWould you like to calculate a paycheck for another employee? (Y/N): ")
        if yesno.upper() == "N":
            another_employee = False 
  
main()    


