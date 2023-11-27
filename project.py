import PyPDF2
import os

mesclar = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if".pdf" in arquivo:
        mesclar.append(f"arquivos/{arquivo}")

mesclar.write("PDF Final.pdf")