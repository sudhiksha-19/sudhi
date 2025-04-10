class Library:
    def __init__(self, book_list):
        self.books = book_list

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f"- {book}")

    def lend_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"\nYou have successfully borrowed '{book_name}'. Please return it on time.")
        else:
            print(f"\nSorry, the book '{book_name}' is not available or has already been issued.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"\nThank you for returning '{book_name}'. Hope you enjoyed reading it!")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"\nThe book '{book_name}' has been added to the library.")


# Main Program
def main():
    library_books = ["Python Programming", "Data Science Handbook", "Machine Learning Basics", "Artificial Intelligence"]
    library = Library(library_books)

    while True:
        print("\n--- Library Management System ---")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Return a Book")
        print("4. Add a Book")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_name = input("\nEnter the name of the book you want to borrow: ")
            library.lend_book(book_name)
        elif choice == "3":
            book_name = input("\nEnter the name of the book you want to return: ")
            library.return_book(book_name)
        elif choice == "4":
            book_name = input("\nEnter the name of the book you want to add: ")
            library.add_book(book_name)
        elif choice == "5":
            print("\nThank you for using the Library Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()