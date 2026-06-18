heros=['spider man','thor','hulk','iron man','captain america']
# Length of the list
'''
print(len(heros))
'''
# Add 'black panther' at the end of this list
'''
heros.append('black panther')
'''
#  You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
'''
heros.insert(2,"black panther")
print(heros)
heros.pop(2)
print(heros)
heros.insert(3,"black panther")
print(heros)
'''
#    Do that with one line of code.
# Now you don't like thor and hul d because they get anygry easily :)    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). 
'''
heros[1:3] = "doctor strange"
print(heros)
'''
# 5. Sort the list in alphabetical order
'''
heros.sort()
print(heros)
'''
# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''
max = int(input('Enter a max number: '))
lst = []
for ele in range(1,max):
    if ele % 2 == 0:
        lst.append(ele)
print(lst)
'''
