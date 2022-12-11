import  random


def welcome():
    print('Welcome to Python')


def fruits_list():
    fruits = ["apple", "banana", "orange"]
    a, b, c = fruits
    print(a)
    print(b)
    print(c)


def random_number():
    print(random.randrange(1, 10))


def lists():
    colors = ["red", "white", "black"]
    fruits = ["apple", "mango", "orange"]

    for x in colors:
        for y in fruits:
            print(x, y)


welcome()
fruits_list()
random_number()
lists()