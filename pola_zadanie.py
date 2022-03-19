import math
print('1- szescian 2- prostopadloscian 3-kulla')
menu = input()
if menu == 1:
    print("wybrales pole szescianu")
    print('podaj a')
    z = input()
    x = lambda a:(a ** 3)
    print(x(z))
elif menu == 2:
    print("wybrales pole prostopadloscianu")
    print("wybrales pole szescianu")
    print('podaj a')
    z = input()
    print('podaj b')
    y = input()
    x = lambda a,b:(a * b)
    print(x(z,y))
elif menu == 3:
    print("wybrales pole kulli")
    print('podaj r')
    r = input()
    x = lambda r:(4/3)*math.pi*(r**3)
    print(x(r))
else:
    print("wybrano bledna opcje")