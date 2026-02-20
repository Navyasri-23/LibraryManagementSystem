books = []

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    # Add Book
    if choice == "1":
        name = input("Enter book name: ")
        books.append([name, "Available"])
        print("Book added successfully!")

    # Show Books
    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            for b in books:
                print("Book:", b[0], "| Status:", b[1])

    # Search Book
    elif choice == "3":
        search = input("Enter book name: ")
        found = False

        for b in books:
            if b[0] == search:
                print("Book found:", b[0], "-", b[1])
                found = True
                break

        if not found:
            print("Book not found.")

    # Issue Book
    elif choice == "4":
        name = input("Enter book name to issue: ")

        for b in books:
            if b[0] == name:
                if b[1] == "Available":
                    b[1] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book already issued.")

    # Return Book
    elif choice == "5":
        name = input("Enter book name to return: ")

        for b in books:
            if b[0] == name:
                b[1] = "Available"
                print("Book returned successfully!")

    # Exit
    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")