    ## IF STATEMENTS
x = int(input("Please enter an integer: "))

if x < 0:
     x = 0
     print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


 ## For Statements
#Measure some strings
cities = ['Nairobi', 'Onatanarivo', 'Dar']
for w in cities:
    print(w, len(w))
print()

   
#     # Code that modifies a collection while iterating over that same collection can be tricky to get right. 
#     # Instead, it is usually more straight-forward to loop over a copy of the collection 
#     # or to create a new collection:

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status


    ## Range function 
# Iterating over a sequence of numbers
for i in range(10):
    print(i, end=',')
print()

for i in range(5,10):
    print(i, end=',')
print()

for i in range(0, 10, 3):               # The three specifies a different increament 
    print(i, end=',')
print()

for i in range(-10, -100, -30):
    print(i, end=',')
print()

# Iterate over indices of a sequence - combine range() and len()
names = ['Mary', 'Matthew', 'Obadiah', 'James']
for i in range(len(names)):
    print(i, names[i])