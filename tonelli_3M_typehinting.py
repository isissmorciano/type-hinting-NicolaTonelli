#inizio
import random
# Es 1
def descrizione(nome: str, eta: int) -> str:
    return f"{nome} ha {eta} anni."
nome=input("Nome: ")                 # l'utente sceglie nome ed età
eta=input("Età: ")

# Es 2
def numero_casuale() -> int:
    return random.randint(0, 99)

# Es 3
def descrizione_eta_casuale(nome: str) -> str:
    eta = numero_casuale()
    return descrizione(nome, eta)

# Es 4
def descrizione_casuale() -> str:
    nomi = ["Mario", "Luigi", "Marco", "Paolo", "Pietro"]
    nome = random.choice(nomi)
    eta = numero_casuale()
    return descrizione(nome, eta)

# Stampo a schermo i risultati
print(descrizione(nome, eta))
print(numero_casuale())
print(descrizione_eta_casuale(nome))
print(descrizione_casuale())

#fine