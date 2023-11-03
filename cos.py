import tkinter as tk
from tkinter import ttk

# Stworzenie klasy Library, która jest bazą danych naszego programu
class Library:
    def __init__(self, books=[]):
        self.books = books

    def newBook(self, title, author, publicationDate):
        self.books.append(Book(title, author, publicationDate))

    def removeBook(self, id):
        self.books.pop(id)

myLibrary = Library()

# Stworzenie klasy Book, która służy do dodawania książek do naszej bazy danych
class Book:
    def __init__(self, title, author, publicationDate):
        self.title = title
        self.author = author
        self.publicationDate = publicationDate


# Zdefiniowanie podstawowych ustawień GUI
yourLibrary = tk.Tk()
yourLibrary.title("Twoja Biblioteka")
yourLibrary.geometry("650x500")
title = tk.Label(yourLibrary, text="Twoja Biblioteka", font=("Comic Sans MS", 40), fg="#0000FF")
title.grid(row=0, column=0, columnspan=3)

# Puste widgety, służące do obrotu danych
enterAuthorName = None
enterTitle = None
enterReleaseDate = None

# Funkcja tworząca pierwszą strone GUI
def create_first_page():
    global enterTitle, enterAuthorName, enterReleaseDate
    for widget in yourLibrary.winfo_children():
        widget.destroy()

    title = tk.Label(yourLibrary, text="Twoja Biblioteka", font=("Comic Sans MS", 40), fg="#0000FF")
    title.grid(row=0, column=0, columnspan=3)

    titleLabel = tk.Label(yourLibrary, text="Podaj nazwę książki:", font=("Consolas", 12), fg="#111111")
    titleLabel.grid(row=1, column=1)

    enterTitle = tk.Entry(yourLibrary, width=30, font=50)
    enterTitle.grid(row=2, column=1)

    authorLabel = tk.Label(yourLibrary, text="Podaj autora książki:", font=("Consolas", 12), fg="#111111")
    authorLabel.grid(row=3, column=1)

    enterAuthorName = tk.Entry(yourLibrary, width=30, font=50)
    enterAuthorName.grid(row=4, column=1)

    releaseDateLabel = tk.Label(yourLibrary, text="Podaj datę wydania książki:", font=("Consolas", 12), fg="#111111")
    releaseDateLabel.grid(row=5, column=1)

    enterReleaseDate = tk.Entry(yourLibrary, width=30, font=50)
    enterReleaseDate.grid(row=6, column=1)

    addButton = tk.Button(yourLibrary, text="Dodaj", width=10, height=2, fg="green", command=dodaj_ksiazke)
    addButton.grid(row=7, column=0)

    removeButton = tk.Button(yourLibrary, text="Usuń", width=10, height=2, fg="red", command=usun_ksiazke)
    removeButton.grid(row=8, column=0)

    resetButton = tk.Button(yourLibrary, text="Reset", command=reset, width=10, height=2, fg="#0000FF")
    resetButton.grid(row=7, column=2)

    libraryButton = tk.Button(yourLibrary, text="Biblioteka", width=10, height=2, fg="orange", command=create_second_page)
    libraryButton.grid(row=8, column=2)

# Funckja tworząca drugą strone GUI
def create_second_page():
    for widget in yourLibrary.winfo_children():
        widget.destroy()

    returnButton = tk.Button(yourLibrary, text="Powrót", width=10, height=2, fg="black", command=create_first_page)
    returnButton.grid(row=1, column=0)

    # Zdefiniowanie kolumn
    columns = ('title', 'author', 'publication')
    tree = ttk.Treeview(yourLibrary, columns=columns, show='headings')

    # Zdefiniowanie nazw kolumn
    tree.heading('title', text='Tytuł')
    tree.heading('author', text='Autor')
    tree.heading('publication', text='Rok Wydania')

    # lista z danaymi
    contacts = [(book.title, book.author, book.publicationDate) for book in myLibrary.books]

    # Wyświetlanie danych
    for contact in contacts:
        tree.insert('', tk.END, values=contact)

    tree.grid(row=0, column=0, sticky='nsew')

    # scroll
    scrollbar = ttk.Scrollbar(yourLibrary, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

# Funkcja do resetowania labeli
def reset():
    if enterTitle:
        enterTitle.delete(0, tk.END)
    if enterAuthorName:
        enterAuthorName.delete(0, tk.END)
    if enterReleaseDate:
        enterReleaseDate.delete(0, tk.END)

# Funkcja do dodawania książki
def dodaj_ksiazke():
    title = enterTitle.get()
    author = enterAuthorName.get()
    publicationDate = enterReleaseDate.get()
    if title == '' or author == '' or publicationDate == '':
        print("Uzupełnij wszystkie pola")
    else:
        myLibrary.newBook(title, author, publicationDate)
        print(f"Dodano książkę: {title} autor: {author} data wydania: {publicationDate}")
        reset()

# Function do usuwania książki
def usun_ksiazke():
    book_name = enterTitle.get()
    if book_name == '':
        print("Wpisz nazwę książki, którą chcesz usunąć")
    else:
        for book in myLibrary.books:
            if book.title == book_name:
                myLibrary.books.remove(book)
                print("Usunięto książkę o nazwie:", book_name)
                reset()
                return
        print("Książka o nazwie", book_name, "nie została znaleziona")

# start GUI
create_first_page()
yourLibrary.mainloop()