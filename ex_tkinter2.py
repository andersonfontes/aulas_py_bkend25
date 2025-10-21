import tkinter as tk

# Criar uma janela
janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry("300x200")

# Função para lidar com o clique do botão
def on_clique():
    label.config(text="Olá, " + entrada.get())

# Criar uma caixa de texto
entrada = tk.Entry(janela, width=20)
entrada.pack()

# Criar um botão
botao = tk.Button(janela, text="Clique aqui", command=on_clique)
botao.pack()

# Criar uma etiqueta para exibir o resultado
label = tk.Label(janela, text="")
label.pack()

# Iniciar o loop principal da aplicação
janela.mainloop()