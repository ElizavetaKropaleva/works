# Необходимые библиотеки
import re
import copy

# Глобальные переменные
reg_x_length = 19
reg_y_length = 22
reg_z_length = 23
key_one = ""
reg_x = []
reg_y = []
reg_z = []


# Заполнение регистров с использованием ключа
def loading_registers(key):
    for i in range(reg_x_length):
        reg_x.insert(i, int(key[i]))
    for i in range(reg_y_length):
        reg_y.insert(i, int(key[i + reg_x_length]))
    for i in range(reg_z_length):
        reg_z.insert(i, int(key[i + reg_y_length + reg_x_length]))


# Установка ключа и заполнение регистров
def set_key(key):
    if len(key) == 64 and re.match("^([01])+", key):
        key_one = key
        loading_registers(key)
        return True
    return False


def get_key():
    return key_one


# Преобразование в двоичный формат
def to_binary(text, alphabet):
    s = ""
    i = 0
    for i in text:
        binary = str(' '.join(format(128 + alphabet.find(x), 'b') for x in i))
        s += binary
    binary_values = []
    for i in range(len(s)):
        binary_values.insert(i, int(s[i]))
    return binary_values


# Функция тактирования
def get_majority(x, y, z):
    if x + y + z > 1:
        return 1
    else:
        return 0


# Вычисление регистров (XOR отдельных битов)
def get_keystream(length):
    reg_x_temp = copy.deepcopy(reg_x)
    reg_y_temp = copy.deepcopy(reg_y)
    reg_z_temp = copy.deepcopy(reg_z)
    keystream = []
    i = 0
    while i < length:
        majority = get_majority(reg_x_temp[8], reg_y_temp[10], reg_z_temp[10])
        if reg_x_temp[8] == majority:
            new = reg_x_temp[13] ^ reg_x_temp[16] ^ reg_x_temp[17] ^ reg_x_temp[18]
            reg_x_temp_two = copy.deepcopy(reg_x_temp)
            j = 1
            while j < len(reg_x_temp):
                reg_x_temp[j] = reg_x_temp_two[j - 1]
                j = j + 1
            reg_x_temp[0] = new

        if reg_y_temp[10] == majority:
            new_one = reg_y_temp[20] ^ reg_y_temp[21]
            reg_y_temp_two = copy.deepcopy(reg_y_temp)
            k = 1
            while k < len(reg_y_temp):
                reg_y_temp[k] = reg_y_temp_two[k - 1]
                k = k + 1
            reg_y_temp[0] = new_one

        if reg_z_temp[10] == majority:
            new_two = reg_z_temp[7] ^ reg_z_temp[20] ^ reg_z_temp[21] ^ reg_z_temp[22]
            reg_z_temp_two = copy.deepcopy(reg_z_temp)
            m = 1
            while m < len(reg_z_temp):
                reg_z_temp[m] = reg_z_temp_two[m - 1]
                m = m + 1
            reg_z_temp[0] = new_two

        keystream.insert(i, reg_x_temp[18] ^ reg_y_temp[21] ^ reg_z_temp[22])
        i = i + 1
    return keystream


# Преобразование в строку
def convert_binary_to_str(binary, alphabet):
    s = ""
    length = len(binary) - 8
    i = 0
    while i <= length:
        s = s + alphabet[int(binary[i:i + 8], 2) - 128]
        i = i + 8
    return str(s)


# Функция шифрования
def encryption(text, alphabet):
    result = ""
    binary = to_binary(text, alphabet)
    keystream = get_keystream(len(binary))
    for i in range(len(binary)):
        result += str(binary[i] ^ keystream[i])
    return result


# Функция расшифрования
def decryption(text, alphabet):
    result = ""
    binary = []
    keystream = get_keystream(len(text))
    for i in range(len(text)):
        binary.insert(i, int(text[i]))
        result += str(binary[i] ^ keystream[i])
    return convert_binary_to_str(str(result), alphabet)


# Ввод ключа
def input_key():
    tha_key = str(input('Введите ключ (64 бит): '))
    if len(tha_key) == 64 and re.match("^([01])+", tha_key):
        return tha_key
    else:
        while len(tha_key) != 64 and not re.match("^([01])+", tha_key):
            if len(tha_key) == 64 and re.match("^([01])+", tha_key):
                return tha_key
            tha_key = str(input('Введите ключ (64 бит): '))
    return tha_key


def main():
    # Исходные данные для тестирования
    alphabet_test = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    test = 'небойсясобакибрехливойзптабойсямолчаливойтчк'
    result_test = '0001010100001111011000000001101011111101010010001010011111111000001010110111001000101111010011110001010111111000011000111011011001010101011101010000010011001010110010100001001001101001010101000010010110000010110010100110010001000110100010101110100110000110010100010100000011000110110100001110011101011110000010001110100000101001001011010101010111111011'  # ожидаемый результат шифрования

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
        key = str(input_key())  # Используется ключ: 0101001000011010110001110001100100101001000000110111111010110111
        set_key(key)
        result_encryption = encryption(test, alphabet_test)
        print('Результат шифрования:', result_encryption)

        # Проверка совпадения с ожидаемым результатом
        check = bool(result_test == result_encryption)
        print('Результат проверки:', check, '\n')

    elif ch == 2:
        print('Исходные данные:\nАлфавит, использующийся для шифрования:', alphabet_text)
        print('Текст:', text, '\n')

        # Преобразование текста к нижнему регистру
        text = text.lower()

        key = str(input_key())  # Используется ключ: 0101001000011010110001110001100100101001000000110111111010110111
        set_key(key)

        # Процесс шифрования и вывод результата
        result_encryption = encryption(text, alphabet_text)
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


