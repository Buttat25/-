import random

print("Игра Перудо.")

player_dice = [random.randint(1, 6) for _ in range(6)]
comp_dice = [random.randint(1, 6) for _ in range(6)]

print(f"Результат броска игрока: {player_dice}")
print("Кости компьютера брошены. Они скрыты.")

count = 0
value = 0

while True:
    print("\nХод пользователя.")
    action = input("Ввод ставки (количество,номинал) или 'н' (не верю): ").strip().lower()
    
    if action == 'н':
        print(f"Заявлено 'Не верю' на ставку: {count} шт., номинал {value}.")
        break
    else:
        n, m = map(int, action.split(','))
        
        if n > count or (n == count and m > value):
            count = n
            value = m
        else:
            print("Ошибка: ставка должна быть выше предыдущей.")
            continue

    print("\nХод компьютера.")
    if count > 3 and random.random() < 0.35:
        print(f"Компьютер объявил 'Не верю' на ставку: {count} шт., номинал {value}.")
        break
    else:
        if random.choice([True, False]) or value == 6:
            count += 1
        else:
            value += 1
        print(f"Новая ставка компьютера: {count} шт., номинал {value}.")

print("\nИгра завершена. Вскрытие костей.")
print(f"Кости игрока: {player_dice}")
print(f"Кости компьютера: {comp_dice}")

all_dice = player_dice + comp_dice
real_count = all_dice.count(value)
print(f"Фактическое количество номинала {value} на столе: {real_count}")

if real_count >= count:
    print(f"Ставка ({count} шт.) подтвердилась.")
    if action == 'н':
        print("Победа компьютера (пользователь ошибся).")
    else:
        print("Победа пользователя (компьютер ошибся).")
else:
    print(f"Ставка ({count} шт.) не подтвердилась (блеф).")
    if action == 'н':
        print("Победа пользователя.")
    else:
        print("Победа компьютера.")
