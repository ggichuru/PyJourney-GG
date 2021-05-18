                        ## CHANGING LISTS ##
cars = ['Arston Martin', 'BMW', 'Toyota', 'Mercedes', 'Ferari']
print(f'This is the initial list of car: {cars}')

   # 1.append() - adding elements to an end of a list 
cars.append('Renault')
print(f'New List on append: {cars}')

   # 2.insert() - adding elements to any position
cars.insert(2, 'KIA')
print(f'New list on insert at index 2: {cars}')

   # 3.del - remove an item whose position you know.
del cars[0]
print(f'New list on del at index 0: {cars}')

   # 4.pop() - remove an item and store it for later user.
popped_car = cars.pop()                      # removes last element
print(f'The popped car is: {popped_car}')
print(f'New list on pop: {cars}')
first_to_arrive = cars.pop(0)                # pop item by index
print(f'The first car to arrive was: {first_to_arrive}')

   # 5.remove() - remove an item whose position is unkown using its value
         # remove only removes the first occurence, a loop is required to remove more than one occurence
cars.remove('Toyota')
print(f'New list on remove Toyota: {cars}')
print()


guests = ['George', 'Maina', 'Gichuru']                                         #Guest List
for g in range(len(guests)):
    print(f'Hello {guests[g]}, you are invited to a party')                     # print an invitation for each guest.
print()

print(f'Unfortunately, {guests[1]} will not be able to make it')
del guests[1]
guests.insert(1, 'Kimenyi')
for g in range(len(guests)):
    print(f'Hello {guests[g]}, you are invited to a party')     
print()

print('Good news all, a new table was found')
guests.insert(0, 'Carole')
guests.insert(2, 'Nduku')
guests.append('Katumo')
for g in range(len(guests)):
    print(f'Hello {guests[g]}, you are invited to a party')     
print()

print('Ooops! I can only invite 2 of you')
guests.pop()
guests.pop(4)
guests.pop(2)
guests.pop(1)
for g in range(len(guests)):
    print(f'Hello {guests[g]}, you are invited to a party')     
print()

del guests[0:]                                                              # Delete all elements from the list
print(guests)