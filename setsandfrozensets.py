# # Set is an [unordered collection] of [unique elements]

# basket = {"orange","apple","mango","apple","orange"}
# print(type(basket))

# a=set()
# a.add(1)
# a.add(2)
# a.add(3)
# a.add(4)
# print(a)
# # set doesn't allow list operations because they are unique but list does
# numbers = [1,2,3,4,2,3,4]
# unique_nubmers=set(numbers)
# # frozen set : doesn't need to change the content of the set
# fs = frozenset(numbers)
# print(fs)
# fs.add(5) # doesn't allow elements to add

x = {'b','c','a'}
y={'a','g','h'}
# Union
print(x|y)
# intersection
print(x&y)
# Difference
print(x-y)
# x is subset of y
print(x<y)
x = {'a','g'}
# yes x is not the subset of y
print(x<y)
