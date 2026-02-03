# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

# syntax:
#   new_list = [expression for item in iterable if condition == True]

example = []

new_list = [x for x in example if "a" in x]

new_list = [x for x in range(10)]

new_list = [[p, s] for (p, s) in zip(example, example)]

new_list = ['hello' for x in example]

new_list = [x if x != "banana" else "orange" for x in example]