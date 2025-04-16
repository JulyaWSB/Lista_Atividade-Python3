import tkinter as tk

def converter_temperatura():
    try:
        celsius = float(entrada_celsius.get())  
        fahrenheit = celsius * 9 / 5 + 32  
        resultado.config(text=f"{fahrenheit:.2f} °F")  
    except ValueError:
        resultado.config(text="Por favor, insira um número válido.")

janela = tk.Tk()
janela.title("Conversão de Temperatura")
janela.geometry("400x300")
janela.config(bg="#ffffff")  

titulo_font = ("Helvetica", 18, "bold")
instrucoes_font = ("Arial", 12)
resultado_font = ("Arial", 14, "italic", "bold")

cor_roxo_claro = "#9370DB"  
cor_preto = "#000000"       
cor_branco = "#FFFFFF"      

titulo = tk.Label(janela, text="Conversão de Temperatura", font=titulo_font, bg=cor_branco, fg=cor_preto)
titulo.pack(pady=20)

instrucoes = tk.Label(janela, text="Digite a temperatura em Celsius:", font=instrucoes_font, bg=cor_branco, fg=cor_preto)
instrucoes.pack(pady=10)

entrada_celsius = tk.Entry(janela, font=("Arial", 12), width=20, borderwidth=2, relief="solid")
entrada_celsius.pack(pady=10)

botao_converter = tk.Button(janela, text="Converter para Fahrenheit", command=converter_temperatura,
                            font=("Arial", 12), bg=cor_roxo_claro, fg=cor_preto, padx=10, pady=5, relief="raised")
botao_converter.pack(pady=10)

resultado = tk.Label(janela, text="Resultado aparecerá aqui.", font=resultado_font, bg=cor_branco, fg=cor_roxo_claro)
resultado.pack(pady=20)

janela.mainloop()
