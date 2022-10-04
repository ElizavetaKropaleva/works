# Необходимые библиотеки
import random as rd


# Функция шифрования и расшифрования
def encryption(text, alphabet, action):
    # функция шифрования
    if action == 'encode':
        result = ''
        ans_jail = [['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '']]
        kardano_jail_step1 = [['', 0, '', '', '', '', '', '', '', ''],
                              [0, '', '', '', 0, '', 0, 0, '', ''],
                              ['', 0, '', '', '', 0, '', '', '', 0],
                              ['', '', '', 0, '', '', '', 0, '', ''],
                              ['', 0, '', '', '', '', '', '', '', ''],
                              ['', '', 0, '', '', 0, 0, '', '', 0]]
        if len(text) % 60 != 0:
            extr_text = len(text)
            for count_extra in range(60 - (extr_text % 60)):
                text += alphabet[rd.randint(0, 31)]
        check_letter = 0
        while True:
            kardano_jail_step2 = []
            kardano_jail_step3 = []
            kardano_jail_step4 = []
            for arr in range(len(kardano_jail_step1)):
                for elem in range(len(kardano_jail_step1[0])):
                    if kardano_jail_step1[arr][elem] == 0:
                        ans_jail[arr][elem] = text[check_letter]
                        check_letter += 1
            # Первый разворот решетки
            for arr in kardano_jail_step1:
                kardano_jail_step2.append(arr[::-1])
            for arr in range(len(kardano_jail_step2)):
                for elem in range(len(kardano_jail_step2[0])):
                    if kardano_jail_step2[arr][elem] == 0:
                        ans_jail[arr][elem] = text[check_letter]
                        check_letter += 1
                # Второй разворот решетки
                kardano_jail_step3 = kardano_jail_step2[::-1]
            for arr in range(len(kardano_jail_step3)):
                for elem in range(len(kardano_jail_step3[0])):
                    if kardano_jail_step3[arr][elem] == 0:
                        ans_jail[arr][elem] = text[check_letter]
                        check_letter += 1
            # Третий разворот решетки
            for arr in kardano_jail_step3:
                kardano_jail_step4.append(arr[::-1])
            for arr in range(len(kardano_jail_step4)):
                for elem in range(len(kardano_jail_step4[0])):
                    if kardano_jail_step4[arr][elem] == 0:
                        ans_jail[arr][elem] = text[check_letter]
                        check_letter += 1
            for arr in ans_jail:
                for elem in arr:
                    result += elem
            if check_letter == len(text):
                return result
    else:
        result = ''
        ans_jail = [['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '']]
        kardano_jail_step1 = [['', 0, '', '', '', '', '', '', '', ''],
                              [0, '', '', '', 0, '', 0, 0, '', ''],
                              ['', 0, '', '', '', 0, '', '', '', 0],
                              ['', '', '', 0, '', '', '', 0, '', ''],
                              ['', 0, '', '', '', '', '', '', '', ''],
                              ['', '', 0, '', '', 0, 0, '', '', 0]]
        check_letter = 0
        while True:
            kardano_jail_step2 = []
            kardano_jail_step3 = []
            kardano_jail_step4 = []
            for arr in range(len(ans_jail)):
                for elem in range(len(ans_jail[arr])):
                    ans_jail[arr][elem] = text[check_letter]
                    check_letter += 1
            for arr in range(len(kardano_jail_step1)):
                for elem in range(len(kardano_jail_step1[0])):
                    if kardano_jail_step1[arr][elem] == 0:
                        result += ans_jail[arr][elem]
            # Первый разворот решетки
            for arr in kardano_jail_step1:
                kardano_jail_step2.append(arr[::-1])
            for arr in range(len(kardano_jail_step2)):
                for elem in range(len(kardano_jail_step2[0])):
                    if kardano_jail_step2[arr][elem] == 0:
                        result += ans_jail[arr][elem]
                # Второй разворот решетки
                kardano_jail_step3 = kardano_jail_step2[::-1]
            for arr in range(len(kardano_jail_step3)):
                for elem in range(len(kardano_jail_step3[0])):
                    if kardano_jail_step3[arr][elem] == 0:
                        result += ans_jail[arr][elem]
            # Третий разворот решетки
            for arr in kardano_jail_step3:
                kardano_jail_step4.append(arr[::-1])
            for arr in range(len(kardano_jail_step4)):
                for elem in range(len(kardano_jail_step4[0])):
                    if kardano_jail_step4[arr][elem] == 0:
                        result += ans_jail[arr][elem]
            if check_letter == len(text):
                return result


def main():
    # Исходные данные для тестирования
    alphabet_test = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    test = 'небойсясобакибрехливойзптабойсямолчаливойтчк'
    result_test = 'янамозалеюевхлбиойчвосаьйялэзсилповстбокуайтжчзиакбукойибслр'  # ожидаемый результат шифрования

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
        print('Результат расшифрования:', result_decryption)

        # Проверка совпадения с изначальным текстом
        check = bool(test == result_decryption[:-1])
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


