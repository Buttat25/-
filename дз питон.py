print("Загадайте число от -1 000 000 000 до 1 000 000 000.")
print("Отвечайте на вопросы символами:")
print("'>' — если ваше число больше")
print("'<' — если ваше число меньше")
print("'=' — если число угадано")
print("-" * 40)

low = -10**9
high = 10**9
attempts = 0

while low <= high:
    guess = (low + high) // 2
    attempts += 1

    user_input = input(f"Попытка №{attempts}. Ваше число это {guess}? (введите >, < или =): ")

    if user_input == '=':
        print(f"Ура! Число {guess} угадано за {attempts} шагов!")
        break
    elif user_input == '>':
        low = guess + 1
    elif user_input == '<':
        high = guess - 1
    else:
        print("Неверный ввод. Пожалуйста, используйте только '>', '<' или '='.")
        attempts -= 1
