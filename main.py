from storage import save_books, load_books
from book_manager import add_book, delete_book, list_books, search_books

def main():
    books = load_books()
    while True:

        print("=== book manager ===\n")
        print("1. boek toevoegen")
        print("2. boeken tonen")
        print("3. boek verwijderen")
        print("4. boek zoeken")
        print("5. stoppen\n")
    
        keuze = input("maak je keuze: ")

        if keuze == "1":
            title = input("wat is de titel van het boek: ")
            author = input("wie is de auteur van het boek: ")
            add_book(books, title, author)
            save_books(books)
            print("boek toegevoegd")
        elif keuze == "2":
            list_books(books)
        elif keuze == "3":
            list_books(books)
            try:
                index = int(input("welk boek wil je verwijderen: ")) -1
                delete_book(books, index)
                save_books(books)
            except ValueError:
                print("ongeldige invoer")
        elif keuze == "4":
            search_word = input("geef de titel van het boek: ")
            search_books(books, search_word)
        elif keuze == "5":
            print("programma stoppen")
            break


if __name__ == "__main__":
    main()

        