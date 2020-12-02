a = "1. Feladat"
print(a)
'''Készíts egy programot ami megtalál minden számot 2000 és 3200 között ami osztható 7-el, de nem osztható 5-el.
Segítség: használd a range függvény-t és az append-et'''
x = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        x.append(i)
print(x)
print('\n')

b = "2. Feladat"
print(b)
'''Adott az alábbi tömb:
['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István',
    'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']
Készíts egy programot ami megszámolja ebben a tömbben a Pistákat'''
nevsor = ['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István',
          'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']
# 1. megoldás:
x = 0
for nev in nevsor:
    if nev == 'Pista':
        x += 1
print('Ebben a névsorban {} fő szerepel Pista néven.'.format(x))
# 2. megoldás:
print('{} fő szerepel Pista néven ebben a névsorban.'.format(nevsor.count('Pista')))
print('\n')

c = "3. Feladat"
print(c)
'''Kérj be a felhasználótól egy számot az input függvény segítségével. Ez után próbáld meg a számot int függvényyel számmá alakítani, végül készíts egy ciklust ami annyiszor fut le amekkora számot beírt a felhasználó, és annyiszor írja ki a képernyőre hogy Helló, de a sorokat is számozza (1től)!'''
num = int(input('Adj meg egy számot: '))
# print(type(num))
# print("A szám, amit kaptam: {}".format(num))
x = []
while num > 0:
    x.append(num)
    num -= 1
for index, num in enumerate(x):
    print('{}. Helló'.format(index+1))
print('\n')

d = "4. Feladat"
print(d)
'''Készíts egy programot ami bekér a felhasználótól egy számot, amit az int függvénnyel alakíts számmá. A bekért szám egy kör sugara legyen, a program pedig számolja ki a kör sugarából a kör területét és kerületét. A számításhoz használd ezt a képletet https: // www.calculat.org/hu/terulet-kerulet/kor.html'''
r = int(input('Adj meg egy számot: '))
print('A kör általad megadott sugara: r = {}'.format(r))
d = 2 * r
π = 3.14
K = π * d
T = π * r**2
print('A kör kerülete: K = {}'.format(K))
print('A kör területe: T = {}'.format(T))
print('\n')

e = "5. Feladat"
print(e)
'''Adott az alábbi tömb:
['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva',
    'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']
Készíts programot ami a neveket abc sorrendbe rendezi(sorted függvénnyel) majd a csoportot két részre osztja(megfelezi) és kiírja a képernyőre a két csoportot külön. Például így:
1.	csoport:
Gaál András
Gaál Bernadett
Kovács Tamás
Kucsera Bálint
Ledán-Munteán Szabolcs
Lukács Dániel
2.	csoport
Magyar Eszter
Mészáros Melinda
Németh Diána
Szamosi Judit
Telek Éva
Tóth Sára
Bővítsd a programot arra az esetre ha a nevek száma páratlan!'''
lista = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána',
         'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']
lista.sort(reverse=False)
print('Abc sorrendbe rendezett névsor:')
print(lista)
print('Névsor 2 csoportra osztva:')
# 1. megoldás:
print('1. csoport:')
for i in lista[:6]:
    print(i, end='\n')
print('2. csoport:')
for i in lista[6:]:
    print(i, end='\n')

# 2. megoldás:
if len(lista) % 2 != 0:
    lista.append('Zatykó Nóra')
    print(lista)

print('1. csoport:')
for i in lista[0:int(len(lista)/2)]:
    print(i, end='\n')
print('2. csoport:')
for i in lista[int(len(lista)/2):]:
    print(i, end='\n')
