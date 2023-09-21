#George Paul Robert, ID: 117928226

#list
numbers = [1,2,3,4,5,6,7,8,9,10]

#set
colors = {'red', 'green', 'blue', 'yellow', 'purple'}

#dictionary
scores = {"Alice": 85,
          "Bob": 90,
          "Alicia" : 75}

#List Comprehension
squared = list(map(lambda x: x**2, numbers))
print("Squared list:", squared)

#Dictionary Comprehension
modified_values = map(lambda x: x + 5 ,scores.values())
modified_dict = dict(zip(scores.keys(), modified_values))
print("Dictionary with scores +5: ", modified_dict)

#Set Comprehension
modifiedColors =  set(map(lambda x: x.upper(), colors))
print("Set with colors in upper case:", modifiedColors)

#list comprehension (Filtering)
evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
print("List with even numbers only: ", evenNumbers)

#Dictionary Comprehension
above80 = filter(lambda x: x if x > 80 else None, scores.values())
above80_dict = dict(zip(scores.keys(), above80))
print("Scores above 80:", above80_dict)

