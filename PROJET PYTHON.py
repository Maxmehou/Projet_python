import tkinter as tk
from tkinter import *

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def ppcm(a, b):
    return abs(a * b) // pgcd(a, b)

def NP(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nombres_premiers(limite):
    return [n for n in range(1, limite + 1) if NP(n)]

def calculer():
    try:
        a = int(N1.get())
        b = int(N2.get())
        
        R1 = pgcd(a, b)
        R2 = ppcm(a, b)
        P1 = "Ce nombre est pair" if a % 2 == 0 else "Ce nombre est impair"
        P2 = "Ce nombre est pair" if b % 2 == 0 else "Ce nombre est impair"
        somme = a + b
        Liste = nombres_premiers(somme)
        
        resultats = (
            f"Le PGCD de ces deux nombres est : {R1}\n"
            f"Le PPCM de ces deux nombres est : {R2}\n"
            f"Nombre 1 ({a}) : {P1}\n"
            f"Nombre 2 ({b}) : {P2}\n"
            f"Liste des nombres premiers entre 1 et {somme} : {Liste}"
        )
        resultat.config(text=resultats)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer deux nombres entiers valides.")


root = tk.Tk()
root.title("Logiciel python (ppcm; pgcd; NP)")
root.geometry("400x400")
root.configure(bg="beige")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (400 // 2)
y = (screen_height // 2) - (400 // 2)
root.geometry(f"400x400+{x}+{y}")

N1 = tk.StringVar()
N2 = tk.StringVar()

tk.Label(root, text="Entrez le premier nombre :", bg="beige").pack(pady=5)
P1 = tk.Entry(root, textvariable=N1)
P1.pack()

tk.Label(root, text="Entrez le deuxième nombre :", bg="beige").pack(pady=5)
P2 = tk.Entry(root, textvariable=N2)
P2.pack()

C = tk.Button(root, text="Soumettre", command=calculer)
C.pack(pady=10)

resultat = tk.Label(root, text="", justify="left", anchor="w", bg="beige", wraplength=380)
resultat.pack(pady=10)

root.mainloop()
