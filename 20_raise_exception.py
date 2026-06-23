'''
try:
    # MemoryError was a class derived from the Exception class if we replace it with it's parent class no issue will be there
    raise Exception("memory error")
except Exception as e:
    print(e)
'''

'''
# exception are instance of classes

class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("User defined exception: ",self.msg)

try:
    raise Accident('some accident occured')
except Accident as e:
    e.print_exception()
    '''

def process_file():
    try:
        f = open("c:\\code\\data.txt")
        x = 1/0
    except FileNotFoundError as e:
        print('inside except')
    finally:
        print("cleaning up file")
        f.close() #neccessary cleanup of the file


process_file()