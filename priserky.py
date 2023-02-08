import random
monsters=[]
dlzka = 5
cage = []

def create_monster():
    temp = []
    for i in range(dlzka):
        temp.append(random.randint(0,10))
    return temp

def iq_test(monster:list)->int:
    return monster.count(1)

def sex(monster1, monster2):
    temp = []
    for i in range(dlzka):
        nahoda = random.randrange(1,101)
        if nahoda >7:
            #normalny sex
            nahoda1 = random.randrange(1,101)
            #polka od tatka alebo od mamky
            if nahoda >50:
                temp.append(monster1[i])
            else:
                temp.append(monster2[i])
        else:
            #mutacia
            temp.append(random.randrange(0,10))
    return temp

def rucna_triedicka(cage):
    for i in range(len(cage),0,-1):
        for j in range(0,i-1):
            if iq_test(cage[j])>iq_test(cage[j+1]):
                cage[j],cage[j+1]=cage[j+1],cage[j]

for i in range(10):
        cage.append(create_monster())

print(cage)
for j in range(20):
    rucna_triedicka(cage)
    cage = cage[len(cage)//2::]
    for i in range(len(cage)):
        cage.append(sex(cage[random.randrange(0,5)],cage[random.randrange(0,5)]))
    print(cage[::-1])
    input()
