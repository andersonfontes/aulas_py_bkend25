#exemplo1: lendo arquivo e colocando as linhas em uma lista
conteudoarquivo = open("exemplo_outra_codificacao.txt"  ,  "r" )

linhas = conteudoarquivo.readlines()

print(linhas)

#exemplo2: abrindo um arquivo modo escrita (w) e escrevendo nele
arquivoescrever = open("testew.txt","a")

string = "\nOla sou texto totalmente diferente de novo"

arquivoescrever.write(string)

arquivoescrever.close()

#exemplo3: abrindo arquivo em modop append (a) para continuar escrevendo nele
arquivoappend = open("testew.txt","a")

novastring = " \n OLA EU SOU UMA NOVA LINHA INSERIDA AQUI"

arquivoappend.write(novastring)