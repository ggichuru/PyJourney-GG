# new_files = open('/mnt/EC22DD0E22DCDF20/Eeggor/Eeggor Codes/Github Repositories/PyJourney-GG/Level1/palindrome.txt', 'r+')
# # new_files.write('JAKU')
# print(new_files.read())
# new_files.close()

from os import environ


numb = [1,2,3]

numb_even = []
for i in numb:
    numb_even.append(2 * i)
print(numb_even)

even_numb = [2*i for i in numb]
print(even_numb)

# Looping through several lists
#unpaired lists
animals = "zebra leopard hippo".split()
# animals = animals.split()
environments = "savanna forest river".split()
print(animals , environments)

for animal in animals:
    for env in environments:
        print('a', animal, 'in the', env)

# Paired two by two
for animal, env  in zip(animals, environments):
    print('a', animal, 'lives in the', env)

print()

#Functions
def remainders(x):
    if(x % 2 == 0):
        return (x, 'is an even number')
    else: 
        return (x, 'is an odd number')    
print(remainders(562 + 56123 * 83 / 24 *89 +45 *2 / 23))



def learn_args_kargs(*args, **kargs):
    print(args, kargs)
    return
print(learn_args_kargs(1,2,3,4, extra_name = 5, name='akex'))

print()
class Book(object):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def format_citation(self):
        return '%s by %s \t price: € %s' % (self.title, self.author, self.price)

ldr = Book("The Lord of the Rings", "JRR Tolkien", 24)
npa = Book("Nine Princes in Amber", "R Zelazny", 12)

print(ldr.format_citation())