#importujemy tkinera i nazywamy i dodajemy 1 text
import tkinter as tk
BMI = tk.Tk()
BMI.title("Twoja Biblioteka")
BMI.geometry("500x500")
tytul=tk.Label(BMI, text="Twoja Biblioteka", font=("Comic Sans MS", 40), fg="#0000FF")
tytul.grid(row=0, column=1, columnspan=2)

<<<<<<< Updated upstream
#tworzenie pól textowych i przycisków
masowytext = tk.Label(BMI, text="Podaj autora ksiązki:", font=("Consolas", 12), fg="#111111")
masowytext.grid(row=5, column=1)

wpisaniemasy = tk.Entry(BMI, width=30, font=50)
wpisaniemasy.grid(row=6, column=1)
=======
class Library:
    def __init__(self, books=[]):
        self.books = books
>>>>>>> Stashed changes

wzrostowytext = tk.Label(BMI, text="Podaj nazwę książki:", font=("Consolas", 12), fg="#111111")
wzrostowytext.grid(row=7, column=1)

wpisaniewzrostu = tk.Entry(BMI, width=30, font=50)
wpisaniewzrostu.grid(row=8, column=1)

<<<<<<< Updated upstream
wynikowytext = tk.Label(BMI, text="Podaj datę wydania książki:", font=("Consolas", 12), fg="#111111")
wynikowytext.grid(row=9, column=1)

wpisaniewyniku = tk.Entry(BMI, width=30, font=50)
wpisaniewyniku.grid(row=10, column=1)

Resetuj = tk.Button(BMI, text="Dodaj""\n""Książke", width=5, height=3, fg="green")
Resetuj.grid(row=10, column=0)

Resetuj = tk.Button(BMI, text="Usuń""\n""Książke", width=5, height=3, fg="green")
Resetuj.grid(row=10, column=2)

BMI.mainloop()
=======
class Book:
    def __init__(self, title, author, publicationDate):
        self.title = title
        self.author = author
        self.publicationDate = publicationDate

# test#
library = Library()
library.newBook("Dziady III", "Adam Mickiewicz", 1814)
library.newBook("To", "Stephen King", 1983)
print(library.books)
########

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
    library.newBook(title, author, publicationDate)
    print(f"Dodano książkę: {title} autor: {author} data wydania: {publicationDate}")

# Funkcja do usuwania książki
def usun_ksiazke():
    book_name = enterTitle.get()  # Pobieramy nazwę książki
    for book in library.books:
        if book.title == book_name:
            library.books.remove(book)
            print("Usunięto książkę o nazwie:", book_name)
            return
    print("Książka o nazwie", book_name, "nie została znaleziona.")

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
libraryButton = tk.Button(yourLibrary, text="Biblioteka", width=10, height=3, fg="orange")
libraryButton.grid(row=10, column=0)

addButton = tk.Button(yourLibrary, text="Dodaj", width=10, height=2, fg="green", command=dodaj_ksiazke)
addButton.grid(row=11, column=0)

removeButton = tk.Button(yourLibrary, text="Usuń", width=10, height=2, fg="red", command=usun_ksiazke)
removeButton.grid(row=11, column=2)

resetButton = tk.Button(yourLibrary, text="Reset", command=reset, width=10, height=3, fg="#0000FF")
resetButton.grid(row=10, column=2)

yourLibrary.mainloop()
>>>>>>> Stashed changes
