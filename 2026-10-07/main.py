def year(number):
    return number % 400 == 0 or ((number % 4 == 0) and (number % 100 != 0))

def mean():
    x1 = (input("1: "))
    x2 = (input("2: "))
    x3 = (input("3: "))
    print(f"Vysledek je: {(x1+x2+x3)/3}")

def nums():
    N = int(input("Zadej cislo: "))
    for i in range(N):
        print(f"{i+1}")

    # N = int(input("Zadej cislo: "))
    # count = 0
    # for _ in range(N):
    #     count = count + 1
    #     print(f"{count}")

def even_sum():
    N = int(input("Zadej cislo: "))
    sum = 0
    for i in range(N + 1):
        if i % 2 == 0:
            sum += i
    print(f"sum: {sum}")

def backwards():
    N = int(input("Zadej cislo: "))
    for i in range(N):
        print(f"{N-1}")
    
def sum():
    N = int(input("Zadej cislo: "))
    sum = 0
    for i in range(N):
        sum = (N*(N+1) / 2)
    print(f"{sum}")

def minimum():
    N = int(input("Zadej cislo: "))

def suda():
    N = int(input("Zadej cislo: "))
    num = 0
    count = 0
    for i in range(N):
        if num % 2 == 0:
            count = count + 1
        num = num + 1
    print(f"{count - 1}")

def factorial():
    result = 1
    N = int(input("Zadej cislo: "))
    for i in range(1, N + 1):
        result = result + 1
    print(f"{result}")

def combination_num():
    N = int(input("Zadej cislo: "))
    k = int(input("Zadej cislo: "))
    print(factorial(0) / factorial(k) * (factorial(N - k)))

def obdelnik():
    a = int(input("Zadej stranu a: "))
    b = int(input("Zadej stranu b: "))

    O = 2*(a+b)
    S = a * b

    print(f"Obvod: {O}")
    print(f"Obsah: {S}")

def kruh():
    r = int(input("Zadej polomer: "))
    O = 2 * 3.14 * r
    S = 3.14 * r * r
    print(f"Obvod {O}")
    print(f"Obsah {S}")

def mocniny():
    a = int(input("Zadej cislo a: "))
    n = int(input("Zadej cislo n: "))
    sum = 1

    for i in range(n):
        sum *= a
    print(f"{sum}")

if __name__ == "__main__":
    mocniny()