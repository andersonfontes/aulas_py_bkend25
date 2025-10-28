import tkinter as tk
from tkinter import messagebox
import csv

# Lista para armazenar os empréstimos
emprestimos = []

# Função para salvar os dados no arquivo CSV
def salvar_dados():
    with open("emprestimos.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["livro", "usuario"])
        for e in emprestimos:
            writer.writerow([e["livro"], e["usuario"]])

# Função para carregar os dados do arquivo CSV
def carregar_dados():
    try:
        with open("emprestimos.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                emprestimos.append(row)
    except FileNotFoundError:
        pass  # Arquivo ainda não existe

# Função para cadastrar um novo empréstimo
def cadastrar_emprestimo():
    livro = nome_livro.get()
    usuario = nome_usuario.get()
    if livro and usuario:
        emprestimos.append({"livro": livro, "usuario": usuario})
        messagebox.showinfo("Sucesso", f"Empréstimo registrado: {livro} para {usuario}")
        nome_livro.delete(0, tk.END)
        nome_usuario.delete(0, tk.END)
        atualizar_emprestimos()
        salvar_dados()  # Salva os dados após cada novo cadastro
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

# Função para atualizar a exibição dos empréstimos
def atualizar_emprestimos():
    texto = "\n".join([f"{e['livro']} - {e['usuario']}" for e in emprestimos])
    emprestimos_label.config(text=texto)

# Cria a janela principal
janela = tk.Tk()
janela.title("Biblioteca - Cadastro de Empréstimos")
janela.geometry("400x300")  # Define o tamanho da janela

# Labels e campos de entrada para o nome do livro e do usuário
tk.Label(janela, text="Nome do Livro:").pack(pady=5)
nome_livro = tk.Entry(janela)
nome_livro.pack(pady=5)

tk.Label(janela, text="Nome do Usuário:").pack(pady=5)
nome_usuario = tk.Entry(janela)
nome_usuario.pack(pady=5)

# Botão para cadastrar o empréstimo
tk.Button(janela, text="Cadastrar Empréstimo", command=cadastrar_emprestimo).pack(pady=20)

# Label para exibir a lista de empréstimos registrados
emprestimos_label = tk.Label(janela, text="")
emprestimos_label.pack(pady=10)

# Carrega os dados ao iniciar o programa
carregar_dados()
atualizar_emprestimos()

# Inicia o loop principal
janela.mainloop()

