#importujemy tkinera i nazywamy i dodajemy 1 text
import tkinter as tk
BMI = tk.Tk()
BMI.title("Twoja Biblioteka")
BMI.geometry("500x500")
tytul=tk.Label(BMI, text="Twoja Biblioteka", font=("Comic Sans MS", 40), fg="#0000FF")
tytul.grid(row=0, column=1, columnspan=2)

#tworzenie pól textowych i przycisków
masowytext = tk.Label(BMI, text="Podaj autora ksiązki:", font=("Consolas", 12), fg="#111111")
masowytext.grid(row=5, column=1)

wpisaniemasy = tk.Entry(BMI, width=30, font=50)
wpisaniemasy.grid(row=6, column=1)

wzrostowytext = tk.Label(BMI, text="Podaj nazwę książki:", font=("Consolas", 12), fg="#111111")
wzrostowytext.grid(row=7, column=1)

wpisaniewzrostu = tk.Entry(BMI, width=30, font=50)
wpisaniewzrostu.grid(row=8, column=1)

wynikowytext = tk.Label(BMI, text="Podaj datę wydania książki:", font=("Consolas", 12), fg="#111111")
wynikowytext.grid(row=9, column=1)

wpisaniewyniku = tk.Entry(BMI, width=30, font=50)
wpisaniewyniku.grid(row=10, column=1)

Resetuj = tk.Button(BMI, text="Dodaj""\n""Książke", width=5, height=3, fg="green")
Resetuj.grid(row=10, column=0)

Resetuj = tk.Button(BMI, text="Usuń""\n""Książke", width=5, height=3, fg="green")
Resetuj.grid(row=10, column=2)

BMI.mainloop()