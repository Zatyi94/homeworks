print('1. feladat:')
# készíts egy programot ami az alábbi tömbben eldönti
# az összes elemről hogy osztható e kettővel vagy nem
nums = [3, 4, 9, 6, 2]
# a kettővel oszthatóság ellenőrzését maradékos osztással
# kell megnézni:
# 8 % 2 == 0  True mert a maradék nulla
# 3 % 2 == 0  False mert van maradék
# az eredményt így írd ki a képernyőre:
# 3: nem osztható
# 4: osztható
# 9: nem osztható
# 6: osztható
# 2: osztható
for i in nums:
    if i % 2 == 0:
        print('{}: osztható'.format(i))
    else:
        print('{}: nem osztható'.format(i))
print('\n')

print('2. feladat:')
# készíts egy programot ami kiirja a tömb összes elemét
# de úgy hogy az indexét is pl:
# ebből:
players = ['Peter', 'Kate', 'John']
# ezt írja ki:
# 0. Peter
# 1. Kate
# 3. John
for index, name in enumerate(players):
    print('{}. {}'.format(index, name))
print('\n')

print('3. feladat:')
# készíts egy függvényt ami megvizsgálja egy elem
# összes tipusát, és kigyűjti őket egy tömbbe.
# pl ebből:
x = ['', 4, True]
# ezt csinálja: ['str', 'int', 'bool']
# Először hozz létre egy üres tömböt, és az append
# függvénnyel add hozzá a típusokat így:
# a=['first']
# a.append['second']  # a is now: ['first', 'second']
# 1. megoldás
y = []
for i in x:
    if str(type(i)).split("'")[1] == 'str':
        y.append('string')
    if str(type(i)).split("'")[1] == 'int':
        y.append('number')
    if str(type(i)).split("'")[1] == 'bool':
        y.append('boolean')
print(y)
# 2. megoldás
z = []
for i in x:
    if type(i) == str:
        z.append('string')
    if type(i) == int:
        z.append('number')
    if type(i) == bool:
        z.append('boolean')
print(z)
