# Необходимые библиотеки
import numpy as np
from numpy import linalg as LA
import random


# Функция шифрования
def encryption(text, alphabet, matrix, mode):
    n = len(alphabet)
    result = ''
    # Проверка кратности и добавление символов
    if mode == 'test':
        text += 'а'
    if len(text) % 3 != 0:
        for i in range(len(text) % 3):
            index = random.randint(0, n)
            text += alphabet[index]
    for i in range(0, len(text), 3):

        if (i + 2 < len(text)):
            arr = np.array([[alphabet.index(text[i])], [alphabet.index(text[i + 1])], [alphabet.index(text[i + 2])]])
            total = matrix.dot(arr)
            result += str(total[0][0]) + ' ' + str(total[1][0]) + ' ' + str(total[2][0]) + ' '
    return (result)


# Функция расшифрования
def decryption(text, alphabet, matrix):
    n = len(alphabet)
    result = ''
    # Формирование обратной матрицы
    inverse_matrix = LA.inv(matrix)
    mes = text.split()
    for i in range(0, len(mes), 3):
        if (i + 2 < len(mes)):
            arr = np.array([[int(mes[i])], [int(mes[i + 1])], [int(mes[i + 2])]])
            total = inverse_matrix.dot(arr)
            result += alphabet[round(total[0][0])] + alphabet[round(total[1][0])] + alphabet[round(total[2][0])]
    return (result)


def main():
    # Исходные данные для тестирования
    alphabet_test = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    test = 'этакапустазеленаязптвсеравночтозеленаякапустатчк'
    result_test = '77 117 90 198 181 212 270 324 301 75 38 76 153 114 161 123 115 128 140 110 148 157 131 166 97 147 115 198 181 212 265 314 296 78 134 89 77 110 88 205 184 219 125 204 148 '  # ожидаемый результат шифрования

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

        # Ввод матрицы 3*3 (5 1 7 8 2 3 6 1 7)
        flag = True
        while flag:
            entries = list(map(int, input('Введите матрицу 3*3 (формат: одна строка разделенная пробелом): ').split()))
            matrix = np.array(entries).reshape(3, 3)
            det = LA.det(matrix)  # вычисление определителя
            flag = (det == 0)  # если определитель равен 0, то обратной матрицы не существует
            if flag:
                print('Обратной матрицы не существует!')

        # Процесс шифрования и вывод результата
        result_encryption = encryption(test, alphabet_test, matrix, 'test')
        print('Результат шифрования:', result_encryption)

        # Проверка совпадения с ожидаемым результатом
        check = bool(result_test == result_encryption)
        print('Результат проверки:', check)

        # Процесс расшифрования и вывод результата
        result_decryption = decryption(result_encryption, alphabet_test, matrix)
        print('Результат расшифрования:', result_decryption)

        # Проверка совпадения с изначальным текстом
        check = bool(test == result_decryption[:-1])
        print('Результат проверки:', check, '\n')

    elif ch == 2:
        print('Исходные данные:\nАлфавит, использующийся для шифрования:', alphabet_text)
        print('Текст:', text, '\n')

        # Ввод матрицы 3*3 (5 1 7 8 2 3 6 1 7)
        flag = True
        while flag:
            entries = list(map(int, input('Введите матрицу 3*3 (формат: одна строка разделенная пробелом): ').split()))
            matrix = np.array(entries).reshape(3, 3)
            det = LA.det(matrix)  # вычисление определителя
            flag = (det == 0)  # если определитель равен 0, то обратной матрицы не существует
            if flag:
                print('Обратной матрицы не существует!')

        # Преобразование текста к нижнему регистру
        text = text.lower()

        # Процесс шифрования и вывод результата
        result_encryption = encryption(text, alphabet_text, matrix, 'text')
        print('Результат шифрования:', result_encryption)

        # Процесс расшифрования и вывод результата
        result_decryption = decryption(result_encryption, alphabet_text, matrix)
        print('\nРезультат расшифрования:', result_decryption)

        # Проверка совпадения с изначальным текстом
        check = bool(text == result_decryption)
        print('Результат проверки:', check, '\n')

    else:
        print('Введено неверное значение!', '\n')


if __name__ == "__main__":
    main()



