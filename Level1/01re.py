name = "Antony Bridget Charlie Devin Grace Edwin"
print(name.split())
name = name.replace('grand', 'papas')
print(name)

nameslist = name.split()
print(nameslist)

# namesdict = {
#     'FNAME': 'Alex', 'LNAME': 'Githeko', 'other': {
#         'DOB': '23/12/2002', 'GENDER': 'Male'
#     }}
namesdict = {}
namesdict['name'] = 'Gaudentia Kituno'
namesdict['age'] = 24
namesdict['eligible'] = True
namesdict['relatives'] = nameslist
print(namesdict)

namesdict['name'] = 'Prince Odjeduka'
print(namesdict)

namesdict['education'] = {'Primary School': {'Schools': {'Kirugu', 'DEB Karatina', 'Gachugu', 'QOP'},'Grade': 'A-' }, 'High School': {'Schools': 'Kanjuri', 'Grade': 'B+'} }
print(namesdict['education']['High School']['Grade'])

del namesdict['education']['Primary School']['Schools']
print(namesdict)
# namesdict.clear()
# print(namesdict)

newdict = namesdict.copy()
print('\nNew dict: ',newdict)

# pop_el = newdict.popitem()
# print('Dict after delition: \n', str(newdict), '\nDeleted Element\t', str(pop_el))

print(newdict.keys())