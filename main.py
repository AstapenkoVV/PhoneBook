import csv
import easygui


# Функция для поиска записи в телефонном справочнике
def search_contact():
    try:
        name = easygui.enterbox("Введите имя для поиска:").lower()
        with open("contacts.csv", "r", encoding="utf-8") as book:
            reader = csv.reader(book)
            rows = list(reader)
            found = False
            for row in rows:
                # Сравнение имени без учета регистра
                if row[0].lower() == name:
                    easygui.msgbox(f"Найдена запись: Имя - {row[0]}, Телефон - {row[1]}")
                    found = True
                    break
            if not found:
                easygui.msgbox(f"Запись с именем {name} не найдена.")
    #Если телефонный справочник пуст, выдаст соответствующее сообщение
    except: easygui.msgbox("Телефонная книга пустая!")


# Функция для добавления новой записи в телефоный справочник
def create_contact():
    name = easygui.enterbox("Введите имя: ").lower()
    phone = easygui.enterbox("Введите номер телефона: ")
    with open("contacts.csv", "a", encoding="utf-8") as book:
        create = csv.writer(book)
        create.writerow([name, phone])
    easygui.msgbox("Новая запись добавленна в телефонную книгу")







# Тело программы

while True:
    choice = easygui.buttonbox("Выберите действие с телефонной книгой:",
                               choices=["Найти контакт",
                                        "Добавить новый контакт",
                                        "Удалить имеющуюся контакт",
                                        "Редактировать контакт",
                                        "Выход"])

    # Выполняем действия
    if choice == "Найти контакт":
        search_contact()
    elif choice == "Добавить новый контакт":
        create_contact()
    elif choice == "Удалить имеющуюся контакт":
        delete_contact()
    elif choice == "Редактировать контакт":
        edit_contact()
    elif choice == "Выход":
        break