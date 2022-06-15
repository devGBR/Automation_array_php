
from copy import copy
from msilib.schema import Directory
import os
from PySimpleGUI import PySimpleGUI as sg

directory = os.getcwd()
layout = [
    [sg.Text("Nome do arquivo:")], 
    [sg.InputText(key='nome'),
    sg.FileBrowse(initial_folder=directory)], 
    [sg.Button("Enter")]]
layout2 = [
    [sg.Text("Copiar array?")],
    [sg.Button("Sim"), sg.Button("Não")]]
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
         janela2 = sg.Window("Janela", layout2)
         while True: 
            event , values = janela2.read()
            if event == 'Sim':
                sg.popup(nome)
            if event == 'Não':
                break

    break
