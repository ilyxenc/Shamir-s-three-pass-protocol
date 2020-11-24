import functions as fn

# выбор случайного числа
p = fn.randPrime(5)

# пользователь A выбирает числа x1 и x2
x1 = fn.randGcd1(p - 1)
x2 = fn.gcdex(x1, p - 1)[0]
print('Random prime number : ', p)
print('x1 : ', x1, ', x2 : ', x2)

# пользователь B выбирает числа y1 и y2
y1 = fn.randGcd1(p - 1)
y2 = fn.gcdex(y1, p - 1)[0]
print('y1 : ', y1, ', y2 : ', y2, '\n')

# сообщение пользователя A для пользователя B
M = ord('H')
print('Original A`s message : ', M)

# шифрование по схеме Шамира

# первый шаг (пользователь А). После отправка пользователю B
X1 = fn.power(M, x1, p)
print('first step (A -> B)  : ', X1)

# второй шаг (пользователь B). После отправка пользователю A
Y1 = fn.power(X1, y1, p)
print('second step (B -> A) : ', Y1)

# третий шаг (пользователь A). После отправка пользователю B
X2 = fn.power(Y1, x2, p)
print('third step (A -> B)  : ', X2)

# пользователь B расшифровывает
Y2 = fn.power(X2, y2, p)
print('B decrypted message  : ', Y2)
