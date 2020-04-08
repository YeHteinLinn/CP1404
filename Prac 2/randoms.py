import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print(random.randint(1, 101))

'''Question 1: On the first try, line 1 gave me 19. Smallest we can get is 5 and largest we can get is 19
    Question 2: On the first try, line 2 gave me 5. Smallest we can get is 3 and largest we can get is 9. It will not produce 4 since it is specified to produce 3 or 5 or 7 or 9.
    Question 3: On the first try, line 3 gave me 5.347364969596523. Smallest we can get is 2.500000000000000 and largest we can get is 5.499999999999999'''
