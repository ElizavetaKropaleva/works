def check_keys(n):
    while True:
        if n < 3:
            print(f'{n} меньше или равно 2, введите значение повторно')
            n = int(input('Введите n больше 2: '))
        else:
            break
    a = int(input(f'Введите a больше 1 и меньше {n}: '))
    while True:
        if a < 2 or n < a:
            print(f'{a} меньше 2 или больше n, введите значение повторно')
            a = int(input(f'Введите a больше 1 и меньше {n}: '))
        else:
            break
    Ka = int(input(f'Введите Ka больше 1 и меньше {n}: '))
    while True:
        if Ka < 2 or Ka > n - 1:
            print(f'{Ka} меньше 2 или больше {n - 1}, введите значение повторно')
            Ka = int(input(f'Введите Ka больше 1 и меньше {n}: '))
        else:
            break
    Kb = int(input(f'Введите Kb больше 1 и меньше {n}: '))
    while True:
        if Kb < 2 or Kb > n - 1:
            print(f'{Kb} меньше 2 или больше {n - 1}, введите значение повторно')
            Kb = int(input(f'Введите Kb больше 1 и меньше {n}: '))
        else:
            break
    return a, Ka, Kb


def main():
    n = int(input('Введите n больше 2: '))
    a, Ka, Kb = check_keys(n)
    Ya = a ** Ka % n
    Yb = a ** Kb % n
    print('Произошел обмен ключами')
    K_a = Yb ** Ka % n
    K_b = Ya ** Kb % n
    while K_a == 1 or K_b == 1:
        print('Ключи равны значению 1. Измените значение секретного ключа')
        Ka = int(input(f'Введите Ka больше 1 и меньше {n}: '))
        while True:
            if Ka < 2 or Ka > n - 1:
                print(f'{Ka} меньше 2 или больше {n - 1}, введите значение повторно')
                Ka = int(input(f'Введите Ka больше 1 и меньше {n}: '))
            else:
                break
        Ya = a ** Ka % n
        Yb = a ** Kb % n
        print('Произошел обмен ключами')
        K_a = Yb ** Ka % n
        K_b = Ya ** Kb % n

    print(K_a, K_b, '\n')


if __name__ == "__main__":
    main()
