from tabulate import tabulate

print("PROGRAMA DE CADASTRO \n")

# passo 1: pegar os dados do usuario
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
email = input("Digite seu email: ")
cpf = input("Digite seu cpf: ")

# passo 2: montar a string que vai ser inserida no arquivo
novoregistro = f"\n{nome},{sobrenome},{email},{cpf}"

# passo 3: abrir o arquivo e inserir a nova linha
arquivoappend = open("dados.csv" , "a")
arquivoappend.write(novoregistro)

# passo 4: fechar a conexao com o arquivo
arquivoappend.close()

# SEGUNDA FASE: IMPRIMIR OS DADOS

# passo 1: abrir o arquivo em modo leitura
arquivoleitura = open("dados.csv" , "r")
listalinhas = arquivoleitura.readlines()

# teste: imprimir cada linha usando for:
# for linha in listalinhas:
#     print(linha)

# passo 2: criar um for para cada linha (excluindo a primeira que o cabeçalho)
# passo 3: imprimir formatado
for linha in listalinhas[1:]: #2
    listadados = linha.split(sep = ",")
    stringexibir = f""" =======================
    Nome = {listadados[0]}
    Sobrenome = {listadados[1]}
    Email = {listadados[2]}
    CPF = {listadados[3]}"""
    print(stringexibir)

# alternativa: fazr uma tabela com tabulate
listaparaotabulate = []

for linha in listalinhas: #2
    listalinha = []

    listadados = linha.split(sep = ",")

    for dado in listadados:
        listalinha.append(dado)

    listaparaotabulate.append(listalinha)    

print(tabulate(listaparaotabulate, headers="firstrow", tablefmt="fancy_grid"))








