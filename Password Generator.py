import random
print('Welcome to our Password Generator')
print('=================================')
 
chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789'

number =int(input('Amount of Password generate: '))


length =int(input('Enter the length of Password Generate: '))

print('\nHere is your Password')
for pwd in range(number):
    Passwords =''
    for c in range(length):
        Passwords += random.choice(chars)
    print(Passwords)

   