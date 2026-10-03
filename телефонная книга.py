phone_book = {}
while True:
    print()
    print("Меню телефона:")
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Показать все контакты")
    print("4. Выйти")
    
    choice = input("Нажмите кнопку (1-4): ")
    
    if choice == "1":
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        phone_book[name] = phone
        print("Контакт успешно добавлен")
        
    elif choice == "2":
        name = input("Введите имя для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print("Контакт успешно удален")
        else:
            print("Такого имени нет в списке")
            
    elif choice == "3":
        if len(phone_book) == 0:
            print("Контактов пока нет")
        else:
            print("Список ваших контактов:")
            for name, phone in phone_book.items():
                print(name, "-", phone)
                
    elif choice == "4":
        print("Выход из программы")
        break
        
    else:
        print("Ошибка, нажмите кнопку от 1 до 4")
