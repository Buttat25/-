text = input("Введите ваш текст:")
predloshenie_count = text.count(".") + text.count("...") + text.count("!") + + text.count("?")
trush = ".,~!@#$%^&*()_+-?/\\[]|\"\'"
for symbol in trush:
    text = text.replace(symbol, "")
words = text.lower().split()
words_count = len(words)
unikal_words = len(set(words))
dlinnoe_words = max(words, key=len)
most_popular_words = max(words, key=words.count)
obchaia_dlina = 0
for word in words:
    obchaia_dlina = obchaia_dlina + len(word)
sr_dlina = obchaia_dlina / words_count
print("Количество всех слов:", words_count)
print("Количество уникальных слов:", unikal_words)
print("Самое длинное слово:",  dlinnoe_words)
print("Самое частое слово:",  most_popular_words)
print("Количество предложений:", predloshenie_count)
print("Средняяя длина слова",sr_dlina )








