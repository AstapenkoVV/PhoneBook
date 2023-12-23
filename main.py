import csv
import easygui


# Функция для поиска записи в телефонном справочнике
def search_contact():
     try:
        name = easygui.enterbox("Введите имя контакта для поиска:").lower()
        with open("contacts.csv", "r", encoding="windows-1251") as book:
            reader = csv.reader(book)
            rows = list(reader)
            found = False
            for row in rows:
                # Сравнение имени без учета регистра
                if row[0].lower() == name:
                    easygui.msgbox(f"Найдена запись: Имя: {row[0]}, Телефон: {row[1]}")
                    found = True
                    break
            if not found:
                easygui.msgbox(f"Запись с именем {name} не найдена.")
    #Если телефонный справочник пуст, выдаст соответствующее сообщение
    except: easygui.msgbox("Телефонная книга пустая!")


# Функция для добавления новой записи в телефоный справочник
def create_contact():
    name = easygui.enterbox("Введите имя контакта: ").lower()
    phone = easygui.enterbox("Введите номер телефона: ")
    with open("contacts.csv", "a", newline='') as book:
        create = csv.writer(book)
        create.writerow([name, phone])
        easygui.msgbox(f"Новая запись {name}: {phone} добавленна в телефонную книгу")


# Функция удаления записи из телефонного справочника
def delete_contact():

    name = easygui.enterbox("Введите имя контакта: ").lower()
    with open('contacts.csv', 'r', encoding="windows-1251") as book:
        reader = csv.reader(book)
        rows = list(reader)
        found = False
        for row in rows:
            if row[0] == name:
                rows.remove(row)
                found = True
                break
        if found:
            with open('contacts.csv', 'w', newline='') as book:
                writer = csv.writer(book)
                writer.writerows(rows)
                easygui.msgbox(f"Запись {name} удалена из телефонного справочника.")
        else:
            easygui.msgbox(f"Запись {name} не найдена в телефонном справочнике.")


# Функция для редактирования записи в телефонном справочнике
def edit_contact():
    name = easygui.enterbox("Введите имя контакта: ").lower()
    with open('contacts.csv', 'r', encoding="windows-1251") as book:
        reader = csv.reader(book)
        rows = list(reader)
    found = False
    for row in rows:
        if row[0] == name:
            phone = easygui.enterbox(f"Введите новый номер телефона для {name}:")
            row[1] = phone
            found = True
            break
    if found:
        with open('contacts.csv', 'w', newline='') as book:
            writer = csv.writer(book)
            writer.writerows(rows)
        easygui.msgbox(f"Запись {name}: {phone} изменена в телефонном справочнике.")
    else:
        easygui.msgbox(f"Запись {name} не найдена в телефонном справочнике.")


# Тело программы
while True:
# Графический интерфейс программы со списком действий
    choice = easygui.buttonbox("Выберите действие с телефонной книгой:",
                               choices=["Найти контакт",
                                        "Добавить новый контакт",
                                        "Удалить имеющуюся контакт",
                                        "Редактировать контакт",
                                        "Выход"])
# Выполнение действий в зависимости от выбранной комманды
    if choice == "Добавить новый контакт":
        create_contact()
    elif choice == "Удалить имеющуюся контакт":
        delete_contact()
    elif choice == "Редактировать контакт":
        edit_contact()
    elif choice == "Найти контакт":
        search_contact()
    elif choice == "Выход":
        break