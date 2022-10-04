# Необходимые библиотеки
import random


# Проверка является число простым или нет
def prime_number(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            print('Введенное число не является простым. Введите простое число.')
            return True
    return False


# Проверка входит ли число в заданный диапазон
def range_p(a, p):
    if a > 1 and a < p:
        return False
    else:
        print('Число не подходит в числовой диапазон (1; P)')
        return True


# Функция хеширования
def hash(text, alphabet, p):
    h = 0
    for i in text:
        h = (h + alphabet.index(i) + 1) ** 2 % p
    print('Xэш-образ сообщения h =', h)
    return h


# Расширенный алгоритм Евклида
def mod_fraction(a, b, Z):
    ost = a % Z
    for i in range(1000):
        if ((Z * i + ost) % b == 0):
            return (Z * i + ost) / b


# Функция шифрования
def encryption(text, alphabet, mode):
    flag = True
    while flag:
        P = int(input('P = '))
        flag = prime_number(P)
    flag = True
    while flag:
        Q = int(input('Q = '))
        flag = prime_number(Q)
    flag = True
    while flag:
        a = int(input('a = '))
        flag = (a ** Q % P != 1)
    flag = True
    while flag:
        x = int(input('x = '))
        flag = (x >= Q)
    y = pow(a, x) % P
    m = hash(text, alphabet, P)
    if m == 0:
        m = 1
    if mode == 'text':
        flag = True
        while flag:
            k = random.randint(2, Q)
            r = (a ** k % P) % Q
            flag = (r == 0)
    else:
        flag = True
        while flag:
            k = int(input('k = '))
            flag = (k >= Q)
        r = (a ** k % P) % Q
    s = (x * r + k * m) % Q
    a = r % (2 ** 256)
    b = s % (2 ** 256)
    result = (a, b)
    return result


# Функция расшифрования
def decryption(text, alphabet, r, s):
    flag = True
    while flag:
        P = int(input('P = '))
        flag = prime_number(P)
    flag = True
    while flag:
        Q = int(input('Q = '))
        flag = prime_number(Q)
    flag = True
    while flag:
        a = int(input('a = '))
        flag = (a ** Q % P != 1)
    flag = True
    while flag:
        x = int(input('x = '))
        flag = (x >= Q)
    y = pow(a, x) % P
    m = hash(text, alphabet, P)
    v = m ** (Q - 2) % Q
    z1 = (s * v) % Q
    z2 = ((Q - r) * v) % Q
    u = ((a ** z1 * y ** z2) % P) % Q
    if u == r:
        print('u =', u)
        print('r =', r)
        print('Подпись верна\n')
    else:
        print('u =', u)
        print('r =', r)
        print('Неверная подпись\n')

def main():
    # Исходные данные для тестирования
    alphabet_test = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    test = 'небойсясобакибрехливойзптабойсямолчаливойтчк'
    result_test = (2, 3)  # ожидаемый результат шифрования

    # Исходные данные для шифрования текста
    alphabet_text = alphabet_test + ' ,.-'  # расширенный алфавит
    text = 'Когда-то небо было маленьким, и тогда оно было все на виду, и, чтоб его рассмотреть, не нужно было никаких телескопов. Небо было маленькое, и звезды на нем были маленькие, и Солнце, и Луна. И все это вертелось вокруг Земли, которая одна в то время была большая. Много было забот с этим маленьким небом. То оно в тучах, то в молниях, то потемнеет средь бела дня, то всю ночь светится - не угомонится. И Земля затмевалась его затмениями и обливалась его дождями - потому что она, Земля, была большая, а небо было еще маленькое. Но прошли годы, и небо выросло. Теперь оно не вертится возле Земли, а Земля вертится по его небесным законам. И если раньше оно было все на виду, то теперь за ним не уследишь в самые, мощные телескопы. Но Земля есть Земля, и она по-прежнему затмевается его затмениями и обливается его дождями, да еще сокрушается его катастрофами, которые, как это всегда бывает, доходят до нее через тысячи световых лет. Маленькое небо - маленькие хлопоты, большое небо - большие хлопоты. Небо теперь очень большое, поэтому так много хлопот у Земли.'

    ch = int(input('Что выполнить:'
                   '\n1. Тестирование'
                   '\n2. Работа с текстом не менее 1000 знаков'
                   '\nВведите свой выбор: '))
    if ch == 1:
        print('Исходные данные:\nАлфавит, использующийся для тестирования:', alphabet_test)
        print('Пословица, использующаяся для тестирования:', test)
        print('Ожидаемый результат:', result_test, '\n')

        # Процесс шифрования и вывод результата
        result_encryption = encryption(test, alphabet_test, 'test')
        print('Электронная цифровая подпись S =', result_encryption)

        # Проверка совпадения с ожидаемым результатом
        check = bool(result_test == result_encryption)
        print('Результат проверки:', check)

        # Процесс расшифрования и вывод результата
        result_decryption = decryption(test, alphabet_test, result_encryption[0], result_encryption[1])

    elif ch == 2:
        print('Исходные данные:\nАлфавит, использующийся для шифрования:', alphabet_text)
        print('Текст:', text, '\n')

        # Преобразование текста к нижнему регистру
        text = text.lower()

        # Процесс шифрования и вывод результата
        result_encryption = encryption(text, alphabet_text, 'text')
        print('Электронная цифровая подпись S =', result_encryption)

        # Процесс расшифрования и вывод результата
        result_decryption = decryption(text, alphabet_text, result_encryption[0], result_encryption[1])

    else:
        print('Введено неверное значение!', '\n')


if __name__ == "__main__":
    main()

