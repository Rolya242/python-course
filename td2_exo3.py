a = int(input("saisir un nombre entier a "))
b = int(input("saisir un nombre entier b "))
r = input("saisir l\'un des  symboles (*,-,+,/)   ")
if r == "*" or r == "-" or r == "+" or r == "/":
    if r == "*":
        s = a * b
    if r == "-":
        s = a - b
    if r == "+":
        s = a + b
    if r == "/":
        s = a / b
else:
    print("erreur de saisie !")
    exit()

print(f"resultat est {a} {r} {b} = {s}")

