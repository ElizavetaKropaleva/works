# Необходимые библиотеки
from math import gcd


# Функция вычисления D
def mod_fraction(a, b, Z):
    ost = a % Z
    for i in range (1000):
        if ((Z * i + ost) % b == 0):
            return (Z * i + ost) / b


# Проверка является число простым или нет
def prime_number(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            print('Введенное число не является простым. Введите простое число.')
            return True
    return False


# Функция шифрования и расшифрования
def encryption(text, alphabet, action):
    result = ''
    # Ввод необходимых параметров
    flag = True
    while flag:
        P = int(input('P = '))
        flag = prime_number(P)
    flag = True
    while flag:
        Q = int(input('Q = '))
        flag = prime_number(Q)
    N = P * Q
    f = (P - 1)*(Q - 1)
    flag = True
    while flag:
        E = int(input('E = '))
        flag = (gcd(E, f) != 1)
        if E > f:
            flag = True
    # Вычисление D
    D = int(mod_fraction(1, E, f))
    # Шифрование и расшифрование
    if action == 'encode':
        for i in text:
            sym = pow(alphabet.index(i), E) % N
            if sym < 10 :
                result += '0' + str(sym)
            else:
               result += str(sym)
    else:
        for i in range(0, len(text), 2):
            sym = int(text[i:i + 2])
            result += alphabet[pow(sym, D) % N]
    return result


def main():
    # Исходные данные для тестирования
    alphabet_test = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    test = 'небойсясобакибрехливойзптабойсямолчаливойтчк'
    result_test = '1331011481750575140100820801743121720832148163714400011481750538147204007208321481440482'  # ожидаемый результат шифрования

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
        result_encryption = encryption(test, alphabet_test, 'encode')
        print('Результат шифрования:', result_encryption)

        # Проверка совпадения с ожидаемым результатом
        check = bool(result_test == result_encryption)
        print('Результат проверки:', check)

        # Процесс расшифрования и вывод результата
        result_decryption = encryption(result_encryption, alphabet_test, 'decode')
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
        result_encryption = encryption(text, alphabet_text, 'encode')
        print('Результат шифрования:', result_encryption)

        # Процесс расшифрования и вывод результата
        result_decryption = encryption(result_encryption, alphabet_text, 'decode')
        print('\nРезультат расшифрования:', result_decryption)

        # Проверка совпадения с изначальным текстом
        check = bool(text == result_decryption)
        print('Результат проверки:', check, '\n')

    else:
        print('Введено неверное значение!', '\n')


if __name__ == "__main__":
    main()