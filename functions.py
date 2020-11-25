import random
import math
import sys
sys.setrecursionlimit(1500)

# быстрый поиск модуля от степени числа
def power(x, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 0:
        p = power(x, n / 2, mod)
        return (p * p) % mod
    else:
        return (x * power(x, n - 1, mod)) % mod

# генерация большого простого числа
def randPrime(n):
    rangeStart = 10 ** (n-1)
    rangeEnd = (10 ** n) - 1
    while True:
        num = random.randint(rangeStart, rangeEnd)
        if isPrime(num):
            return num

# определение простое ли число
def isPrime(num):
    if (num < 2):
        return False
    for prime in LOW_PRIMES:
        if (num == prime):
            return True
        if (num % prime == 0):
            return False
    return MillerRabin(num)

# решето Эратосфена
def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False # Zero and one are not prime numbers.
    sieve[1] = False
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)
    return primes

LOW_PRIMES = primeSieve(100)

# тест Миллера-Рабина
def MillerRabin(num):
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

# нахождение рандомного числа num при условии НОД(num, b) = 1
def randGcd1(b):
    rangeStart = 2
    rangeEnd = b - 1
    while True:
        num = random.randint(rangeStart, rangeEnd)
        if math.gcd(num, b) == 1:
            return num

# рекурентный алгоритм к КЦД
def fct(arr):
    global b
    if arr == []:
        return 'Null division', 0
    elif arr == [0.0]:
        return 0, b
    p = []
    q = []
    for i in range(len(arr)):
        q.append(0)
        p.append(0)
    p[0] = arr[0]
    p[1] = arr[0] * arr[1] + 1
    q[0] = 1
    q[1] = arr[1]
    for n in range(2,len(arr)):
        p[n] = arr[n] * p[n-1] + p[n-2]
        q[n] = arr[n] * q[n-1] + q[n-2]
    return p[-2], len(p)

# расширенный алгоритм Евклида
def gcdex(a, m, b = 1, d = 1):
    a //= d
    b //= d
    m //= d
    newM = m

    arr = []
    while m != 1:
        division = m // a
        arr.append(float(division))
        p = m
        m = a
        a = p - (p // a) * a

    pN_1, n = fct(arr)

    x0 = (((-1) ** (n - 1)) * pN_1 * b) % newM

    arrX = []
    for i in range(d):
        arrX.append(int(x0 + i * newM))
    return arrX

# перевод текста в массив чисел
def textToArray(text):
    textArray = []
    for i in text:
        textArray.append(ord(i))
    return textArray

# передача сообщения с помощью протокола Шамира
def messageTransmission(p, text):
    # генерация чисел для пользователей A и B
    x1Arr = []
    x2Arr = []
    y1Arr = []
    y2Arr = []
    for i in range(len(text)):
        x1Arr.append(randGcd1(p - 1))
        x2Arr.append(gcdex(x1Arr[i], p - 1)[0])
        y1Arr.append(randGcd1(p - 1))
        y2Arr.append(gcdex(y1Arr[i], p - 1)[0])
    print('A`s arrays of numbers : \n x1 : ', x1Arr, '\n x2 : ', x2Arr)
    print('B`s arrays of numbers : \n y1 : ', y1Arr, '\n y2 : ', y2Arr)
    print('\n')

    # перевод текста в массив чисел
    textArray = textToArray(text)
    print('Original A`s message : ', textArray)

    # первый шаг (пользователь А). После отправка пользователю B
    for i in range(len(textArray)):
        textArray[i] = step(textArray[i], x1Arr[i], p)
    print('first step (A -> B)  : ', textArray)

    # второй шаг (пользователь B). После отправка пользователю A
    for i in range(len(textArray)):
        textArray[i] = step(textArray[i], y1Arr[i], p)
    print('second step (B -> A) : ', textArray)

    # третий шаг (пользователь A). После отправка пользователю B
    for i in range(len(textArray)):
        textArray[i] = step(textArray[i], x2Arr[i], p)
    print('third step (A -> B)  : ', textArray)

    # пользователь B расшифровывает
    for i in range(len(textArray)):
        textArray[i] = step(textArray[i], y2Arr[i], p)
    print('B decrypted message  : ', textArray)

# шаг в протоколое Шамира
def step(text, num, p):
    return power(text, num, p)
