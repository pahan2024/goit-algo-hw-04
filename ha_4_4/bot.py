def parse_input(user_input):
    if not user_input.strip():
        return "unknown", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Критерій: нечутливість до регістру
    return cmd, *args


# Критерій: Логіка в окремих функціях, приймають аргументи, повертають рядок
def add_contact(args, contacts):
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Error: Contact '{name}' not found."


def show_phone(args, contacts):
    if not args:
        return "Error: Enter user name."
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return f"Error: Contact '{name}' not found."


def show_all(contacts):
    if not contacts:
        return "Your contact list is empty."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


# Критерій: Вся взаємодія (print/input) тільки у функції main
def main():
    contacts = {}  # Критерій: Зберігання у пам'яті (словник)
    print("Welcome to the assistant bot!")

    while True:  # Критерій: Нескінченний цикл
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:  # Критерій: Завершення за командами
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
