print("Kalkulacka (+,-,*,/,^)")
a = int(input("Zadejte prvni cislo: "))
b = input("Zadejte operace: ")
c = int(input("Zadejte druhy cislo: "))

if (b == "*"):
    d = a * c
    print("{} * {} = {}".format(str(a),str(c),str(d)))
elif (b == "/"):
    if (c == 0): print("Deleni nulou!")
    else:
        d = a / c
        print("{} / {} = {}".format(str(a),str(c),str(d)))
elif (b == "+"):
    d = a + c
    print("{} + {} = {}".format(str(a),str(c),str(d)))
elif (b == "-"):
    d = a - c
    print("{} - {} = {}".format(str(a),str(c),str(d)))
elif (b == "^"):
    d = a ** c
    print("{} ^ {} = {}".format(str(a),str(c),str(d)))
else: print("Neni operace!")
