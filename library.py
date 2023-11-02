import tkinter as tk

class Library:
    def __init__(self, books = []):
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

def reset():
    enterAuthorName.delete(0, tk.END)
    enterTitle.delete(0, tk.END)
    enterReleaseDate.delete(0, tk.END)

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

addBookButton = tk.Button(yourLibrary, text="Dodaj""\n""Książke", width=5, height=3, fg="#0000FF")
addBookButton.grid(row=10, column=0)

removeBookButton = tk.Button(yourLibrary, text="Usuń""\n""Książke", width=5, height=3, fg="#0000FF")
removeBookButton.grid(row=10, column=2)

resetButton = tk.Button(yourLibrary, text="Reset", command=reset, width=5, height=3, fg="#0000FF")
resetButton.grid(row=10, column=3)

yourLibrary.mainloop()