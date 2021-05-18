# # Slices
# word = "GeorgeGichuru"

# print(word[:3])  # character from position 0 (included) to position 3 (excluded)
# print(word[3:])  # from position 3 (included) to the end
# print(word[0:6])  # From position 0 (included) to position 6(excluded)
# print(word[-7:])  # From 7th last to end

# print("New to " + word[3:])  # create new string # output = New to rgeGichuru
# print("Oye" + word[-3:])  # output = Oyeuru

# Fibonnaci Series
    # The sum of two elements defines the next.
a, b = 0, 2
while a < 100:
    print(a, end=',')
    a, b = b, a+b
