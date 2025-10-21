from tkinter import Tk

from tkinter import Tk, Button, Label

def dizer_ola():
    rotulo_ola_mundo.config(text="Olá, Mundo!")

janela = Tk()
janela.title("Dizer Olá")
janela.maxsize(width=600, height=600)


botao_dizer_ola = Button(janela, text="Dizer Olá", command=dizer_ola)
botao_dizer_ola.pack(pady=20)

rotulo_ola_mundo = Label(janela, text="")
rotulo_ola_mundo.pack()

janela.mainloop()
