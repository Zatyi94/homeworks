print('1. feladat:')
# keszits programot ami egy neveket tartalmazó listában
# megmondja hogy van e benne Pista es kiirja azt is hogy hanyadik elem
# a listában a Pista
x = ['Eszti', 'Patrik', 'Tamás', 'Brigi', 'Pista', 'Anna', 'Márk']
print('Pista' in x)
print('A listában a Pista a {}. név.'.format(x.index('Pista')))

print('2. feladat:')
# keszits programot ami egy szamokat tartalmazo tomb-on vegig megy
# es egy osszeg valtozoba bepakolja a szamok osszegét. A ciklus után az osszeg
# valtozot irja ki a kepernyore
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z = 0
for i in y:
    z += i
print(z)

print('3. feladat:')
# Az elozo programot bovitsd ki úgy hogy uzenetet dobjon ha a tomb
# egyik eleme
# nem szam, es azt ne vegye figyelembe, de igy is osszegezze a többi number
# tipusu elemeket, es irja ki az eredmenyt
y = [1, 2, 3, 4, 5, 6, True, 7, 8, 9, 10]
z = 0
for i in y:
    if type(i) == int:
        z += i
    if type(i) != int:
        print('A lista ezen eleme nem szám: {}'.format(i))
print(z)

print('4. feladat:')
# Az elozo programot bovitsd ki ugy hogy amennyiben nem szam a tomb
# egyik eleme
# akkor probalja meg a program a int fgv-el atkonvertalni
# számmá, és ezután
# újra nézze meg hogy szám e az adott elem. Ha igen, adja hozzá,
# ha nem, jelezze
# egy print-el hogy nem sikerult a konvertalas annál az elemnél
y = [1, 2, 3, '4', 5, 6, 7, 8, 9, 10]
z = 0
for i in y:
    if type(i) == int:
        z += i
    if type(i) != int:
        z = z + int(i)
print(z)

'''
Rájöttem, hogy az if, else, elif és return használata nekem még nagyon nehezen megy.
Pl. mikor érdemes simán print-elni az 'ez nem szám' és hasonló üzeneteket,
és mikor használjuk a returnt?
Ha ilyen programokat próbálok írni, sokszor kapok SyntaxErrort.
Szívesen gyakorolnék még ilyen feladatokat az órán, főleg ha ez a többikenek is segítene.
Köszönettel, Nóra
'''
