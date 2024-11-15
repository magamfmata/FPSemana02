strFrase = str(input())
arrPalavras = strFrase.split(" ")
dicPalavras = {}

for i in range(len(arrPalavras)):
    dicPalavras[arrPalavras[i]] = len(arrPalavras[i])

print(dicPalavras) 