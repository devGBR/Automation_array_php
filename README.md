#Pyth if(nome != ''):
                sg.popup(sg.Text("Assunto: "), sg.Input(key='assunto'),
                sg.Text("Digite o tipo de norma: "), sg.Input(key='tipo'),
                sg.Text("Digite o numero e data: "), sg.Input(key='data'),
                sg.Text("Digite o orgão: "), sg.Input(key='orgao'),
                sg.Text("Digite a ementa: "), sg.Input(key='ementa'))
            else: