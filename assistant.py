def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    if not contacts:
        return "No contacts."
    return "\n".join(f"{k}: {v}" for k, v in contacts.items())

def show_help():
    return (
        "Available commands:\n"
        "hello                   - greet the bot\n"
        "add <name> <phone>      - add new contact\n"
        "change <name> <phone>   - change contact phone\n"
        "phone <name>            - show phone number\n"
        "all                     - show all contacts\n"
        "help                    - show this help\n"
        "exit / close            - exit the program"
    )
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Usage: add <name> <phone>")
            else:
                print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(show_help())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()