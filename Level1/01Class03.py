# Inheritance
class Book(object):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def format_citation(self):
        return '%s written by %s \t goes for: $%s' % (self.title, self.author, self.price)

class Comic(Book):
    def __init__(self, title, author,illustrator, price):
        super().__init__(title, author, price)
        self.illustrator = illustrator
    def format_citation(self):
        return '%s written by %s and illustrated by %s \t goes for: $%s' % (self.title, self.author, self.illustrator, self.price)

ldr = Book("The Lord of the Rings", "JRR Tolkien", 24)
npa = Book("Nine Princes in Amber", "R Zelazny", 12)
dnr = Comic("The Dark night Rises", 'Stan Lee', 'Alex Von Bustral', 8)

# print(dnr.format_citation())
print('\t\tBook Details')

for x in (ldr, npa, dnr):
    print(x.format_citation())