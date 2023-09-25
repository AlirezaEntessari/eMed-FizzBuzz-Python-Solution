for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:   # checks for numbers that are multiples of 3 and 5
        print('FizzBuzz')
    elif num % 3 == 0:                  # checks for multiples of 3
        print('Fizz')
    elif num % 5 == 0:                  # checks for multiples of 5
        print('Buzz')
    else:                               # prints out the remaining numbers from 1 to 100
        print(num)