from dataclasses import replace
from os.path import exists
from shutil import copyfile
import os

nome = input("Digite o nome do arquivo:")

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

campos = ["array(\n" + "    "+"\"" + "assunto"+ "\"" +"=>" + "\"" + input("Digite o assunto: ") +"\"" + "," ,
 "    " + "\"" + "tipos_de_normas"+ "\"" +"=>" + "\"" + input("Digite o tipo de norma: ") +"\"" + "," ,
 "    " + "\"" + "numero_data"+ "\"" +"=>" + "\"" + input("Digite o numero e data: ") +"\"" + "," ,
 "    " + "\"" + "orgao"+ "\"" +"=>" + "\"" + input("Digite o orgao: ") +"\"" + "," ,
 "    " +  "\"" + "ementa"+ "\"" +"=>" + "\"" + input("Digite a ementa: ") +"\"" + "," ,
 "    " +   "\"" + "download"+ "\"" +"=>" + "\"" + juntar +"\"" + "\n" + ")" + ","]

for i in range(len(campos)):
    print(campos[i]) 


try :
    if(juntar != None):
        copyfile(nome, juntar)
        os.remove(nome)
        print("Arquivo copiado")
except ValueError: 
        print("Erro ao copiar o arquivo")
