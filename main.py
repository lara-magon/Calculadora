import tkinter as tk
from tkinter import messagebox
from math import cos, sin, radians

def calcular():

    try:
        peso_b = float(entry_peso_b.get())
        mu = float(entry_mu.get())
        angulo = float(entry_angulo.get())
        theta = radians(angulo)

        fat_max = mu * peso_b

        t1 = fat_max

        t2 = t1 / cos(theta)

        pa = t2 * sin(theta)

        resultado.config(
            text=(
                f"Atrito máximo = {fat_max:.2f} N\n\n"
                f"T1 máximo = {t1:.2f} N\n\n"
                f"T2 = {t2:.2f} N\n\n"
                f"Peso máximo de A = {pa:.2f} N"
            )
        )

    except:
        messagebox.showerror(
            "Erro",
            "Digite valores válidos!"
        )

def limpar():
    entry_peso_b.delete(0, tk.END)
    entry_mu.delete(0, tk.END)
    entry_angulo.delete(0, tk.END)

    resultado.config(text="Resultados aparecerão aqui")

janela = tk.Tk()
janela.title("Calculadora - Sistema sem Roldana")
janela.geometry("600x500")
janela.config(bg="#f0f0f0")

titulo = tk.Label(
    janela,
    text="CALCULADORA - SISTEMA SEM ROLDANA",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#003366"
)

titulo.pack(pady=15)

frame = tk.Frame(janela, bg="white", bd=2, relief="groove")
frame.pack(padx=20, pady=10, fill="both")


label_peso_b = tk.Label(
    frame,
    text="Peso do bloco B (N):",
    font=("Arial", 12),
    bg="white"
)
label_peso_b.pack(pady=5)

entry_peso_b = tk.Entry(frame, font=("Arial", 12))
entry_peso_b.pack(pady=5)

label_mu = tk.Label(
    frame,
    text="Coeficiente de atrito estático:",
    font=("Arial", 12),
    bg="white"
)
label_mu.pack(pady=5)

entry_mu = tk.Entry(frame, font=("Arial", 12))
entry_mu.pack(pady=5)


label_angulo = tk.Label(
    frame,
    text="Ângulo (graus):",
    font=("Arial", 12),
    bg="white"
)
label_angulo.pack(pady=5)

entry_angulo = tk.Entry(frame, font=("Arial", 12))
entry_angulo.pack(pady=5)

botao_calcular = tk.Button(
    frame,
    text="CALCULAR",
    font=("Arial", 12, "bold"),
    bg="#0077cc",
    fg="white",
    width=20,
    command=calcular
)
botao_calcular.pack(pady=10)

botao_limpar = tk.Button(
    frame,
    text="LIMPAR",
    font=("Arial", 12),
    width=20,
    command=limpar
)
botao_limpar.pack(pady=5)

resultado = tk.Label(
    janela,
    text="Resultados aparecerão aqui",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="black",
    justify="left"
)

resultado.pack(pady=20)

janela.mainloop()
