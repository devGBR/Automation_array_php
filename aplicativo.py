from genericpath import exists
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class incrementar(BoxLayout):
    pass
    def select(self):
         if exists(self.ids.nome.text):
            print("Arquivo existe")
            remove = nome[:-4]
            substituir = remove.replace(" ", "_")
            substituir1 = substituir.replace(",", "")
            substituir2 = substituir1.replace("º", "")
            form = substituir2.replace(".", "")
            result = form.upper()
            name = result + ".pdf"
            print(name)
            return name
    def view_file(self):
        if exists(self.ids.nome.text):
            print("Arquivo existe")
            print(self.ids.nome.text)
            return self.ids.nome.text
        else:
            print("Arquivo não encontrado")
class teste(App):
    def build(self):
        return incrementar()
    
teste().run()