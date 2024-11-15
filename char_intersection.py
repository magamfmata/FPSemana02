strFrase = str(input())
arrPalavras = strFrase.split(" ")
dicPalavras = {}

for i in range(len(arrPalavras)):
    dicPalavras[arrPalavras[i]] = len(arrPalavras[i])

print(dicPalavras) 

palavra1 = input()
palavra2 = input()

interseçao = set(palavra1) and set(palavra2)

resultado=""

for car in palavra1:
    if car in interseçao and car not in resultado:
        resultado+=car

print(resultado)
print(interseçao)
