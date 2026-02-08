#3

airports = {}


while True:
    user_choice = input("Enter 'new' to add, 'fetch' to get info, or 'quit' to exit: ")

    if user_choice == "quit":
        break
    elif user_choice == "new":
        code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[code] = name
        print(f"New airport added", name)

    elif user_choice == "fetch":
        code = input("Enter ICAO code to fetch: ")
        if code in airports:
            print(f"Airport name:", airports[code])
        else:
            print("No Airport found.")
    else:
        print("Invalid choice. Please type fetch, new or quit")


