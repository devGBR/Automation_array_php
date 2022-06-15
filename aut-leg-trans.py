from PySimpleGUI import PySimpleGUI as sg
from dataclasses import replace
from os.path import exists
import shutil
import os
import pyperclip as pc 
diretorio = os.getcwd()
#Layout:
sg.theme('Dark Blue')
layout = [
    [sg.Text("Nome do arquivo:")],
    [sg.InputText(key='nome', size=(30,1)), sg.FileBrowse(initial_folder = diretorio),],
    [sg.Text("Nome do arquivo:")],
    [sg.InputText(key='arquivo', size=(30,1))],
    [sg.Text("Assunto: ")],
    [sg.Input(key='assunto', size=(30,1))],
    [sg.Text("norma: ")], 
    [sg.Input(key='tipo', size=(30,1))],
    [sg.Text("numero e data: ")],
    [sg.Input(key='data', size=(30,1))],
    [sg.Text("orgão: ")],
    [sg.Input(key='orgao', size=(30,1))],
    [sg.Text("ementa: ")],
    [sg.Input(key='ementa', size=(30,1))],
    [sg.Button("Selecionar"), sg.Button("Visualizar")]
]

#Janela:
janela = sg.Window("Criador de array", layout)
#Eventos:
while True: 
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Selecionar':
        nome = values['nome']
        arquivo = values['arquivo']
        assunto = values['assunto']
        tipo = values['tipo']
        data = values['data']
        orgao = values['orgao']
        ementa = values['ementa']
        sg.popup(nome)
        if nome == '':
            sg.popup('Preencha o nome do arquivo!')
        else:
            if exists(nome):
                remove = arquivo[:-4]
                substituir = remove.replace(" ", "_")
                substituir1 = substituir.replace(",", "")
                substituir2 = substituir1.replace("º", "")
                form = substituir2.replace(".", "")
                result = form.upper()
                name = result + ".pdf" 
            if(name != None):
               juntar = name
               campos = "array(\n" + "    "+"\"" + "assunto"+ "\"" +"=>" + "\"" + assunto +"\"" + "," + "\n" + "    " + "\"" + "tipos_de_normas"+ "\"" +"=>" + "\"" + tipo +"\"" + "," + "\n" + "    " + "\"" + "numero_data"+ "\"" +"=>" + "\"" + data +"\"" + "," +"\n" + "    " + "\"" + "orgao"+ "\"" +"=>" + "\"" + orgao +"\"" + ","  + "\n" + "    " + "\"" + "ementa"+ "\"" +"=>" + "\"" + ementa +"\"" + "," + "\n" + "    " + "\"" + "Download"+ "\"" +"=>" + "\"" + juntar +"\"" + ")" + ","
               sg.popup(campos)
               if (campos != None):
                layout2 = [
                    [sg.Text("Copiar array?")],
                    [sg.Button("Sim"), sg.Button("Não")]]

                janela2 = sg.Window("Janela", layout2)

                while True: 
                    event , values = janela2.read()
                    if event == 'Sim':
                        pc.copy(campos)
                        sg.popup("Copiado para a area de trabalho!")
                    if event == 'Não':
                        sg.popup("Não copiado!")
                        sg.WINDOW_CLOSED
                    break
            if(name != ''):
                sg.popup(name)
                shutil.copyfile(nome, name)
                os.remove(nome)
                sg.popup("Arquivo criado com sucesso!")
            else:
                print("Preencha o nome do arquivo!")
           
              
            # if(name != None):
                #     juntar = renomearArquivo(nome)
                #     campos = ["array(\n" + "    "+"\"" + "assunto"+ "\"" +"=>" + "\"" + assunto +"\"" + "," ,"    " + "\"" + "tipos_de_normas"+ "\"" +"=>" + "\"" + tipo +"\"" + "," ,"    " + "\"" + "numero_data"+ "\"" +"=>" + "\"" + data +"\"" + "," ,"    " + "\"" + "orgao"+ "\"" +"=>" + "\"" + orgao +"\"" + "," ,"    " + "\"" + "ementa"+ "\"" +"=>" + "\"" + ementa +"\"" + "," ,"    " + "\"" + "Download"+ "\"" +"=>" + "\"" + juntar +"\"" + ","]
                #     with open("array.txt", "a") as f:
                #         f.writelines(campos)
                #     f.close()
                #     sg.popup("Arquivo criado com sucesso!")
                #     janela.close()
            break
