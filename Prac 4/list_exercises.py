def main():
    #1 - Numbers
    numbers = []
    for i in range(5):
        number=int(input("Number {} : ".format(i+1)))
        numbers.append(number)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

    #2 - Username

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("\nEnter the username :")
    if username in usernames:
        print("Acess granted")

    else:
        print("Access denied")

if __name__ == '__main__':
    main()