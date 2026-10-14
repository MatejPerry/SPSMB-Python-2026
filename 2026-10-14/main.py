def NSD():
    a = int(input("Zadej prvni cislo: "))
    b = int(input("Zadej druhe cislo: "))

    while b != 0:
        a, b = b, a % b
        
    print(a)

def delka():
    text = input("Zadej retezec: ")
    print(len(text))

def palindrom():
    text = input("Zadej text: ")
    palindrom = (f"{text[::-1]}")
    if palindrom == text:
        print("Je palindrom")
    else:
        print("Neni palindrom")

def samohlasky():
    text = input("Zadej text: ")
    lst = ["a", "e", "i", "o", "u"]
    for c in lst:
        counter = 0
        for h in text:
            if c == h:
                counter += 1
    
    print(f"V textu je {c} × {counter}")

    # text = input("Zadej text: ")
    # count = 0
    # for i in range (len(text)):
    #     if ((text[i]) == ('a' or 'e' or 'i' or 'o' or 'u')):
    #         count = count + 1
    # print(f"Pocet samohlasek je: {count}")

def znaky():
    text = input("Zadej text: ")

def list_sum():
    N = input("Zadejte cislo: ")
    number = []
    for i in N.split():
        number.append(int(i))
    print(sum(number))

def seznam():
    N = input("Zadejte cislo: ")
    number = []
    for i in N.split():
        number.append.(int(i))
    print(number.reverse())

if __name__ == "__main__":
    samohlasky()