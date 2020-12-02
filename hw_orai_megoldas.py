# 1.3.
num = input("irj be egy szamot: ")

try:
    test_num = int(num)
    for i in range(test_num):
        print('{}: Helló'.format(i+1))
except ValueError:
    print('ez nem szam')

# 1.4.
'''
num = input("irj be egy szamot: ")

try:
    r = int(num)
    print("a kör területe: {}".format(2*r*math.pi))
    print("a kör területe: {}".format(r*r*math.pi))
except ValueError:
    print("ez nem szam")
'''

# 1.5
names = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána',
         'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']

sorted_names = sorted(names)
if len(sorted_names) % 2 == 0:
    half_index = int(len(sorted_names)/2)
    group1 = sorted_names[:half_index]
    group2 = sorted_names[half_index:]

print('1.csoport:')
for name in group1:
    print(name)
print('2.csoport:')
for name in group2:
    print(name)

# 2.1.3 Sándor-féle megoldás
x = ['', 4, True]
a = []
i = 0
for i in x:
    a.append(type(i).__name__)
print(a)

# 2.2.1.
names = ['Eszti', 'Patrik', 'Tamás', 'Brigi', 'Pista', 'Anna', 'Márk']
try:
    van_pista = names.index('Pista')
    print('Pista ezen a helyen van: {}'.format(van_pista))
except ValueError:
    print('Nincs Pista')

# 2.2.2.
nums = [2, 4, 5]
sum_of_nums = 0
for num in nums:
    sum_of_nums = sum_of_nums + num
print(sum_of_nums)

# 2.2.3.
nums = [2, 4, 's', 5]
sum_of_nums = 0
for num in nums:
    if type(num) is int:
        sum_of_nums = sum_of_nums + num
print(sum_of_nums)

# 2.2.4.
nums = [2, 4, '4', 5, 's']
sum_of_nums = 0
for num in nums:
    try:
        num = int(num)
    except ValueError:
        print('nem sikerult a konvertalas')
    if type(num) is int:
        sum_of_nums = sum_of_nums + num
print(sum_of_nums)
