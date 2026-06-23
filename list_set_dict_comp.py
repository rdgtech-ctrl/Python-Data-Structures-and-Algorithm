# List comprehension provides a way to transform one list into another

numbers = [1,2,3,4,5,6,7]
even =[]
for i in numbers:
    if i % 2  == 0:
        even.append(i)
# or
even = [i for i in numbers if i%2 == 0]
print(even)

sqr = [i*i for i in numbers]
print(sqr)

# Set comprehensions
# set unordered collection of unique items
s = set([1,2,3,4,5,2,3])
print(s) #removes duplicates from s

even = { i for i in numbers if i % 2 == 0}
print(even)

cities = ['mumbai','new york','paris']
countries = ['india','usa','france']
zip = zip(cities,countries)
for a in zip:
    print(a)
 