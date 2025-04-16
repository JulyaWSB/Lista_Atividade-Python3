import tkinter as tk
from tkinter import messagebox
import sqlite3

janela = tk.Tk()
janela.title("Exercícios 05-09")
janela.geometry("400x300")

label_nome = tk.Label(janela, text="Nome:")
label_nome.pack(pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

label_idade = tk.Label(janela, text="Idade:")
label_idade.pack(pady=5)
entrada_idade = tk.Entry(janela)
entrada_idade.pack(pady=5)

def exibir_dados():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    print(f"Nome: {nome}, Idade: {idade}")  
    messagebox.showinfo("Informações", f"Nome: {nome}\nIdade: {idade}")

def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)

def mudar_label_nome():
    if label_nome.cget("text") == "Nome":
        label_nome.config(text="Nome Completo")
    else:
        label_nome.config(text="Nome")

def salvar_no_banco():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    
    conexao = sqlite3.connect("dados.db")
    cursor = conexao.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome TEXT, idade INTEGER)")
    
    cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))
    
    conexao.commit()
    conexao.close()
    messagebox.showinfo("Sucesso", "Dados salvos no banco de dados!")

def consultar_banco():
    conexao = sqlite3.connect("dados.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas")  
    dados = cursor.fetchall()  

    for pessoa in dados:
        print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}")

    if dados:
        messagebox.showinfo("Dados no Banco", "\n".join([f"Nome: {pessoa[0]}, Idade: {pessoa[1]}" for pessoa in dados]))
    else:
        messagebox.showinfo("Sem Dados", "Nenhum dado encontrado no banco.")

    conexao.close()

botao_exibir = tk.Button(janela, text="Exibir Nome e Idade", command=exibir_dados)
botao_exibir.pack(pady=5)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar_campos)
botao_limpar.pack(pady=5)

botao_mudar_label = tk.Button(janela, text="Mudar para 'Nome Completo'", command=mudar_label_nome)
botao_mudar_label.pack(pady=5)

botao_salvar = tk.Button(janela, text="Salvar no Banco", command=salvar_no_banco)
botao_salvar.pack(pady=5)

botao_consultar = tk.Button(janela, text="Consultar Dados no Banco", command=consultar_banco)
botao_consultar.pack(pady=5)

janela.mainloop()

