import random
print("Player 1 nickname")
g1 = input("Enter your name : ")
print("Player 2 nickname")
g2 = input("Enter your name : ")
y = random.randrange(0,2)+1
if y==1:
    print("Choose your side of coin",g1)
    g1c = input("1-heads or 2-tails : ")
    if g1c==1:
        g2c=2
    else:
        g2c=1
else:
    print('Choose your side of coin', g2)
    g2c = input("1-heads or 2-tails: ")
    if g2c==1:
        g1c=2
    else:
        g1c=1
print( g1,'chosen -',g1c)
print(g2,'chosen -',g2c)
x = random.randrange(0,2)+1
print('The coin drop is',x)
if x==g1c:
    print(g1,' won the game')
else:
    print(g2, ' won the game')
