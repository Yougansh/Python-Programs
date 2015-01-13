'''
Program for reading File
'''

f = open("test.txt", "r") #opens file with name of "test.txt" 

'''
print(f.read(1))
print(f.read())
'''

'''
print(f.readline())
print(f.readline()) 
'''

myList = []
for line in f:

    myList.append(line)

print(myList) 

f.close()
