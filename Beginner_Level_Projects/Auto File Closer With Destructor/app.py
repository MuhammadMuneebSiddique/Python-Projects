
class File:
    def __init__(self):
        self.file = open("text1.txt","w")

    def write(self,words):
        self.file.write(words)


    def __del__(self):
        self.file.close()


# f1 = File()
# f1.write("heelo dude")

# del f1

f1 = File()
f1.write("hello dude i am muneeb and i learn how destructor work")
f1.write("hello dude i am muneeb and i learn how destructor work")
del f1