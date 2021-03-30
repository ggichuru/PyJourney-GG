def decorator(x):
    return '<<' + str(x) + '>>'

for c in 'HELLO':
    print(decorator(decorator(c)), end=' ')