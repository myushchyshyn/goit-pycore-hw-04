def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Розбиває рядок на команду (нижній регістр) та список аргументів."""
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.strip().lower(), args


def add_contact(args: list[str], contacts: dict) -> str:
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    if name in contacts:
        return "Contact already exists. Use change to update the phone."
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict) -> str:
    if len(args) != 2:
        return "Usage: change [name] [phone]"
    name, phone = args
    if name not in contacts:
        return f"Contact {name!r} not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict) -> str:
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    return contacts.get(name, f"Contact {name!r} not found.")


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
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
