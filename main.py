from sprv import *

def main():
    contacts = load_contacts()

    while True:
        print("Выберите действие:")
        print("1. Показать все контакты")
        print("2. Добавить новый контакт")
        print("3. Изменить существующий контакт")
        print("4. Удалить контакт")
        print("5. Сохранить контакты")
        print("6. Выйти")

        choice = input("Ваш выбор: ")
        print()

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            contact = add_contact()
            contacts.append(contact)
            print("Контакт успешно добавлен.")
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
