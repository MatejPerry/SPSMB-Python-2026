def prumer():
    N = int(input("Zadej kolik chces zadat cisel: "))
    numbers = []
    for i in range(N):
        number = int(input(f"Zadej {i+1}. cislo: "))
        numbers.append(number)
    print(sum(numbers) / len(numbers))

def suda_licha():
    N = int(input("Zadej kolik chces zadat cisel: "))
    numbers = []
    suda = 0
    licha = 0
    for i in range(N):
        number = int(input(f"Zadej {i+1}. cislo: "))
        numbers.append(number)
    for i in range (len(numbers)):
        if numbers[i] % 2 == 0:
            suda = suda + 1
        else:
            licha = licha + 1

    print(f"Licha: {licha}")
    print(f"Suda: {suda}")

def pocet_cislic():
    N = int(input("Zadej cislo: "))
    lst = []
    while N != 0:
        lst.append(N % 10)
        N = N // 10
    print(lst)

def soucet_cislic():
    N = int(input("Zadej cislo: "))
    lst = []
    soucet = 0
    while N != 0:
        lst.append(N % 10)
        N = N // 10
    for i in range (len(lst)):
        soucet = soucet + lst[i]
    print(soucet)

if __name__ == "__main__":
    soucet_cislic()