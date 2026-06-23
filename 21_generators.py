# # Generator is a simply way of creating iterator
# def remote_control_next():
#     yield "cnn"
#     yield "espn"
# '''
# In Python, yield is used inside a function to create a generator.

# Instead of returning all values at once like return, yield produces values one at a time and remembers where it stopped.
# '''
# itr = remote_control_next()
# itr
# next(itr)

# fibonacci sequence using generators
def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

for f in fib():
    if f>50:
        break
    print(f)
    