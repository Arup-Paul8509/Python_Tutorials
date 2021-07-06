class myNum:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=5:
            n=self.a
            self.a+=1
            return n
        else:
            raise StopIteration
obj=myNum()
myiter=iter(obj)
for x in myiter:
    print(x)
'''
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''