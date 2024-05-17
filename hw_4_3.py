def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added." 
    #my code
def change_contact(args, contacts):
    
    name = args [0]
    if name in contacts:
        contacts[name] = phone
        name.format(phone)
        return "Contact updated."
    else:
        return "Contact does not find"

def show_contact (args, contacts):
    name = args [0]
    if name in contacts:
        return contacts[name]
    else:
        return "contact does not exist"

def show_all (args, contacts):
    
    all_name = []
    for name in contacts:
        all_name.append(contacts)
        return all_name
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        # my code 
        elif command == "phone":
            print (show_contact(args,contacts))
        
        elif command == "all":
            print (show_all(args,contacts))
        
        elif command == "change":
            print (change_contact(args, contacts))
       #my code
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
