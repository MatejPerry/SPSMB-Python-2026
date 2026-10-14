def NSD():
    a = int(input("Zadej prvni cislo: "))
    b = int(input("Zadej druhe cislo: "))

    while b != 0:
        a, b = b, a % b
        
    print(a)

if __name__ == "__main__":
    NSD()