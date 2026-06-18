# question 1

# question 2
'''
total_expenses = 0
for i in range (0,3):
    total_expenses += expenses[i]

print(total_expenses)
'''

# question 3 
'''
yeah = False
for i in range (len(expenses)):
    if (expenses[i] == 2000):
        yeah = True
    
if (yeah == True):
    print("Yeah")
else:
    print("nope")
'''
expenses = [2200,2350,2600,2130,2190]

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
'''
expenses.append(1980)
print(expenses)
'''
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
'''
april_expense = expenses[3] - 200
expenses.insert(3,april_expense)
print(expenses)
'''
