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


BMI = tk.Tk()
BMI.title("Kalkulator BMI")
szerokosc=BMI.winfo_screenwidth()#pobiera szerokosc ekranu
wysokosc=BMI.winfo_height()#pobiera wielkosc ekranu
BMI.geometry(f"{szerokosc}x{wysokosc}")
BMI.attributes("-fullscreen", True)
tytul=tk.Label(BMI, text="Kalkulator BMI", font=("Comic Sans MS", 40), fg="#0000FF")
tytul.grid(row=0, column=16)
SOZ=tk.Label(BMI, text="Interpretacja wyniku BMI jest"  "\n" "oparta na ogólnie przyjętych kategoriach"     "\n" "(według Światowej Organizacji Zdrowia).", font=("Consolas", 10), fg="#111111")
SOZ.grid(row=1, column=10)

#tworzenie pól textowych i przycisków
masowytext = tk.Label(BMI, text="Podaj masę swego ciała (w kilogramach):", font=("Consolas", 12), fg="#111111")
masowytext.grid(row=3, column=16)

wpisaniemasy = tk.Entry(BMI, width=30, font=50)
wpisaniemasy.grid(row=4, column=16)

wzrostowytext = tk.Label(BMI, text="Podaj swój wzrost (w centymetrach):", font=("Consolas", 12), fg="#111111")
wzrostowytext.grid(row=5, column=16)

wpisaniewzrostu = tk.Entry(BMI, width=30, font=50)
wpisaniewzrostu.grid(row=6, column=16)

wynikowytext = tk.Label(BMI, text="Twoje BMI to:", font=("Consolas", 12), fg="#111111")
wynikowytext.grid(row=7, column=16)

wpisaniewyniku = tk.Entry(BMI, width=30, font=50)
wpisaniewyniku.grid(row=8, column=16)

Resetuj = tk.Button(BMI, text="Reset", width=5, height=3, command=reset, fg="green")
Resetuj.grid(row=1, column=2)

Obliczanie = tk.Button(BMI, text="Oblicz", width=5, height=3, command=result, fg="green")
Obliczanie.grid(row=1, column=1)

BMI.mainloop()