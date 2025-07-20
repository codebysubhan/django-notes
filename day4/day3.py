from random import randint
# set and frozen sets
def set_implementation():
    my_set = set()
    for i in range(100):
        my_set.add(randint(1, 10))
    print(my_set)

set_implementation()