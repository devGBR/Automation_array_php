from cProfile import run
from tkinter import Button
from turtle import color
from webbrowser import BackgroundBrowser
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

GUI = Builder.load_file('tela.kv')

class Meuapp(App):
    def build(self):
        return GUI
    def abrir(self):
        Abrir = open
      
Meuapp().run()