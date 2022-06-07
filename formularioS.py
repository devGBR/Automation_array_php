from dataclasses import replace
from os.path import exists
from shutil import copyfile
import os

nome = input("Digite o nome do arquivo:")
global name
def renomearArquivo(nome):
    if exists(nome):
        print("Arquivo existe")
        remove = nome[:-4]
        substituir = remove.replace(" ", "_")
        substituir1 = substituir.replace(",", "")
        substituir2 = substituir1.replace("º", "")
        form = substituir2.replace(".", "")
        result = form.upper()
        name = result + ".pdf"
        return name

    else:
        print("Arquivo não encontrado")

juntar = renomearArquivo(nome)
print(juntar)
campos = ["assunto", "tipos_de_normas", "numero_data", "orgao", "ementa", "download"]
respotas = [input("Digite o assunto: "), 
            input("Digite o tipo de norma: "), 
            input("Digite o numero e data: "), 
            input("Digite o orgao: "), 
            input("Digite a ementa: "), 
            ("Digite o link do download:" , {juntar})]
resultado = "array(\n"           
for i in range(len(campos)):
    resultado +=  "\"" + campos[i] + "\"" + "=> " + "\"" , respotas[i] + "\"" + ",\n"
resultado += ")"
print(resultado)

try :
    if(juntar != None):
        copyfile(nome, juntar)
        os.remove(nome)
        print("Arquivo copiado")
except ValueError: 
        print("Erro ao copiar o arquivo")




            





#DECRETO Nº 2277 DE 6 DE MAIO DE 2022.pdf