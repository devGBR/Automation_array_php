from msilib.schema import Directory
import os
from PySimpleGUI import PySimpleGUI as sg

directory = os.getcwd()
layout = [
    [sg.Text("Nome do arquivo:")], 
    [sg.InputText(key='nome'),
    sg.FileBrowse(initial_folder=directory)], 
    [sg.Button("Enter")]]
#janela
janela = sg.Window("Janela", layout)
#eventos
while True:
    event, values = janela.read()
    if event == 'Enter':
        nome = values['nome']
        if nome == '':
            sg.popup('Preencha o nome do arquivo!')
        else:
            sg.popup(nome)
    break
