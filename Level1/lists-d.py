## NUMERICAL LISTS
for value in range(1, 5):
    print(value)
print()
for no in range(5):
    print(no)
print()

## use Range() to make a numerical list
numbers = list(range(1,6))
print(f'List of numbers of range 1,6: {numbers}\n')
## using 3 arguments in range as a step size | Sequence, third range defines the step
even_numbers = list(range(2,11,2))
print(f'List of even numbers from 1-10: {even_numbers}\n') #starts from two and adds two till it gets to 10

#Make a list of the first 10 square numbers | square of each number from 1 - 10
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(f'List of squares of each number from 1-10: {squares}\n')

print(f'Sum of squares: {sum(squares)}')
print(f'Minimum in squares: {min(squares)}')
print(f'Maximum in squares: {max(squares)}\n')

## List Comprehension
squares = [value**2 for value in range(1,11)]
print(f'List of squares of each number from 1-10: {squares} \t (using list comprehension)\n')

numbers = [number*3 for number in range(1,20)]
print(numbers)
print()

## Try it yourself
number_mil = [value for value in range(1,1000001)]
print(f'Sum: {sum(number_mil)}')
print(f'Minimun: {min(number_mil)}')
print(f'Maximum: {max(number_mil)}\n')

#2 Odd number 0-20
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number)
print()

#3 multiples of 3 from 3-30
threes = [number for number in range(3,31,3)]
print(f'Multiple of 3 from 3-30: {threes}\n')

#4 First ten cubes 
cubes = [cube**3 for cube in range(1,11)]
print(f'First 10 cubes: {cubes}\n')