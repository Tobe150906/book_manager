def add_book(books, title, author):
    book = {
        "title": title,
        "author": author
    }
    books.append(book)

def list_books(books):
    if len(books)== 0:
        print("geen boeken")
        return
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book['title']} | {book['author']}")

def delete_book(books, index):
    if 0 <= index < len(books):
        verwijderd = books.pop(index)
        print(f"verwijderd {verwijderd['title']}")
    else:
        print("ongeldige waarde")
def search_books(books, search_word):
    for book in books:
        if search_word.lower() in book["title"].lower():
            print(f"{book["title"]} | {book["author"]}")
        else:
            print("boek niet gevonden kijk na op schrijffouten.")
