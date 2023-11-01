import tkinter as tk
bib = tk.Tk()
bib.title("Twoja Biblioteka")
bib.geometry("520x500")
tytul=tk.Label(bib, text="Twoja Biblioteka", font=("Comic Sans MS", 40), fg="#0000FF")
tytul.grid(row=0, column=1, columnspan=2)

def reset():
    wpisanieautora.delete(0, tk.END)
    wpisanietytulu.delete(0, tk.END)
    wpisanierocznika.delete(0, tk.END)

textautora = tk.Label(bib, text="Podaj autora ksiązki:", font=("Consolas", 12), fg="#111111")
textautora.grid(row=5, column=1)

wpisanieautora = tk.Entry(bib, width=30, font=50)
wpisanieautora.grid(row=6, column=1)

tytulowytext = tk.Label(bib, text="Podaj nazwę książki:", font=("Consolas", 12), fg="#111111")
tytulowytext.grid(row=7, column=1)

wpisanietytulu = tk.Entry(bib, width=30, font=50)
wpisanietytulu.grid(row=8, column=1)

rocznikowytext = tk.Label(bib, text="Podaj datę wydania książki:", font=("Consolas", 12), fg="#111111")
rocznikowytext.grid(row=9, column=1)

wpisanierocznika = tk.Entry(bib, width=30, font=50)
wpisanierocznika.grid(row=10, column=1)

dodawanie = tk.Button(bib, text="Dodaj""\n""Książke", width=5, height=3, fg="#0000FF")
dodawanie.grid(row=10, column=0)

usuwanie = tk.Button(bib, text="Usuń""\n""Książke", width=5, height=3, fg="#0000FF")
usuwanie.grid(row=10, column=2)

resetowanie = tk.Button(bib, text="Reset", command=reset, width=5, height=3, fg="#0000FF")
resetowanie.grid(row=10, column=3)

bib.mainloop()