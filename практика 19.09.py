def cypher(char, n):
    alphavite = ("abcdefghijklmnopqrstuvwxyz",
"ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if char in alphavite[0]:
        current_index = alphavite[0].find(char)
        new_index = (current_index + n) % 26
        return alphavite[0][new_index]

    elif char in alphavite[1]:
        current_index = alphavite[1].find(char)
        new_index = (current_index + n) % 26
        return alphavite[1][new_index]

    else:
        return char

n = int(input("Введите сдвиг: "))
str = input("Введите слово для шифрования: ")
shstr = ""

for char in str:
    shstr += cypher(char, n)

print(shstr)
