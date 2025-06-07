#!/usr/bin/python
import os

# creating lists of users, their PINs and bank statements
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0

print("="*50)
print("           WELCOME TO ATM SYSTEM")
print("="*50)

# while loop checks existence of the entered username
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        n = users.index(user)  # More efficient way to get index
        break
    else:
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# comparing pin
while count < 3:
    print('------------------')
    print('******************')
    pin = input('PLEASE ENTER PIN: ')
    print('******************')
    print('------------------')
    
    if pin.isdigit() and len(pin) == 4:
        if pin == pins[n]:
            break
        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            if count < 3:
                print(f'Attempts remaining: {3-count}')
            print()
    else:
        print('------------------------')
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        print('------------------------')
        count += 1
        if count < 3:
            print(f'Attempts remaining: {3-count}')

# in case of invalid pin after 3 attempts
if count == 3:
    print('-----------------------------------')
    print('***********************************')
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESSFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')    
print(f'{users[n].capitalize()} welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')

# Main menu
while True:
    print('\n' + '='*40)
    print('         ATM MAIN MENU')
    print('='*40)
    response = input('''SELECT FROM FOLLOWING OPTIONS:
[S] - Statement (Check Balance)
[W] - Withdraw Money
[L] - Lodgement (Deposit Money)
[P] - Change PIN
[Q] - Quit

Enter your choice: ''').lower()
    
    if response == 's':
        print('='*50)
        print(f'{users[n].capitalize()}, YOU HAVE {amounts[n]} EURO ON YOUR ACCOUNT.')
        print('='*50)
        
    elif response == 'w':
        try:
            cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: €'))
            
            if cash_out <= 0:
                print('ERROR: Amount must be greater than 0')
            elif cash_out % 10 != 0:
                print('ERROR: Amount must be in multiples of €10')
            elif cash_out > amounts[n]:
                print('ERROR: Insufficient balance')
                print(f'Your current balance: €{amounts[n]}')
            else:
                amounts[n] -= cash_out
                print('='*40)
                print('TRANSACTION SUCCESSFUL')
                print(f'Withdrawn: €{cash_out}')
                print(f'New Balance: €{amounts[n]}')
                print('='*40)
        except ValueError:
            print('ERROR: Please enter a valid number')
            
    elif response == 'l':
        try:
            cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: €'))
            
            if cash_in <= 0:
                print('ERROR: Amount must be greater than 0')
            elif cash_in % 10 != 0:
                print('ERROR: Amount must be in multiples of €10')
            else:
                amounts[n] += cash_in
                print('='*40)
                print('TRANSACTION SUCCESSFUL')
                print(f'Deposited: €{cash_in}')
                print(f'New Balance: €{amounts[n]}')
                print('='*40)
        except ValueError:
            print('ERROR: Please enter a valid number')
            
    elif response == 'p':
        new_pin = input('ENTER A NEW 4-DIGIT PIN: ')
        
        if new_pin.isdigit() and len(new_pin) == 4 and new_pin != pins[n]:
            confirm_pin = input('CONFIRM NEW PIN: ')
            
            if confirm_pin != new_pin:
                print('ERROR: PIN mismatch. Please try again.')
            else:
                pins[n] = new_pin
                print('='*30)
                print('PIN SUCCESSFULLY CHANGED')
                print('='*30)
        else:
            print('ERROR: New PIN must be 4 digits and different from current PIN')
            
    elif response == 'q':
        print('='*40)
        print('    THANK YOU FOR USING ATM')
        print('         HAVE A NICE DAY!')
        print('='*40)
        break
        
    else:
        print('ERROR: Invalid option. Please try again.')

print("Session ended.")
