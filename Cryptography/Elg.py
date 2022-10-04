# Необходимые библиотеки
from math import gcd
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


# Формирование списка рандомизаторов
def randomizers(p, length):
    arr_k = []
    n = int(input('Количество рандомизаторов: '))
    for i in range(n):
        z = 0
        flag = True
        while flag:
            s = 'k' + str(i + 1) + ': '
            z = int(input(s))
            flag = (gcd(z, (p - 1)) != 1)
        arr_k.append(z)
    k = []
    for i in range(length):
        k.append(random.choice(arr_k))
    return k


# Функция шифрования
def encryption(text, alphabet, k, mode):
    result = ''
    flag = True
    while flag:
        P = int(input('P = '))
        flag = prime_number(P)
    flag = True
    while flag:
        x = int(input('x = '))
        flag = range_p(x, P)
    flag = True
    while flag:
        g = int(input('g = '))
        flag = range_p(g, P)
    y = pow(g, x) % P
    if mode == 'text':
        k = randomizers(P, len(text))
    for i in range(len(text)):
        a = pow(g, k[i]) % P
        b = (pow(y, k[i]) * alphabet.index(text[i])) % P
        if a < 10:
            result += "0" + str(a)
        else:
            result += str(a)
        if b < 10:
            result += "0" + str(b)
        else:
            result += str(b)
    return result


# Функция расшифрования
def decryption(text, alphabet):
    result = ''
    flag = True
    while flag:
        P = int(input('P = '))
        flag = prime_number(P)
    flag = True
    while flag:
        x = int(input('x = '))
        flag = range_p(x, P)
    for i in range(0, len(text), 4):
        a = int(text[i:i + 2])
        b = int(text[i + 2:i + 4])
        ind = b * (a ** (P - 1 - x) % P) % P
        result += alphabet[ind]
    return result


def main():
    # Исходные данные для тестирования
    alphabet_test = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    test = 'небойсясобакибрехливойзптабойсямолчаливойтчк'
    result_test = '16250412163535090413163635230415042516351600042435420411160104123535350404021627350916141630352535301600041104253515041504403520350904350438040004353542353204253515162816313531'  # ожидаемый результат шифрования
    k_test = [73, 5, 73, 25, 5, 73, 25, 5, 5, 73, 73, 5, 25, 5, 73, 5, 25, 25, 5, 73, 25, 73, 73, 25, 25, 73, 5, 5, 25, 5, 5, 25, 25, 5, 5, 5, 5, 25, 25, 5, 25, 73, 73, 25]  # рандомизаторы, используемые для тестирования

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
        print('Ожидаемый результат шифрования:', result_test, '\n')

        # Процесс шифрования и вывод результата
        result_encryption = encryption(test, alphabet_test, k_test, 'test')
        print('Результат шифрования:', result_encryption)

        # Проверка совпадения с ожидаемым результатом
        check = bool(result_test == result_encryption)
        print('Результат проверки:', check)

        # Процесс расшифрования и вывод результата
        result_decryption = decryption(result_encryption, alphabet_test)
        print('Результат расшифрования:', test)

        # Проверка совпадения с изначальным текстом
        check = bool(test == result_decryption)
        print('Результат проверки:', check, '\n')

    elif ch == 2:
        print('Исходные данные:\nАлфавит, использующийся для шифрования:', alphabet_text)
        print('Текст:', text, '\n')

        # Преобразование текста к нижнему регистру
        text = text.lower()

        # Процесс шифрования и вывод результата
        result_encryption = encryption(text, alphabet_text, [], 'text')
        print('Результат шифрования:', result_encryption)

        # Процесс расшифрования и вывод результата
        result_decryption = decryption(result_encryption, alphabet_text)
        print('\nРезультат расшифрования:', result_decryption)

        # Проверка совпадения с изначальным текстом
        check = bool(text == result_decryption)
        print('Результат проверки:', check, '\n')

    else:
        print('Введено неверное значение!', '\n')


if __name__ == "__main__":
    main()