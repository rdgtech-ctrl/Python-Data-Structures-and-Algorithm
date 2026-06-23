'''
(a) What was the avg temp in first week of Jan
'''

arr = []
with open("nyc_weather.csv",'r') as f:
    for line in f :
        tokens = line.split(',')
        try:
            temperature =  int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temprature.Ignore the row")



'''
The enumerate() function in Python adds a counter to an iterable (like a list, tuple, or string) and returns both the index and the value as you loop through it.

'''