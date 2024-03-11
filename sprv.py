from clop import *
4

def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = [surname, name, patronymic, phone_number]
    return contact

def display_contacts(contacts):
    for contact in contacts:
        print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Телефон: {contact[3]}")

def save_contacts(contacts):
    write_contacts_to_csv("contacts.csv", contacts)
    print("Контакты сохранены в файле contacts.csv")

def load_contacts():
    try:
        contacts = read_contacts_from_csv("contacts.csv")
        print("Контакты успешно загружены из файла contacts.csv")
        return contacts
    except FileNotFoundError:
        print("Файл contacts.csv не найден. Создайте новый список контактов.")
        return []

def find_contact_index(contacts, search_query):
    for i, contact in enumerate(contacts):
        if search_query in (contact[0], contact[1], contact[2]):
            return i
    return -1

def update_contact(contacts):
    search_query = input("Введите фамилию, имя или отчество контакта, которого хотите изменить: ")
    contact_index = find_contact_index(contacts, search_query)
    if contact_index != -1:
        print("Найден следующий контакт:")
        display_contacts([contacts[contact_index]])
        surname = input("Введите новую фамилию (оставьте пустым, если не хотите менять): ")
        name = input("Введите новое имя (оставьте пустым, если не хотите менять): ")
        patronymic = input("Введите новое отчество (оставьте пустым, если не хотите менять): ")
        phone_number = input("Введите новый номер телефона (оставьте пустым, если не хотите менять): ")
        if surname:
            contacts[contact_index][0] = surname
        if name:
            contacts[contact_index][1] = name
        if patronymic:
            contacts[contact_index][2] = patronymic
        if phone_number:
            contacts[contact_index][3] = phone_number
        print("Контакт успешно обновлен.")
    else:
        print("Контакт не найден.")

def delete_contact(contacts):
    search_query = input("Введите фамилию, имя или отчество контакта, которого хотите удалить: ")
    contact_index = find_contact_index(contacts, search_query)
    if contact_index != -1:
        print("Найден следующий контакт:")
        display_contacts([contacts[contact_index]])
        confirmation = input("Вы уверены, что хотите удалить этот контакт? (y/n): ")
        if confirmation.strip().lower() == "y":
            del contacts[contact_index]
            print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")


    