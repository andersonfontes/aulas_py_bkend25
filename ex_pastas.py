from pathlib import Path

print ( Path.cwd() )
print("----------")

caminho = Path('__pycache__')

print(caminho)

arquivos = caminho.iterdir()

for arquivo in arquivos:
    print(arquivo)

if (caminho / Path('teste')).exists():
    print("o arquivo existe!")
else:
    print("nao existe")

Path(caminho / Path('pasta2')).mkdir()    