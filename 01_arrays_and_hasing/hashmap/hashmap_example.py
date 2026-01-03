# creating dictionary
dictionary_capitals = {'Madrid': 'Spain', 'Lisboa': 'Portugal', 'London': 'United Kingdom'}

# Search in a dictionary 
print(dictionary_capitals['Madrid'])
print(dictionary_capitals.get('Madrid'))

# Adding and deleting values in a dictionary
dictionary_capitals['Berlin'] = 'Italy' # adding a new key-value pair

# dictionary_capitals.clear()

# iterate over key-value pairs
for key, value in dictionary_capitals.items():
  print('the capital of {} is {}'.format(value, key))

print(dictionary_capitals.keys())
print(dictionary_capitals.values())


# defaultdict
from collections import defaultdict

capitals = defaultdict()
capitals['Madrid'] = 'Spain'
# print(capitals['Ankara']) # KeyError: 'Ankara'

#counter
from collections import Counter
c1 = Counter(['aaa', 'bbbb', 'ccccc', 'aaa'])

for item, count in c1.items():
   if count == 2:
      print(item)
      