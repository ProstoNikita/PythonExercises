import math
# Obsah a obvod ctvrce
a = int(input("Zadejte stranu ctvrce: "))
print ("Obvod ctvrce: ", a*4)
print ("Obsah ctvrce: ", a*a)
print(end="\n")

#Obsah a obvod obdelnika
a = int(input("Zadejte prvni stranu obdelnika: "))
b = int(input("Zadejte druhy stranu obdelnika: "))
print ("Obvod obdelnika: ", (a+b)*2)
print ("Obsah obdelnika: ", a*b)
print(end="\n")

#Obsah a obvod kruhu
pi = 3.14
a = int(input("Zadejte polomer kruhu: "))
print("Obvod kruhu: ", float(2*pi*a))
print("Obsah kruhu: ", float(pi*a*a))
print(end="\n")

#Povrch a objem koule
a = int(input("Zadejte polomer koule: "))
print("Povrch kruhu: ", float(4*pi*a*a))
print("Objem kruhu: ", float(4/3*pi*a*a*a))
print(end="\n")

#Soucet, rozdil, soucin dvou cisel
a = int(input("Zadejte prvni cislo: "))
b = int(input("Zadejte druhe cislo: "))
print("Soucet cisel: ", a+b)
print("Rozdil cisel: ", a-b)
print("Soucin cisel: ", a*b)
print(end="\n")

#Zmena cisel
a = int(input("Zadejte cislo pro promenu a: "))
b = int(input("Zadejte cislo pro promenu b: "))
a = a + b
b = a - b
a = a - b
print("Promena a:", a)
print("Promena b:", b)
print(end="\n")

#Objem kvadru
a = int(input("Zadejte sirku kvadra: "))
b = int(input("Zadejte delku kvadra: "))
c = int(input("Zadejte vysku kvadra: "))
print("Objem kvadra: ", a*b*c)
print(end="\n")

#Vzdalenost dvou bodu
a = int(input("Zadejte X prvniho bodu: "))
b = int(input("Zadejte Y prvniho bodu: "))
c = int(input("Zadejte X druheho bodu: "))
d = int(input("Zadejte Y druheho bodu: "))
print ("Vzdalenost dvou bodu: ", math.sqrt((c - a)**2 + (d - b)**2))
print(end="\n")

#Obsah trojuhelnika
a = int(input("Zadejte prvni stranu trojuhelnika: "))
b = int(input("Zadejte druhy stranu trojuhelnika: "))
c = int(input("Zadejte treti stranu trojuhelnika: "))
s = (a + b + c) / 2
print("Obsah trojuhelnika: ", math.sqrt(s * (s - a) * (s - b) * (s - c)))
print(end="\n")

#Liche nebo sude?
a = int(input("Zadejte cislo: "))
if (a % 2 == 0):
    print("Cislo je sude.")
else:
    print("Cislo je liche.")
print(end="\n")

#Objem sudu a vejde voda, nebo ne?
a = int(input("Zadejte prumer sudu: "))
b = int(input("Zadejte vysku sudu: "))
c = int(input("Objem vody: "))
d = pi*a*a/4*b * 1000 #objem sudu v litrech
if d < c:
    print("Voda nevejde.")
else:
    print("Voda vejde")
    print("Hladina bude na vysce: ", c/(pi*a*a/4))
print(end="\n")

#Cislo v intervalu
a = int(input("Zadejte cislo: "))
if 10 <= a <= 20:
    print("Cislo je prvkem intervalu")
else:
    print("Cislo neni prvkem intervalu")
print(end="\n")

#Porovnani cisel
a = int(input("Zadejte prvni cislo: "))
b = int(input("Zadejte druhy cislo: "))
if a < b:
    print("Vetsi cislo: ", b)
elif a > b:
    print("Vetsi cislo: ", a)
else:
    print("Zadana cisla jsou stejna")
print(end="\n")

#Pravouhly, ostrouhly, tupouhly
a = int(input("Zadejte prvni stranu trojuhelnika: "))
b = int(input("Zadejte druhy stranu trojuhelnika: "))
c = int(input("Zadejte treti stranu trojuhelnika: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Trojuhelnika exestuje")
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Trojuhelnik je pravouhly")
    elif a*a + b*b < c*c or a*a + c*c < b*b or b*b + c*c < a*a:
        print("Trojuhelnik je tupouhly")
    else: print("Trojuhelnik je ostrouhly")
else:
    print("Trojuhelnika neexestuje")
print(end="\n")

#Reseni kvadraticke rovnici
a = int(input("Zadejte koeficient a: "))
b = int(input("Zadejte koeficient b: "))
c = int(input("Zadejte koeficient c: "))
d = b*b - 4*a*c
if d > 0:
    print("Rovnice ma dve reseni")
    print("X1 = ", (-b + math.sqrt(d))/ 4 * a)
    print("X2 = ", (-b - math.sqrt(d))/ 4 * a)
elif d == 0:
    print("Rovnice ma jedno reseni")
    print("X = ", (-b + math.sqrt(d)) / 4 * a)
else: print("Rovnice nema reseni")
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

#Jedoducha kalkulacka
print("Kalkulacka (+,-,*,/,^)")
a = int(input("Zadejte prvni cislo: "))
b = input("Zadejte operace: ")
c = int(input("Zadejte druhy cislo: "))

if (b == "*"):
    d = a * c
    print("{} * {} = {}".format(a,c,d))
elif (b == "/"):
    if (c == 0): print("Deleni nulou!")
    else:
        d = a / c
        print("{} / {} = {}".format(a,c,d))
elif (b == "+"):
    d = a + c
    print("{} + {} = {}".format(a,c,d))
elif (b == "-"):
    d = a - c
    print("{} - {} = {}".format(a,c,d))
elif (b == "^"):
    d = a ** c
    print("{} ^ {} = {}".format(a,c,d))
else: print("Neni operace!")
print(end="\n")

