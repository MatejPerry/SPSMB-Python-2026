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
    print(number[::-1])

def dupe():
    N = input("Zadej cisla: ")
    cislo = []
    for i in cislo.split():
        a = int(i)
        # if a not in cislo:
            # cislo.append(a)
    st = set(cislo)
    lst = set(st)
    print(cislo)

def maxmin():
    N = input("Zadejte cisla: ")
    numbers = []
    min = float("inf")
    max = float("-inf")
    for i in N.split():
        a = int(i)
        if i > max:
            max = a
        elif i < min:
            min = a
    print(f"Max: {max}")    
    print(f"Min: {min}")    
        

if __name__ == "__main__":
    samohlasky()