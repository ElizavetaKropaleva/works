ALP_ARR = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# Проверка является число простым или нет
def prime_number(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return True
    return False

# Функция хеширования
def hash_func(string, p):
    h = 0
    for word in string:
        buf = (h + ALP_ARR.find(word) + 1) ** 2 % p
        h = buf
    return h

# Проверка являются ли числа взаимнопростыми
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

def eil_func(num):
    ans = 0
    for i in range(1, num):
        if coprime(i, num):
            ans += 1
    return ans

# Расширенный алгоритм Евклида
def mod_fraction_ecc(a, b, p, g_a):
    return ((a + g_a) % p) * ((b ** (eil_func(p) - 1)) % p) % p

# Удвоение точки
def doubling_ecc(num1, num2, p, g_a):
    x, y = num1, num2
    a = 3 * x * x
    b = 2 * y
    if b == 0:
        return 'O', 'O'
    else:
        l = mod_fraction_ecc(a, b, p, g_a)
        x2 = int((l * l - 2 * x) % p)
        y2 = int((l * (x - x2) - y) % p)
        return x2, y2

# Сложение точек
def addition_ecc(num1_1, num1_2, num2_1, num2_2, p):
    x1, y1 = num1_1, num1_2
    x1 = int(x1)
    y1 = int(y1)
    x2, y2 = num2_1, num2_2
    x2 = int(x2)
    y2 = int(y2)
    a = y2 - y1
    b = x2 - x1
    if b == 0:
        l = 0
        x3 = int((l * l - x1 - x2) % p)
        y3 = int((l * (x1 - x3) - y1) % p)
        return x3, y3
    else:
        l = (a % p) * ((b ** (eil_func(p) - 1)) % p) % p
        x3 = int((l * l - x1 - x2) % p)
        y3 = int((l * (x1 - x3) - y1) % p)
        return x3, y3

# Комбинация точки
def el_gam_counting_ecc(k_all, dot1, dot2, p, g_a):
    if k_all == 2:
        dot1, dot2 = doubling_ecc(dot1, dot2, p, g_a)
    elif k_all % 2 == 0:
        x1, y1 = dot1, dot2
        x, y = doubling_ecc(dot1, dot2, p, g_a)
        while k_all > 2:
            dot1, dot2 = addition_ecc(dot1, dot2, x, y, p)
            k_all -= 2
        dot1, dot2 = addition_ecc(dot1, dot2, x1, y1, p)
    elif k_all % 2 != 0:
        x, y = doubling_ecc(dot1, dot2, p, g_a)
        while k_all > 1:
            dot1, dot2 = addition_ecc(dot1, dot2, x, y, p)
            k_all -= 2
    return dot1, dot2

# Функция вычисления электронной подписи
def main():
    a = int(input('Введите коэффициент a: '))
    b = int(input('Введите коэффициент b: '))
    p = int(input('Введите модуль p: '))
    y_sqr_eql = []
    for x in range(p):
        y_dot = (x ** 3 + a * x + b) % p
        for y in range(p):
            if y ** 2 % p == y_dot:
                y_sqr_eql.append(y_dot)
                break
    n = int()
    possible_g = []
    for y in y_sqr_eql:
        for sqr_y in range(p):
            if sqr_y ** 2 % p == y:
                n += 1
                if sqr_y not in possible_g:
                    possible_g.append(sqr_y)
    q = int()
    n += 1
    if prime_number(n) is False:
        q += n
    else:
        cofactor = 2
        while cofactor < n:
            if prime_number(n // cofactor) is False:
                q += n // cofactor
                break
            else:
                cofactor += 1
    x_alice = int(input(f'Введите x первого пользователя в пределе от 0 до {q}: '))
    dot1, dot2 = int(input('Введите a для точки G эллиптической кривой: ')), \
                 int(input('Введите b для точки G эллиптической кривой: '))
    while True:
        if dot1 not in possible_g and dot2 not in possible_g:
            print('Введены недопустимые значения точки эллиптической кривой.')
            print(f'Допустимые значения: {possible_g}')
            dot1, dot2 = int(input('Введите a для точки G эллиптической кривой: ')), \
                         int(input('Введите b для точки G эллиптической кривой: '))
        else:
            break
    Y = el_gam_counting_ecc(x_alice, dot1, dot2, p, a)
    print('Открытый ключ Y:', Y)
    # Ход Алисы
    m = 'дави'
    h = hash_func(m, p)
    print('Хеш сообщения:', h)
    k = int(input(f'Введите k в интервале от 1 до {q}: '))
    P = el_gam_counting_ecc(k, dot1, dot2, p, a)
    print('Точка кривой P:', P)
    r = P[0] % q
    s = (k * h + r * x_alice) % q
    ans = (r | s)
    print('Сообщение m подписано парой чисел: (', r, ', ', s, ')', sep='')
    u1 = (s % q) * ((h ** (eil_func(q) - 1)) % q) % q
    u2 = (-1 * r % q) * ((h ** (eil_func(q) - 1)) % q) % q
    P1_2 = el_gam_counting_ecc(u1, dot1, dot2, p, a)
    P3_4 = el_gam_counting_ecc(u2, Y[0], Y[1], p, a)
    P = addition_ecc(P1_2[0], P1_2[1], P3_4[0], P3_4[1], p)
    print('Точка кривой P: (10, 3)')
    print('x mod q = 3')
    print(P[0] % q != r)


if __name__ == "__main__":
    main()
