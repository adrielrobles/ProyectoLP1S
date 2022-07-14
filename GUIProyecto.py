from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter.ttk import Treeview
from ProyectoLP import analizar
from Sintactico import AnalizadorSintactico

def anlisisLexico():
    print("Analisis Lexico")
    result = Cajatexto.get("1.0","end-1c")
    tokens = analizar(result)
    for row in tabla.get_children():
        tabla.delete(row)
    for token in tokens:
        token_r = ''
        token_r = token_r + token + '\n'
        t = token_r.split(',')
        tabla.insert(
        "",
        tk.END,
        text=t[0].split('(')[1],
        values=(t[1], t[-1].split(')')[0]))

    # text_code_lex = st.ScrolledText(root, width=65, height=20)
    # text_code_lex.insert("1.0", token_r)
    # text_code_lex.grid(column=5, row=2, padx=10, pady=10, columnspan=2)
    # text_code_lex.configure(state="disabled")
    

def analisisSintactico():
    
    print("Analisis Sintactico")
    result = Cajatexto.get("1.0","end-1c")
    numeroLinea=0
    
    resultado_es=result
    if(len(AnalizadorSintactico(resultado_es)[1])==0):
        Encabezado="No hay estructura general"
    else:
        Encabezado=reglasPorLinea(AnalizadorSintactico(resultado_es)[1])
    todo="General: {}\n--- Análisis Linea a Linea ---\n".format(Encabezado)
    
    
    for linea in result.split("\n"):
        print(AnalizadorSintactico(linea)[0])
        if(len(AnalizadorSintactico(linea)[0])!=0):
            estructura=reglasPorLinea(AnalizadorSintactico(linea)[0])
            todo+="{}: {}\n".format(numeroLinea,estructura)
            
        else:
            todo+="{}: {}\n".format(numeroLinea,"Error de Sintaxis")

        numeroLinea+=1  
         
    # con este codigo rellenas la caja de texto
    text_code_lex.insert("1.0", todo)
    text_code_lex.configure(state="disabled")

def reglasPorLinea(DicReglas):
    lista_reglas=list(DicReglas.values())[::-1]
    string_reglas=" -> ".join(lista_reglas)
    return string_reglas

root = Tk()
root.title('Proyecto Final Programacion')
root.resizable(width=False, height=True)
# Label del titulo
title = tkFont.Font(family="Lucida Grande", size=20, weight=tkFont.BOLD)
lbred = Label(root, text="Interprete de Ruby", fg="black", font=title)
lbred.grid(column=0, row=0, pady=10, padx=10, columnspan=2)
#Caja de texto
tituloInstrucion = tkFont.Font(family="Lucida Grande", size=10, weight=tkFont.BOLD)
lbInstruction = Label(root, text="Ingrese el algoritmo a analizar:", font=tituloInstrucion)
lbInstruction.grid(column=0, row=1, pady=10)
#Cuadro de texto para el algoritmo
Cajatexto = Text(root)
Cajatexto.grid(column=0, row=2, columnspan=2)
Cajatexto.config(width=55, height=15, font=("Consolas",12),pady=20)
# Label de Seleccion de analisis
tituloAnalisis = tkFont.Font(family="Lucida Grande", size=10, weight=tkFont.BOLD)
lbInsAnalys = Label(root, text="Seleccione el tipo de analisis que desea realizar", font=tituloAnalisis)
lbInsAnalys.grid(column=0, row=4, pady=10)
# Botones de Analisis Lexico
btnLexico = Button(root, text="Analisis Lexico", width=30, command=anlisisLexico)
btnLexico.grid(padx=10, pady=10, row=5, column=0)
# Botones de Analisis Sintactico
btnSintactico = Button(root, text="Analisis Sintactico", width=30, command=analisisSintactico)
btnSintactico.grid(padx=10, pady=10, row=5, column=1)

#Tabla resultado tokens lexico
tabla = Treeview(root,height = 15, columns =("tipo", "codigo") )
tabla.grid(row = 2, column = 5, columnspan = 2)
tabla.heading('#0', text = 'Nombre', anchor = CENTER)
tabla.heading('tipo', text = 'Tipo', anchor = CENTER)
tabla.heading('codigo', text = 'Codigo', anchor = CENTER)

# Resultado Analisis Sintatico
text_code_lex = st.ScrolledText(root, width=60, height=5)
text_code_lex.grid(column=0, row=6, padx=10, pady=10, columnspan=2)


root.mainloop()