# Функция шифрования и расшифрования
def encryption(text, alphabet, key, mode, action):
    # Формирование матрицы-алфавита
    for i in key:
        alphabet = alphabet.replace(i, '')
    if (mode == 'test'):
        alphabet = alphabet.replace('й', '').replace('ъ', '')
        m, t = 6, 5
    else:
        m, t = 6, 6
    alphabet = key + alphabet
    # Вывод матрицы
    if action == 'encode':
        for i in range(t):
            for j in range(m):
                print(alphabet[i * m + j], end=' ')
            print()

    n = len(alphabet)
    result = ''
    z = 1
    if action == 'decode':
        z = -1
    for i in range(0, len(text), 2):
        if (i + 1 < len(text)):
            if text[i] == text[i + 1]:
                x1 = alphabet.index(text[i + 1]) // m
            x1 = alphabet.index(text[i]) // m
            y1 = alphabet.index(text[i]) % m
            x2 = alphabet.index(text[i + 1]) // m
            y2 = alphabet.index(text[i + 1]) % m
            if x1 == x2:
                result += alphabet[x1 * m + (alphabet.index(text[i]) + z * 1) % m]
                result += alphabet[x1 * m + (alphabet.index(text[i + 1]) + z * 1) % m]
            elif y1 == y2:
                result += alphabet[(x1 + z * 1) % t * m + y1]
                result += alphabet[(x2 + z * 1) % t * m + y1]
            else:
                result += alphabet[x1 * m + y2]
                result += alphabet[x2 * m + y1]

    return result


def main():
    # Исходные данные для тестирования
    alphabet_test = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    test = 'небойсясобакибрехливойзптабойсямолчаливойтчк'
    result_test = 'отжлтвщрлжкувгсрфмтимепшсджлтвьппмужмвелтеуо'  # ожидаемый результат шифрования

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

        key = input('Ключ = ')  # ключ шифрования при тестирования (shift = свитер)

        # Процесс шифрования и вывод результата
        result_encryption = encryption(test.replace('й', 'и'), alphabet_test, key, 'test', 'encode')
        print('Результат шифрования:', result_encryption)

        # Проверка совпадения с ожидаемым результатом
        check = bool(result_test == result_encryption)
        print('Результат проверки:', check)

        # Процесс расшифрования и вывод результата
        result_decryption = encryption(result_encryption, alphabet_test, key, 'test', 'decode')
        print('Результат расшифрования:', test)

        # Проверка совпадения с изначальным текстом
        check = bool(test.replace('й', 'и') == result_decryption)
        print('Результат проверки:', check, '\n')

    elif ch == 2:
        print('Исходные данные:\nАлфавит, использующийся для шифрования:', alphabet_text)
        print('Текст:', text, '\n')

        # Преобразование текста к нижнему регистру
        text = text.lower()
        key = input('Ключ = ')  # ключ шифрования при тестирования (shift = свитер)
        # Процесс шифрования и вывод результата
        result_encryption = encryption(text, alphabet_text, key, 'text', 'encode')
        print('Результат шифрования:', result_encryption)

        # Процесс расшифрования и вывод результата
        result_decryption = encryption(result_encryption, alphabet_text, key, 'text', 'decode') + '.'
        print('\nРезультат расшифрования:', result_decryption)

        # Проверка совпадения с изначальным текстом
        check = bool(text == result_decryption)
        print('Результат проверки:', check, '\n')

    else:
        print('Введено неверное значение!', '\n')


if __name__ == "__main__":
    main()

