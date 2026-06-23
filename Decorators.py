import time

def time_it(func):
    # functions are first class object in Python. What it means is that they can be treated just like any other variable and you can pass them as argument to another function or even return them as a return value
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + "mili seconds")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    start = time.time()    
    result = []
    for number in numbers:
        result.append(number**2)
    end = time.time()
    print("calc_square took " + str((end-start)*1000) + "mili sec")
    return result

@time_it
def calc_cube(numbers):
    start = time.time()    
    result = []
    for number in numbers:
        result.append(number**3)
    end = time.time()
    print("calc_square took " + str((end-start)*1000) + "mili sec")
    return result

array = range(1,100000)
out_square =  calc_square(array)
out_cube = calc_cube(array)

# Decorators = wrap your function to another function