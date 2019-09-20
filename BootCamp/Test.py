import math
import random

# Obsah a obvod ctvrce
a = int(input("Zadejte stranu ctvrce: "))
print("Obvod ctvrce: ", a * 4)
print("Obsah ctvrce: ", a * a)
print(end="\n")

# Obsah a obvod obdelnika
a = int(input("Zadejte prvni stranu obdelnika: "))
b = int(input("Zadejte druhy stranu obdelnika: "))
print("Obvod obdelnika: ", (a + b) * 2)
print("Obsah obdelnika: ", a * b)
print(end="\n")

# Obsah a obvod kruhu
pi = 3.14
a = int(input("Zadejte polomer kruhu: "))
print("Obvod kruhu: ", float(2 * pi * a))
print("Obsah kruhu: ", float(pi * a * a))
print(end="\n")

# Povrch a objem koule
a = int(input("Zadejte polomer koule: "))
print("Povrch kruhu: ", float(4 * pi * a * a))
print("Objem kruhu: ", float(4 / 3 * pi * a * a * a))
print(end="\n")

# Soucet, rozdil, soucin dvou cisel
a = int(input("Zadejte prvni cislo: "))
b = int(input("Zadejte druhe cislo: "))
print("Soucet cisel: ", a + b)
print("Rozdil cisel: ", a - b)
print("Soucin cisel: ", a * b)
print(end="\n")

# Zmena cisel
a = int(input("Zadejte cislo pro promenu a: "))
b = int(input("Zadejte cislo pro promenu b: "))
a = a + b
b = a - b
a = a - b
print("Promena a:", a)
print("Promena b:", b)
print(end="\n")

# Objem kvadru
a = int(input("Zadejte sirku kvadra: "))
b = int(input("Zadejte delku kvadra: "))
c = int(input("Zadejte vysku kvadra: "))
print("Objem kvadra: ", a * b * c)
print(end="\n")

# Vzdalenost dvou bodu
a = int(input("Zadejte X prvniho bodu: "))
b = int(input("Zadejte Y prvniho bodu: "))
c = int(input("Zadejte X druheho bodu: "))
d = int(input("Zadejte Y druheho bodu: "))
print("Vzdalenost dvou bodu: ", math.sqrt((c - a) ** 2 + (d - b) ** 2))
print(end="\n")

# Obsah trojuhelnika
a = int(input("Zadejte prvni stranu trojuhelnika: "))
b = int(input("Zadejte druhy stranu trojuhelnika: "))
c = int(input("Zadejte treti stranu trojuhelnika: "))
s = (a + b + c) / 2
print("Obsah trojuhelnika: ", math.sqrt(s * (s - a) * (s - b) * (s - c)))
print(end="\n")

# Liche nebo sude?
a = int(input("Zadejte cislo: "))
if (a % 2 == 0):
    print("Cislo je sude.")
else:
    print("Cislo je liche.")
print(end="\n")

# Objem sudu a vejde voda, nebo ne?
a = int(input("Zadejte prumer sudu: "))
b = int(input("Zadejte vysku sudu: "))
c = int(input("Objem vody: "))
d = pi * a * a / 4 * b * 1000  # objem sudu v litrech
if d < c:
    print("Voda nevejde.")
else:
    print("Voda vejde")
    print("Hladina bude na vysce: ", c / (pi * a * a / 4))
print(end="\n")

# Cislo v intervalu
a = int(input("Zadejte cislo: "))
if 10 <= a <= 20:
    print("Cislo je prvkem intervalu")
else:
    print("Cislo neni prvkem intervalu")
print(end="\n")

# Porovnani cisel
a = int(input("Zadejte prvni cislo: "))
b = int(input("Zadejte druhy cislo: "))
if a < b:
    print("Vetsi cislo: ", b)
elif a > b:
    print("Vetsi cislo: ", a)
else:
    print("Zadana cisla jsou stejna")
print(end="\n")

