a = input("saisir un nombre à virgule flottante a  ")
b = input("saisir un nombre à virgule flottante b  ")
c = input("saisir un nombre à virgule flottante c  ")
print("voici les nombres de le plus grand a petit")
if(a > b):
    if(a > c):
        print(f"{a}")
        if(b > c):
            print(f"{b}")
            print(f"{c}")
        else:
            print(f"{c}")
            print(f"{b}")
elif(b > c):
    print(f"{b}")
    if(a > c):
        print(f"{a}")
        print(f"{c}")
    else:
        print(f"{c}")
        print(f"{b}")
else:
    print(f"{c}")
    if (b > a):
        print(f"{b}")
        print(f"{a}")
    else:
        print(f"{a}")
        print(f"{b}")






