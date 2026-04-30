# #import time
# # file_object =open(filename, mode)
# my_file = open("README.md","r")
# data = my_file.read()
# print(data)
# my_file.close()

# #time.sleep(10)
try:
    file_name = "README1.md"
    with open(file_name,"r") as f: # file
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"Error: File {file_name} Not Found!")

note_name = "note.txt"

with open(note_name, "w") as f:
    f.write("Hello, this is my first note!")

for i in range(10):

    with open(note_name, "a") as f:
        f.write(f"\n{i} : this is a new line")

with open(note_name, "r") as f:
    for line in f:
        print(line.strip())

# w+ write and read

# r+ read and write
with open(note_name, "r+") as f:
    data = f.read()
    f.write("\nNew Data")

with open("new_"+note_name, "w+") as f:

    f. write("New Note file.")
    f.seek(0)
    print(f.read())

with open(note_name , "r") as f:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()
    
    print(line1)
    print(line2)
    print(line3)

with open(note_name , "r") as f:
    print(f.readlines())

