# fizzbuzz
try:
    x = int(input('Up to which number shall I count fizzbuzz? '))
except ValueError:
    print('That aint number!')
    
for i in range(1,x,1):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} FizzBuzz')
    elif i % 3 == 0:
        print(f'{i} Fizz')
    elif i % 5 == 0:
        print(f'{i} Buzz')
    else:
        print(i)
input('Press anything to end. ')