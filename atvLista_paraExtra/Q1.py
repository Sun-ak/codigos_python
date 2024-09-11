#Se um número que esteja no intervalo de 1 a 50 for multiplo de 3 receberá Fizz, se for multiplo de 5 será Buzz e caso seja dos dois será FizzBuzz

for num in range(1,50 +1):
    if num % 3 == 0:
        print(f"{num} Fizz")
    elif num % 5 == 0:
        print(f"{num} Buzz")
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} FizzBuzz")    