#! C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.7_3.7.2032.0_x64__qbz5n2kfra8p0 python
from tkinter import *
from PIL import ImageTk , Image

root = Tk()
root.title('Pleno Sono ')

logo = ImageTk.PhotoImage(Image.open('cropped-plenosono_logo-1.png'))
lg = Label(image = logo)

espaco = Label(root, text = '')

def cad():
    return

def alt():
    return

def gerar():
    return

def vis():
    return

Cadas_Dist = Button(root, text = "Cadastrar Distribuidor", command = cad)
Alt_Dist = Button(root, text = "Alterar Distribuidor", command = alt)
Ger_Rel = Button(root, text = "Gerar Relatório", command = gerar)
Vis_Dist = Button(root, text = "Visualizar Distribuidor", command = vis)

Cadas_Dist.grid(row = 0, column = 0, padx = 50, pady = 50)
Alt_Dist.grid(row = 0, column = 1, padx = 50, pady = 50)

lg.grid(row = 1, column = 0, columnspan = 2)

Ger_Rel.grid(row = 2, column = 0, padx = 50, pady = 50)
Vis_Dist.grid(row = 2, column = 1, padx = 50, pady = 50)


root.mainloop()