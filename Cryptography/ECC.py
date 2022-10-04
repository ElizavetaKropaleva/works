def prime_number(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return True
    return False


def gcd(a, b): #проверка на взаимную простоту
    while b != 0:
        a, b = b, a % b
    return a


def coprime(a, b): #если взаимнопростые True, иначе False
    return gcd(a, b) == 1


def eil_func(num): #функция Эйлера (от 1 до введенного числа); кол-во взаимнопростых чисел с тем, что ввели
    ans = 0
    for i in range(1, num):
        if coprime(i, num):
            ans += 1
    return ans


def mod_fraction_ecc(a, b, p, g_a): #вычисление лямбды для удвоения точки
    return ((a + g_a) % p) * ((b ** (eil_func(p) - 1)) % p) % p


def doubling_ecc(num1, num2, p, g_a): #удвоение точки
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


def addition_ecc(num1_1, num1_2, num2_1, num2_2, p): #сложение точек
    x1, y1 = num1_1, num1_2
    x1 = int(x1)
    y1 = int(y1)
    x2, y2 = num2_1, num2_2
    x2 = int(x2)
    y2 = int(y2)
    a = y2 - y1
    b = x2 - x1
    if b == 0:
        return 'O', 'O'
    else:
        l = (a % p) * ((b ** (eil_func(p) - 1)) % p) % p
        x3 = int((l * l - x1 - x2) % p)
        y3 = int((l * (x1 - x3) - y1) % p)
        return x3, y3


def el_gam_counting_ecc(k, dot1, dot2, p, g_a): #вычисление значения точки по секретному ключу [k]G
    if k % 2 == 0:
        x1, y1 = dot1, dot2
        x, y = doubling_ecc(dot1, dot2, p, g_a)
        while k > 2:
            dot1, dot2 = addition_ecc(dot1, dot2, x, y, p)
            k -= 2
        dot1, dot2 = addition_ecc(dot1, dot2, x1, y1, p)
    elif k % 2 != 0:
        x, y = doubling_ecc(dot1, dot2, p, g_a)
        while k > 1:
            dot1, dot2 = addition_ecc(dot1, dot2, x, y, p)
            k -= 2
    return dot1, dot2


def main():
    a = int(input('Введите коэффициент a: '))
    b = int(input('Введите коэффициент b: '))
    p = int(input('Введите модуль p: '))
    y_sqr_eql = [] #массив возможных y для вычисления q
    for x in range(p):
        y_dot = (x**3 + a*x + b) % p
        for y in range(p):
            if y**2 % p == y_dot:
                y_sqr_eql.append(y_dot)
                break
    n = int()
    possible_g = [] #массив допустимых точек эллиптической кривой
    for y in y_sqr_eql:
        for sqr_y in range(p):
            if sqr_y**2 % p == y:
                n += 1
                if sqr_y not in possible_g:
                    possible_g.append(sqr_y)
    q = int() #предел q
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
    c_alice = int(input(f'Введите k отправителя в пределе от 0 до {q}: ')) #выбор секретных ключей
    c_bob = int(input(f'Введите k получателя в пределе от 0 до {q}: '))
    dot1, dot2 = int(input('Введите a для точки G эллиптической кривой: ')), \
                 int(input('Введите b для точки G эллиптической кривой: '))
    while True:
        if dot1 not in possible_g and dot2 not in possible_g: #проверка на допустимость точки
            print('Введены недопустимые значения точки эллиптической кривой.')
            print(f'Допустимые значения: {possible_g}')
            dot1, dot2 = int(input('Введите a для точки G эллиптической кривой: ')), \
                         int(input('Введите b для точки G эллиптической кривой: '))
        else:
            break
    dot_b1, dot_b2 = el_gam_counting_ecc(c_bob, dot1, dot2, p, a)
    D = (dot_b1, dot_b2)
    print(f'D(b) = [C(b)]G = ({D[0]}, {D[1]})')
    m = int(input('Введите текст m < p: '))
    dot_a1, dot_a2 = el_gam_counting_ecc(c_alice, dot1, dot2, p, a)
    R = (dot_a1, dot_a2)
    print(f'R = [k]G = ({R[0]}, {R[1]})')
    dot_a1_1, dot_a2_1 = el_gam_counting_ecc(c_alice, D[0], D[1], p, a)
    P = (dot_a1_1, dot_a2_1)
    print(f'P = [k]D(b) = ({P[0]}, {P[1]})')
    e = (m * P[0]) % p
    print(f'Шифротекст: {R}, {e}')
    dot_b1_1, dot_b2_1 = el_gam_counting_ecc(c_bob, R[0], R[1], p, a)
    Q = (dot_b1_1, dot_b2_1)
    print(f'Q = [C(b)]R = ({Q[0]}, {Q[1]})')
    m = ((e % p) * (Q[0] ** (eil_func(p) - 1)) % p) % p
    print(f'Текст: {m}', '\n')


if __name__ == "__main__":
    main()
