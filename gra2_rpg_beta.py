import random
print("Player 1 nickname")
g1 = input("Enter your name : ")
takeover=0  
while takeover=0
    print("| Hero 1 - Swordsman | Hero 2 - Tank | Hero 3 - Wizard |")
    g1h = input("Pick your hero! ")
    if g1h=='Hero 1':
        Heroname = 'Scott'
        dmg = 30
        hp = 120
        ult = 50
        mana = 40
        ultname = 'Sword Furry'
    elif g1h=='Hero 2':
        Heroname = 'Elias The Grand Order Commander'
        dmg = 40
        hp = 250
        ult = 70
        ultname = 'Berserk'
        mana = 50
    elif g1h=='Hero 3':
        Heroname = 'Leon The wizard'
        dmg = 80
        hp = 50
        ult = 100
        ultname = 'Meteor rain'
        mana = 100
    print(g1,' You have chosen',Heroname)
    takeover=1
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
    if typeattack=='Ult':
        ehp = ehp - ult
        mana = mana - 40
        print(Heroname, ' Attacked ',enemyname,'using UltSkill! And gived',ult, 'dmg! Enemy hp left is ',ehp)
    elif typeattack=='Attack':
        ehp = ehp - dmg
        mana = mana + 20
        print(Heroname, ' Attacked ', enemyname, 'using Normal Attack! And gived', dmg, 'dmg! Enemy hp left is ', ehp)
    if ehp < 0:
        print('Game Over, you Won!')
        exit()
    hp = hp - edmg
    print(enemyname,' attacked ',Heroname,'dealing ',edmg, 'dmg! Hero hp left is ', hp)
    if hp < 0:
        print('Game Over, you Lost!')
        exit()



