#importujemy tkinera i nazywamy i dodajemy 1 text
import tkinter as tk
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

#funkcja result po kliknięciu guzika obliczanie wylicza bmi ściągając dane z 2 pól(wzrost, masa) i zależnie od bmi daje odpowiedź
def result():
    wpisaniewyniku.delete(0, tk.END)
    usuniecie = tk.Label(BMI, text="                                                          ""\n""              ""\n""                ",font=("Comic Sans MS", 20))
    usuniecie.grid(row=1, column=0)
    masa = wpisaniemasy.get()
    wzrost = wpisaniewzrostu.get()
    if masa.isdigit() and wzrost.isdigit():
        wzrost=float(wzrost)/100
        masa = float(masa)
        w = round((masa/wzrost**2), 2)
        wpisaniewyniku.insert(0, w)

#funkcja reset usuwa wszystko co użytkownik wpisał oraz usuwa odpowiedzi
def reset():
    wpisaniewzrostu.delete(0, tk.END)
    wpisaniemasy.delete(0, tk.END)
    wpisaniewyniku.delete(0, tk.END)
    usuniecie = tk.Label(BMI,text="                                                          ""\n""              ""\n""                ", font=("Comic Sans MS", 20))
    usuniecie.grid(row=9, column=1)

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