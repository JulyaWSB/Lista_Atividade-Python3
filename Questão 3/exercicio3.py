import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 03")
janela.geometry("400x300")

label = tk.Label(janela, text="Bem-vindo ao Tkinter")
label.pack(pady=20)
janela.mainloop()
