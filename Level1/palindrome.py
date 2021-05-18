                   #### Using WHILE Loop ####

                    ## NUMBER PALINDROME ##
number = int(input("Enter any Number: "))       # prompt user for input

temp = number                                   # Store the inputed number
reverse_num = 0                                 # Calculate the reverse of this number

while(number > 0):                                 
    digit = number % 10                         # Extract the last digit of this number
    reverse_num = reverse_num*10 + digit        # Append this digit in the reversed number.
    number = number//10                         # Floor divide the number leaving out the last digit                             

if (temp == reverse_num):                       # Compare reverse to original number
    print('This Number is a palindrome')

else:
    print('This Number is not a palindrome')


                    ## STRING PALINDROME ##
def check_palindrome(name):
    length = len(name)
    first = 0
    last = length - 1
    status = 1

    while(first < last):
        if(name[first] == name[last]):
            first = first + 1
            last = last - 1
        else:
            status = 0
            break
    return int(status)

name = input('\nEnter the string: ')
print('Method 1')

status = check_palindrome(name)
if(status):
    print('The string is a palindrome')
else:
    print('This string is not a palindrome')


                        ## Using REVERSE FUNCTION ##

def check_palindrome_1(name):
    reverse_string = name[::-1]
    status = 1

    if(name != reverse_string):
        status = 0
    return status

name = input('\nEnter the string: ')
print('Method 2')

status = check_palindrome_1(name)
if(status):
    print('The string is a palindrome')
else:
    print('This string is not a palindrome')