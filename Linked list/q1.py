'''
In LinkedList class that we implemented in our tutorial add following two methods,
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
Now make following calls,

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

    '''

# SOLUTION
class Node:
    def __init__(self,data):
        self.data = data # Store the value
        self.next = None # Initially,no connection to next node


'''
CREATE THE LINKEDLIST CLASS
The LinkedList class manages all the nodes together. It provides methods to :
- Insert values
- Remove values
- Search for values
- Display the list

The LinkedList track of :
- head: Points to the first node in the chain
- Methods : Function to manipulate the list
When a LinkedList is created, it's empty:
l1 = LinkedList()
l1.head = None (no nodes yet)
'''

class LinkedList :
    def __init__(self):
        self.head = None 

'''
INSERT MULTIPLE VALUES AT ONCE
Purpose: Take a Python lilst and convert it into a linked list

Parameters:
-data_list: A python list like ['banana','mango','grapes','orange]

How it works:
1.Reset self.head = None to clear any exisiting list
2. Loop through each item in data_list
3. Call insert_end() for each item to add it to the end

'''

def insert_values(self,data_list):
    self.head = None # clear the list first

    # Loop through each value in the list
    for data in data_list:
        self.insert_end(data)

'''
STEP 4 : INSERT A SINGLE VALUE AT THE END
Exaplanation of insert_end():

Purpose: Add a new value to the end of the linked list

Parameters:
-data: The single value to add

Two Cases:

CASE 1: List is empty ( head is None)

Before: head = None
Call:   insert_end("banana:)
After:  head -> [banana|None]

Action: Create new node and make it the head

Code Logic: 
    if self.head is None:
        self.head = None(data)
        return

CASE 2 : List already has nodes

Before:     head -> [banana|next] -> [mango|None]
Call:   insert_end("grapes")
After:  head -> [banana|next] -> [mango|next] -> [grapes|None]

Action:
1. Start from head
2. Traverse to the last node (find the node where next is None)
3. Create a new node
4. Connect last node to new node

Code Logic:
    current = self.head         # Start from head
    while current.next:         # Loop while next exists
        current = current.next  # Move to next node
    current.next = Node(data)   # Connect last node
                                 to new node
'''

def insert_end(self,data):
    #Case 1: If list is empty
    if self.head is None:
        self.head = Node(data)
        return
    
    # Case 2: If list has at least one node
    current = self.head     # Start from head

    # Traverse to find the last node
    # Loop continues while current.next is NOT NONE
    # When loop exists,current is the last node
    while current.next:
        current = current.next # Jump to nex node

    # None
    current.next = Node(data)

'''
STEP 5: INSERT AFTER A SPECIFIC VALUE *** NEW METHOD ***

Purpose: Find a node with specific value, insert new value right after it

'''