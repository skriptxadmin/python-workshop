file = open("./names.txt", "r") #read mode only

content = file.read()

print(content) 

lines = file.readlines()

for line in lines:
    print(line)




file = open('example.txt', 'w')

file.write("Hello, World!")

lines = ["First line\n", "Second line\n", "Third line\n"]

file.writelines(lines)
