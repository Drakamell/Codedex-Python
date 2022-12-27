# Before we dive deep into the while loop, let's see a demo using a bank's ATM. 🏦

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

  if pin == 1234:
    print('PIN accepted!')