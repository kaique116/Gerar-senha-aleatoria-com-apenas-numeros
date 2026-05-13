import tkinter as tk
from tkinter import messagebox
import random

# Cria a função para gerar uma senha aleatória de números, do tamanho especificado pelo usuário
def gerar_senha_aleatória():
    try:
        tamanho = int(tamanho_senha.get())
        senha = ''.join(random.choices('0123456789', k=tamanho))
        messagebox.showinfo("Senha gerada", f"Sua senha aleatória é: {senha}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o tamanho de sua senha")

# Cria a janela principal
janela = tk.Tk()
janela.title("Gerador de senha aleatória")
janela.geometry("300x150")

# Cria um rótulo e um campo de entrada para o tamanho da senha
rotulo_tamanho = tk.Label(janela, text="Tamanho da senha:")
rotulo_tamanho.pack()
tamanho_senha = tk.Entry(janela)
tamanho_senha.pack()

# Cria um botão para gerar a senha
botao_gerar = tk.Button(janela, text="Gerar senha", command=gerar_senha_aleatória)
botao_gerar.pack()

# Cria o loop principal da janela
janela.mainloop()