# Pravouhly, ostrouhly, tupouhly
a = int(input("Zadejte prvni stranu trojuhelnika: "))
b = int(input("Zadejte druhy stranu trojuhelnika: "))
c = int(input("Zadejte treti stranu trojuhelnika: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Trojuhelnika exestuje")
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("Trojuhelnik je pravouhly")
    elif a * a + b * b < c * c or a * a + c * c < b * b or b * b + c * c < a * a:
        print("Trojuhelnik je tupouhly")
    else:
        print("Trojuhelnik je ostrouhly")
else:
    print("Trojuhelnika neexestuje")
print(end="\n")

# Reseni kvadraticke rovnici
a = int(input("Zadejte koeficient a: "))
b = int(input("Zadejte koeficient b: "))
c = int(input("Zadejte koeficient c: "))
d = b * b - 4 * a * c
if d > 0:
    print("Rovnice ma dve reseni")
    print("X1 = ", (-b + math.sqrt(d)) / 4 * a)
    print("X2 = ", (-b - math.sqrt(d)) / 4 * a)
elif d == 0:
    print("Rovnice ma jedno reseni")
    print("X = ", (-b + math.sqrt(d)) / 4 * a)
else:
    print("Rovnice nema reseni")
print(end="\n")

"""""
    #Tri body na jedne primce
    a = int(input("Zadejte X prvniho bodu: "))
    b = int(input("Zadejte Y prvniho bodu: "))
    c = int(input("Zadejte X druheho bodu: "))
    d = int(input("Zadejte Y druheho bodu: "))
    e = int(input("Zadejte X tretiho bodu: "))
    f = int(input("Zadejte Y tretiho bodu: "))
"""""

# Jedoducha kalkulacka
print("Kalkulacka (+,-,*,/,^)")
a = int(input("Zadejte prvni cislo: "))
b = input("Zadejte operace: ")
c = int(input("Zadejte druhy cislo: "))

if (b == "*"):
    d = a * c
    print("{} * {} = {}".format(a, c, d))
elif (b == "/"):
    if (c == 0):
        print("Deleni nulou!")
    else:
        d = a / c
        print("{} / {} = {}".format(a, c, d))
elif (b == "+"):
    d = a + c
    print("{} + {} = {}".format(a, c, d))
elif (b == "-"):
    d = a - c
    print("{} - {} = {}".format(a, c, d))
elif (b == "^"):
    d = a ** c
    print("{} ^ {} = {}".format(a, c, d))
else:
    print("Neni operace!")
print(end="\n")

# Mince
a = int(input("Zadejte vasi utratu: "))
b = 0  # 50 korun
c = 0  # 20 korun
d = 0  # 10 korun
e = 0  # 5 korun
f = 0  # 2 koruny
g = 0  # 1 koruna
h = 0  # pocet mince

if a <= 0:
    print("Chyba!")
else:
    while a >= 50:
        a -= 50
        b += 1
        h += 1
    while a >= 20:
        a -= 20
        c += 1
        h += 1
    while a >= 10:
        a -= 10
        d += 1
        h += 1
    while a >= 5:
        a -= 5
        e += 1
        h += 1
    while a >= 2:
        a -= 2
        f += 1
        h += 1
    while a >= 1:
        a -= 1
        g += 1
        h += 1
    print("Celkem je potreba {} minci".format(h))
    print("Pocet minci o hodnote 50 Kc: ", b)
    print("Pocet minci o hodnote 20 Kc: ", c)
    print("Pocet minci o hodnote 10 Kc: ", d)
    print("Pocet minci o hodnote 5 Kc: ", e)
    print("Pocet minci o hodnote 2 Kc: ", f)
    print("Pocet minci o hodnote 1 Kc: ", g)
print(end="\n")

# N-krat text
a = int(input("Zadejte cislo: "))
b = input("Zadejte text: ")
for i in range(a):
    print(b)
print(end="\n")

# Cislovy rad
a = int(input("Zadejte posledni cislo: "))
for i in range(1, a + 1):
    print(i)
print(end="\n")

# Cislovy rad naopak
a = int(input("Zadejte prvni cislo: "))
for i in range(a + 1, 1, -1):
    print(i)
print(end="\n")

# Cislovy rad s carkami a mezerami
a = int(input("Zadejte posledni cislo"))
for i in range(1, a + 1):
    if i == a:
        print(i)
    else:
        print(i, end=", ")
print(end="\n")

# Cislovy rad naopak
a = int(input("Zadejte prvni cislo: "))
for i in range(a, 0, -1):
    if i == 1:
        print(i)
    else:
        print(i, end=", ")
print(end="\n")

# Faktorial
a = int(input("Zadejte cislo: "))
b = 1
for i in range(1, a + 1):
    b *= i
print("{}! = {}".format(a, b))
print(end="\n")

# Prvocislo
a = int(input("Zadejte cislo: "))
b = 0  # pocet delitelu
for i in range(1, a + 1):
    if a % i == 0:
        b += 1
if b == 2:
    print("Cislo je prvocislo")
else:
    print("Cislo neni prvocislo")
print(end="\n")

# Z binarniho cisla k normalnimu cislu
a = input("Zadejte binarni cislo: ")
b = 0  # normalni cislo
f = 0
for i in range(len(a) - 1, -1, -1):
    if a[f] == "1":
        b += 2 ** i
    f += 1
print("Normalni cislo: ", b)

# Prvocislo (zlepseni)
a = int(input("Zadejte cislo: "))
b = 0  # pocet delitelu
c = 0
print("Vsechny prvocisla mensi nez", a, ": ")
for i in range(1, a + 1):
    for g in range(1, i + 1):
        if i == a: break
        if i % g == 0:
            c += 1
        if c == 2:
            print(i)
        c = 0
        if a % i == 0:
            b += 1
    if b == 2:
        print("Cislo je prvocislo")
    else:
        print("Cislo neni prvocislo")
print(end="\n")

# Matice
n = int(input("Zadejte cislo: "))
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            if j == n - 1:
                print(1)
            else:
                print(1, end=", ")
        else:
            if j == n - 1:
                print(0)
            else:
                print(0, end=", ")
print(end="\n")

# Baracek
n = int(input("Zadejte liche cislo vetsi nebo se rovna 5: "))
if n % 2 == 0:
    print("Cislo je sude!")
elif n <= 4:
    print("Cislo je mensi nez 5!")
else:
    print((n // 2) * " " + "#")
    for i in range(0, ((n // 2) - 1)):
        print(((n // 2) - 1 - i) * " ", end="")
        print("#", end="")
        print((2 * i + 1) * " ", end="")
        print("#")
    print("#" * n)
    for i in range(0, n - 2):
        print("#", end="")
        print(" " * (n - 2), end="")
        print("#")
    print("#" * n)
print(end="\n")

# Fibonacciho posloupnost
n = int(input("Zadejte prirozene cislo: "))
a = 0  # prvni element
b = 1  # druhy element
for i in range(0, n - 2):
    c = b
    b += a
    a = c
if (n == 1): b = 0
print("{}. element Fibonacciho posloupnosti: ".format(n), b)
print(end="\n")

# Nejvetsi spolecny delitel
a = int(input("Zadejte prvni cislo: "))
b = int(input("Zadejte druhe cislo: "))
c = 0  # delitel
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        c = i
print("Nejvetsi spolecny delitel: ", c)
print(end="\n")

# Soucet cisel v intervalu
a = int(input("Zadejte prvni cislo: "))
b = int(input("Zadejte druhe cislo: "))
c = 0  # soucet
for i in range(a, b + 1):
    c += i
print("Soucet: ", c)
print(end="\n")

# Mocnina
a = int(input("Zadejte zaklad: "))
b = int(input("Zadejte exponent: "))
if a == 0 and b == 0:
    print("Neni definovano!")
elif a < 0 or b < 0:
    print("Neni prirozene cislo")
else:
    c = a ** b
    print("{}^{} =".format(a, b), c)
print(end="\n")

# 10 nahodnych cisel
cisla = []
a = 0  # soucet sudych cisel
b = 0  # soucet lichych cisel
c = 0  # soucet vsech cisel
d = 0  # nejvetsi cislo
e = 0  # druhe nejvetsi cislo

for i in range(10):
    cisla.append(random.randint(1, 100))
print("10 nahodnych cisel:", cisla)

for i in cisla:
    if i > d:
        d = i
    c += i
    if i % 2 == 0:
        a += i
    else:
        b += i
print("Soucet sudych cisel:", a)
print("Soucet lichych cisel:", b)
print("Prumerna hodnota vsech cisel:", c / 10)

for i in cisla:
    if i > e and i != d:
        e = i
print("Nejvetsi cislo:", d)
print("Druhy nejvetsi cislo:", e)
print(end="\n")
