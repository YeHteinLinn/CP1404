# Name Program
NAME_FILE = "name.txt"
name_file = open(NAME_FILE, 'w')
name = input("Enter your name : ")
print(name, file=name_file)
name_file.close()

name_file=open("name.txt", "r")
name=name_file.read().strip()
name_file.close()
print("Your name is", name)

# Number Program
NUMBERS_FILE = "numbers.txt"
numbers_file = open(NUMBERS_FILE, 'r')
first_line = int(numbers_file.readline())
second_line = int(numbers_file.readline())
result = first_line + second_line
print(result)

# Numebr program 2 (total)
total = 0
for line in numbers_file:
    number = int(line)
    total += number
numbers_file.close()
print(total)
