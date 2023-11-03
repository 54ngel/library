import tkinter as tk

class Library:
    def __init__(self, books=[]):
        self.books = books

    def newBook(self, title, author, publicationDate):
        self.books.append(Book(title, author, publicationDate))

    def removeBook(self, id):
        self.books.pop(id)

class Book:
    def __init__(self, title, author, publicationDate):
        self.title = title
        self.author = author
        self.publicationDate = publicationDate

yourLibrary = tk.Tk()
yourLibrary.title("Twoja Biblioteka")
yourLibrary.geometry("520x500")
title = tk.Label(yourLibrary, text="Twoja Biblioteka", font=("Comic Sans MS", 40), fg="#0000FF")
title.grid(row=0, column=1, columnspan=2)

# Funkcja do resetowania
def reset():
    enterAuthorName.delete(0, tk.END)
    enterTitle.delete(0, tk.END)
    enterReleaseDate.delete(0, tk.END)

# Funkcja do dodawania książki
def dodaj_ksiazke():
    title = enterTitle.get()
    author = enterAuthorName.get()
    publicationDate = enterReleaseDate.get()
    Library.newBook(title, author, publicationDate)
    print(f"Dodano książkę: {title} autor: {author} data wydania: {publicationDate}")

# Funkcja do usuwania książki
def usun_ksiazke():
    book_name = enterTitle.get()  # Pobieramy nazwę książki
    for book in Library.books:
        if book.title == book_name:
            Library.books.remove(book)
            print("Usunięto książkę o nazwie:", book_name)
            return
    print("Książka o nazwie", book_name, "nie została znaleziona.")

def biblioteka():
    for widget in yourLibrary.winfo_children():
        widget.destroy()
    returnButton = tk.Button(yourLibrary, text="Powrót", width=10, height=2, fg="black", command=powrot)
    returnButton.grid(row=2, column=1)

# Funkcja do przywracania początkowego stanu po powrocie z "Biblioteka"
def powrot():
    for widget in yourLibrary.winfo_children():
        widget.destroy()

    authorLabel = tk.Label(yourLibrary, text="Podaj autora ksiązki:", font=("Consolas", 12), fg="#111111")
    authorLabel.grid(row=5, column=1)

    enterAuthorName = tk.Entry(yourLibrary, width=30, font=50)
    enterAuthorName.grid(row=6, column=1)

    titleLabel = tk.Label(yourLibrary, text="Podaj nazwę książki:", font=("Consolas", 12), fg="#111111")
    titleLabel.grid(row=7, column=1)

    enterTitle = tk.Entry(yourLibrary, width=30, font=50)
    enterTitle.grid(row=8, column=1)

    releaseDateLabel = tk.Label(yourLibrary, text="Podaj datę wydania książki:", font=("Consolas", 12), fg="#111111")
    releaseDateLabel.grid(row=9, column=1)

    enterReleaseDate = tk.Entry(yourLibrary, width=30, font=50)
    enterReleaseDate.grid(row=10, column=1)

    libraryButton = tk.Button(yourLibrary, text="Biblioteka", width=10, height=3, fg="orange", command=biblioteka)
    libraryButton.grid(row=10, column=0)

    addButton = tk.Button(yourLibrary, text="Dodaj", width=10, height=2, fg="green", command=dodaj_ksiazke)
    addButton.grid(row=11, column=0)

    removeButton = tk.Button(yourLibrary, text="Usuń", width=10, height=2, fg="red", command=usun_ksiazke)
    removeButton.grid(row=11, column=2)

    resetButton = tk.Button(yourLibrary, text="Reset", command=reset, width=10, height=3, fg="#0000FF")
    resetButton.grid(row=10, column=2)

# ...

authorLabel = tk.Label(yourLibrary, text="Podaj autora ksiązki:", font=("Consolas", 12), fg="#111111")
authorLabel.grid(row=5, column=1)

enterAuthorName = tk.Entry(yourLibrary, width=30, font=50)
enterAuthorName.grid(row=6, column=1)

titleLabel = tk.Label(yourLibrary, text="Podaj nazwę książki:", font=("Consolas", 12), fg="#111111")
titleLabel.grid(row=7, column=1)

enterTitle = tk.Entry(yourLibrary, width=30, font=50)
enterTitle.grid(row=8, column=1)

releaseDateLabel = tk.Label(yourLibrary, text="Podaj datę wydania książki:", font=("Consolas", 12), fg="#111111")
releaseDateLabel.grid(row=9, column=1)

enterReleaseDate = tk.Entry(yourLibrary, width=30, font=50)
enterReleaseDate.grid(row=10, column=1)

# Tworzenie przycisków "Dodaj" i "Usuń" z wywołaniem odpowiednich funkcji

libraryButton = tk.Button(yourLibrary, text="Biblioteka", width=10, height=3, fg="orange", command=biblioteka)
libraryButton.grid(row=10, column=0)

addButton = tk.Button(yourLibrary, text="Dodaj", width=10, height=2, fg="green", command=dodaj_ksiazke)
addButton.grid(row=11, column=0)

removeButton = tk.Button(yourLibrary, text="Usuń", width=10, height=2, fg="red", command=usun_ksiazke)
removeButton.grid(row=11, column=2)

resetButton = tk.Button(yourLibrary, text="Reset", command=reset, width=10, height=3, fg="#0000FF")
resetButton.grid(row=10, column=2)

yourLibrary.mainloop()