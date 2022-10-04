import atbash_cipher, caesar_cipher, polybius_square, trithemia_cipher, belazo_cipher, vigener_cipher, matrix_cipher, playfair_cipher, vertical_permutation, cardano_grid, shannon_notebook,\
    A5_1, A5_2, MAGMA, KUZNECHIK, RSA, Elg, ECC, RSA_sig, elgamal_sig, GOST_P_34_10_94, GOST_P_34_11_2012, diffi


blok = 1
while blok != 0:
    blok = int(input('Выберете блок:'
                '\n1. Блок А: ШИФРЫ ОДНОЗНАЧНОЙ ЗАМЕНЫ'
                '\n2. Блок В: ШИФРЫ МНОГОЗНАЧНОЙ ЗАМЕНЫ'
                '\n3. Блок С: ШИФРЫ БЛОЧНОЙ ЗАМЕНЫ'
                '\n4. Блок D: ШИФРЫ ПЕРЕСТАНОВКИ'
                '\n5. Блок E: ШИФРЫ ГАММИРОВАНИЯ'
                '\n6. Блок F: ПОТОЧНЫЕ ШИФРЫ'
                '\n7. Блок G: КОМБИНАЦИОННЫЕ ШИФРЫ'
                '\n8. БЛОК H: АСИММЕТРИЧНЫЕ ШИФРЫ'
                '\n9. Блок I: АЛГОРИТМЫ ЦИФРОВЫХ ПОДПИСЕЙ'
                '\n10. Блок J: СТАНДАРТЫ ЦИФРОВЫХ ПОДПИСЕЙ'
                '\n11. БЛОК K: ОБМЕН КЛЮЧАМИ'
                '\n0. Выход'
                '\nВведите свой выбор: '))

    match blok:
        case 1:
            cipher = int(input('Выберете шифр:'
                '\n1. Шифр простой замены АТБАШ'
                '\n2. Шифр ЦЕЗАРЯ'
                '\n3. Квадрат Полибия'
                '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    atbash_cipher.main()
                case 2:
                    caesar_cipher.main()
                case 3:
                    polybius_square.main()
                case _:
                    print('Введено неверное значение!')
        case 2:
            cipher = int(input('Выберете шифр:'
                               '\n1. Шифр Тритемия'
                               '\n2. Шифр Белазо'
                               '\n3. Шифр Виженера'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    trithemia_cipher.main()
                case 2:
                    belazo_cipher.main()
                case 3:
                    vigener_cipher.main()
                case _:
                    print('Введено неверное значение!')
        case 3:
            cipher = int(input('Выберете шифр:'
                               '\n1. Матричный шифр'
                               '\n2. Шифр Плэйфера'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    matrix_cipher.main()
                case 2:
                    playfair_cipher.main()
                case _:
                    print('Введено неверное значение!')
        case 4:
            cipher = int(input('Выберете шифр:'
                               '\n1. Вертикальная перестановка'
                               '\n2. Решетка Кардано'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    vertical_permutation.main()
                case 2:
                    cardano_grid.main()
                case _:
                    print('Введено неверное значение!')
        case 5:
            cipher = int(input('Выберете шифр:'
                               '\n1. Одноразовый блокнот К.Шеннона'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    shannon_notebook.main()
                case _:
                    print('Введено неверное значение!')
        case 6:
            cipher = int(input('Выберете шифр:'
                               '\n1. А5 /1'
                               '\n2. А5 /2'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    A5_1.main()
                case 2:
                    A5_2.main()
                case _:
                    print('Введено неверное значение!')
        case 7:
            cipher = int(input('Выберете шифр:'
                               '\n1. МАГМА'
                               '\n2. КУЗНЕЧИК'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    MAGMA.main()
                case 2:
                    KUZNECHIK.main()
                case _:
                    print('Введено неверное значение!')
        case 8:
            cipher = int(input('Выберете шифр:'
                               '\n1. RSA'
                               '\n2. Elgamal'
                               '\n3. ECC'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    RSA.main()
                case 2:
                    Elg.main()
                case 3:
                    ECC.main()
                case _:
                    print('Введено неверное значение!')
        case 9:
            cipher = int(input('Выберете шифр:'
                               '\n1. RSA'
                               '\n2. El Gamal'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    RSA_sig.main()
                case 2:
                    elgamal_sig.main()
                case _:
                    print('Введено неверное значение!')
        case 10:
            cipher = int(input('Выберете шифр:'
                               '\n1. ГОСТ Р 34.10-94'
                               '\n2. ГОСТ Р 34.10-2012'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    GOST_P_34_10_94.main()
                case 2:
                    GOST_P_34_11_2012.main()
                case _:
                    print('Введено неверное значение!')
        case 11:
            cipher = int(input('Выберете шифр:'
                               '\n1. ОБМЕН КЛЮЧАМИ ПО ДИФФИ-ХЕЛЛМАНУ'
                               '\nВведите свой выбор: '))
            match cipher:
                case 1:
                    diffi.main()
                case _:
                    print('Введено неверное значение!')
        case _:
            print('Введено неверное значение!')
