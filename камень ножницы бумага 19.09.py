import random

items = ["камень", "ножницы", "бумага"]

player_wins = 0
computer_wins = 0
draws = 0
print("Игра камень, ножницы, бумага.")

while True:
    player_choice = input("\nВведите ваш ход (камень, ножницы или бумага): ").lower().strip()

    if player_choice not in items:
        print("Ошибка, вы ввели что-то не то. Выберите: камень, ножницы или бумага.")
        continue
    computer_choice = random.choice(items)
    print(f"Компьютер выбрал: {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья в этом раунде!")
        draws += 1

    elif (player_choice == "камень" and computer_choice == "ножницы") or \
        (player_choice == "ножницы" and computer_choice == "бумага") or \
        (player_choice == "бумага" and computer_choice == "камень"):
        print("Ура! Вы победили в этом раунде!")
        player_wins += 1

    else:
        print("Компьютер победил в этом раунде!")
        computer_wins += 1

    print(f"Статистика: вы победили: {player_wins} | компьютер победил: {computer_wins} | ничьих: {draws}")

    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower().strip()

    if play_again == "нет":
        print("\nИгра окончена.")
        break
