import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 04")
janela.geometry("400x300")

def dizer_ola():
    print("Olá!")

botao_ola = tk.Button(janela, text="Dizer Olá", command=dizer_ola)
botao_ola.pack(pady=20)
janela.mainloop()
