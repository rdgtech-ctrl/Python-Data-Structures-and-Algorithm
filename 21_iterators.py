# next() is used to retrieve the next item from an iterator.

'''
Implement Remote Control Class that allows you to press "next" button to go to next TV channel
'''
class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","cnn","abc","espn"]
        self.index =-1 #when tv is off

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1 #first channel
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
    