# Create a function that takes a number
# and returns its length.


def length_of_num(num):
    counter = 0

    for x in str(num):
        counter += 1

    return counter


print(length_of_num(2))
print(length_of_num(47385))
print(length_of_num(475))