import random
import os
import time
clear = lambda: os.system('cls')
clear()
print("Before the start, you shall know that having 0 mana will kill your champion imediatly(its blocked dont worry bastard)")
print("Player 1 nickname")
g1 = input("Enter your name : ")
takeover=0  
while takeover==0:
    print("| Hero 1 - Swordsman | Hero 2 - Tank | Hero 3 - Wizard |")
    g1h = input("Pick your hero! ")
    if g1h=='Hero 1':
        Heroname = 'Scott'
        dmg = 30
        hp = 120
        ult = 50
        mana = 40
        takeover=1
    elif g1h=='Hero 2':
        Heroname = 'Elias The Grand Order Commander'
        dmg = 40
        hp = 250
        ult = 70
        takeover=1
        mana = 50
    elif g1h=='Hero 3':
        Heroname = 'Leon The wizard'
        dmg = 80
        hp = 50
        ult = 100
        takeover=1
        mana = 100
    else:
        print("try again")
time.sleep(2.4)
clear()
print(g1,' You have chosen',Heroname)
enemylottery = random.randrange(0,3)+1
if enemylottery==1:
    enemyname = 'Tanya, The Devil'
    edmg = 20
    ehp = 220
elif enemylottery==2:
    enemyname = 'Iorweth, The Bastard'
    edmg = 40
    ehp = 150
elif enemylottery == 3:
    enemyname = 'Soulchef, The BigGangsta'
    edmg = 10
    ehp = 450
print(Heroname,'Your enemy on Arena will be',enemyname)
while ehp > 0 | hp > 0:
    typeattack = input('Use your skills to attack! "Ult"(-40mana) or "Attack"(+20mana)')
    if typeattack=='Ult' and mana>40 and typeattack=='ult':
        ehp = ehp - ult
        mana = mana - 40
        print(Heroname, ' Attacked ',enemyname,'using UltSkill! And gived',ult, 'dmg! Enemy hp left is ',ehp)
    elif typeattack=='Attack' and typeattack=='attack' :
        ehp = ehp - dmg
        mana = mana + 20
        print(Heroname, ' Attacked ', enemyname, 'using Normal Attack! And gived', dmg, 'dmg! Enemy hp left is ', ehp)
        time.sleep(3.4)
        clear()
    if ehp < 0:
        print('Game Over, you Won!')
        time.sleep(4.4)
        exit()
    print(enemyname,' attacked ',Heroname,'dealing ',edmg, 'dmg! Hero hp left is ', hp)
    hp = hp - edmg
    time.sleep(3.4)
    clear()
    if hp < 0:
        print('Game Over, you Lost!')
        time.sleep(4.4)
        exit()
