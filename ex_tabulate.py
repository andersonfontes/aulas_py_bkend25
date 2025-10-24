from tabulate import tabulate

lista = [
    ["jose", "silva"],
    ["jorge", "garcia"],
    ]

print(tabulate(lista, headers=["nome","sobrenome"], tablefmt="fancy_grid"))    