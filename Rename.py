
# tipos =input("Digite o tipo de norma: ") 
# data = input("Digite o numero e data: ") 
# orgao = input("Digite o orgao: ")
# ementa = input("Digite a ementa: ")
# download = input("Digite o link do download: ")





campos = ["array(\n" + "    "+"\"" + "assunto"+ "\"" +"=>" + "\"" + input("Digite o assunto: ") +"\"" + "," ,
 "    " + "\"" + "tipos_de_normas"+ "\"" +"=>" + "\"" + input("Digite o tipo de norma: ") +"\"" + "," ,
 "    " + "\"" + "numero_data"+ "\"" +"=>" + "\"" + input("Digite o numero e data: ") +"\"" + "," ,
 "    " + "\"" + "orgao"+ "\"" +"=>" + "\"" + input("Digite o orgao: ") +"\"" + "," ,
 "    " +  "\"" + "ementa"+ "\"" +"=>" + "\"" + input("Digite a ementa: ") +"\"" + "," ,
 "    " +   "\"" + "download"+ "\"" +"=>" + "\"" + input("Digite o link do download: ") +"\"" + "\n" + ")" + ","]

for i in range(len(campos)):
    print(campos[i]) 

