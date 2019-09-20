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