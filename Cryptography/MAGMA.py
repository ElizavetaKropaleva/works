n = 32
alphabet = '0 0000 1 0001 2 0010 3 0011 4 0100 5 0101 6 0110 7 0111 8 1000 9 1001 a 1010 b 1011 c 1100 d 1101 e 1110 f 1111'
key = ['', 'ffeeddcc', 'bbaa9988', '77665544', '33221100', 'f0f1f2f3', 'f4f5f6f7', 'f8f9fafb', 'fcfdfeff', 'ffeeddcc',
       'bbaa9988', '77665544', '33221100', 'f0f1f2f3', 'f4f5f6f7', 'f8f9fafb', 'fcfdfeff', 'ffeeddcc', 'bbaa9988',
       '77665544', '33221100', 'f0f1f2f3', 'f4f5f6f7', 'f8f9fafb', 'fcfdfeff', 'fcfdfeff', 'f8f9fafb', 'f4f5f6f7',
       'f0f1f2f3', '33221100', '77665544', 'bbaa9988', 'ffeeddcc']
alp = '0123456789abcdef'
S = [['c', '4', '6', '2', 'a', '5', 'b', '9', 'e', '8', 'd', '7', '0', '3', 'f', '1'],  # таблица замены S блоков
     ['6', '8', '2', '3', '9', 'a', '5', 'c', '1', 'e', '4', '7', 'b', 'd', '0', 'f'],
     ['b', '3', '5', '8', '2', 'f', 'a', 'd', 'e', '1', '7', '4', 'c', '9', '6', '0'],
     ['c', '8', '2', '1', 'd', '4', 'f', '6', '7', '0', 'a', '5', '3', 'e', '9', 'b'],
     ['7', 'f', '5', 'a', '8', '1', '6', 'd', '0', '9', '3', 'e', 'b', '4', '2', 'c'],
     ['5', 'd', 'f', '6', '9', '2', 'c', 'a', 'b', '7', '8', '1', '4', '3', 'e', '0'],
     ['8', 'e', '2', '5', '6', '9', '1', 'c', 'f', '4', 'b', '0', 'd', 'a', '3', '7'],
     ['1', '7', 'e', 'd', '0', '5', '8', '3', '4', 'f', 'a', '6', '9', 'c', 'b', '2']]


# Преобразование из 16 в 2
def hex_to_bin(text):
    result = ''
    for i in text:
        index = alphabet.index(i)
        result += alphabet[index + 2:index + 6]
    return result


# Преобразование из 2 в 16
def bin_to_hex(text):
    result = ''
    for i in range(0, len(text), 4):
        index = alphabet.index(text[i:i + 4])
        result += alphabet[index - 2]
    return result


# Суммирование по модулю 2^32
def sum_mod_2_32(a, b):
    c = ''
    z = 0
    for i in range(n):
        num1 = int(a[n - i - 1])
        num2 = int(b[n - i - 1])
        c = str((num1 + num2 + z) % 2) + c
        z = (num1 + num2 + z) // 2
    return c


# Замена по S блоку
def replace_S_block(text):
    result = ''
    for i in range(len(text)):
        index = alp.index(text[i])
        result += S[7 - i][index]
    return result


# Сложение по модулю 2
def xor(a, b):
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result


# Циклический сдвиг на 11 бит
def shift(text):
    return text[11:] + text[:11]


# Режим простой замены
def simple_replacement_mode(text, atr, mode):
    L = hex_to_bin(text[:len(text) // 2])
    R = hex_to_bin(text[len(text) // 2:])
    if atr == 1:
        print('Раунд: 0')
        print('Результат раунда:', bin_to_hex(L), bin_to_hex(R))
    e = 1
    if mode == 2:
        e = -1
    for i in range(1, n + 1):
        k = hex_to_bin(key[e * i])
        z = sum_mod_2_32(R, k)  # суммирование по модулю 2^32
        z = hex_to_bin(replace_S_block(bin_to_hex(z)))  # замена по S-блоку и возвращение в двоичный формат
        z = shift(z)  # сдвиг на 11 бит
        z = xor(L, z)  # сложение по модулю 2
        L = R
        R = z
        if (atr == 1):
            print('Раунд:', (i + 1))
            print('Результат раунда:', bin_to_hex(L), bin_to_hex(R))
    return bin_to_hex(R) + bin_to_hex(L)


# Режим гаммирования с обратной связью по выходу
def output_feedback_gamming_mode(text, IV, CTR):
    # Формирование IV
    if CTR == 0:
        IV = IV[:16]
    if CTR == 1:
        IV = IV[16:]
    if CTR == 2:
        IV = simple_replacement_mode(IV[:16], 2, 1)
    if CTR == 3:
        IV = simple_replacement_mode(IV[16:], 2, 1)

    blok = simple_replacement_mode(IV, 2, 1)
    result = xor(hex_to_bin(text), hex_to_bin(blok))
    return bin_to_hex(result)


# Режим гаммирования
def gamming_mode(text, IV, CTR):
    IV += '0' * (16 - len(IV) - len(str(CTR))) + str(CTR)  # Формирование IV
    blok = simple_replacement_mode(IV, 2, 1)
    result = xor(hex_to_bin(text), hex_to_bin(blok))
    return bin_to_hex(result)

def main():
    # Меню
    while True:
        print(
            'МАГМА\n1. Режим простой замены\n2. Режим гаммирования\n3. Режим гаммирования с обратной связью по выходу\n4. Выход')
        a = int(input('Выбор (1-4): '))
        if a == 4:
            break
        print('Действие:\n1. Шифрование\n2. Расшифрование')
        b = int(input('Выбранное действие (1/2): '))

        if a == 1:
            print('Раунды:\n1. Показать \n2. Скрыть')
            atr = int(input('Выбор (1/2): '))
            for i in range(4):
                text = input('Введите текст: ')
                print('Результат:', simple_replacement_mode(text, atr, b), '\n')
        if a == 2:
            IV = input('IV = ')
            for i in range(4):
                text = input('Введите текст: ')
                print('Результат:', gamming_mode(text, IV, i), '\n')
        if a == 3:
            IV = input('IV = ')
            for i in range(4):
                text = input('Введите текст: ')
                print('Результат:', output_feedback_gamming_mode(text, IV, i), '\n')


if __name__ == "__main__":
    main()

