while True:
    number_1 =int(input("type your first number: "))
    if number_1 == 0:
        break
    else:
        number_2 =int(input("type your second number: "))

if number_1 == number_2:
    print(f'{number_1}is equal to {number_2}')
elif number_1 > number_2:
    print(" Number 1 is bigger than number 2!")
else:
    print(" Number 2 is bigger than number 1!")