from tkinter import *
import tkinter.font as tkFont
def anlisisLexico():
    print("Analisis Lexico")
    result = Cajatexto.get("1.0","end-1c")
    print("Analisis "+result)

def analisisSintactico():
    print("Analisis Sintactico")
    result = Cajatexto.get("1.0","end-1c")
    print("Analisis "+result)

root = Tk()
root.title('Proyecto Final Programacion')
root.resizable(width=False, height=True)
# Label del titulo
title = tkFont.Font(family="Lucida Grande", size=20, weight=tkFont.BOLD)
lbred = Label(root, text="Interprete de Ruby", fg="Red", font=title)
lbred.grid(column=0, row=0, pady=10, padx=10, columnspan=2)
#Caja de texto
tituloInstrucion = tkFont.Font(family="Lucida Grande", size=10, weight=tkFont.BOLD)
lbInstruction = Label(root, text="Ingrese el algoritmo a analizar:", font=tituloInstrucion)
lbInstruction.grid(column=0, row=1, pady=10)
#Cuadro de texto para el algoritmo
Cajatexto = Text(root)
Cajatexto.grid(column=0, row=2, columnspan=2)
Cajatexto.config(width=65, height=15, font=("Consolas",12),pady=20)
# Label de Seleccion de analisis
tituloAnalisis = tkFont.Font(family="Lucida Grande", size=10, weight=tkFont.BOLD)
lbInsAnalys = Label(root, text="Seleccione el tipo de analisis que desea realizar", font=tituloAnalisis)
lbInsAnalys.grid(column=0, row=4, pady=10)
# Botones de Analisis Lexico
btnLexico = Button(root, text="Analisis Lexico", width=50, command=anlisisLexico)
btnLexico.grid(padx=10, pady=10, row=5, column=0)
# Botones de Analisis Sintactico
btnSintactico = Button(root, text="Analisis Sintactico", width=50, command=analisisSintactico)
btnSintactico.grid(padx=10, pady=10, row=5, column=1)
root.mainloop()