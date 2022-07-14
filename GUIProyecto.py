from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter.ttk import Treeview
from ProyectoLP import analizar
from Sintactico import AnalizadorSintactico
def Limpiar():
    for row in tabla.get_children():
        tabla.delete(row)
    text_code_lex.configure(state="normal")
    Cajatexto.delete("1.0","end")
    text_code_lex.delete("1.0","end")

def Compilacion():
    anlisisLexico()
    analisisSintactico()

def anlisisLexico():
    print("Analisis Lexico")
    result = Cajatexto.get("1.0","end-1c")
    tokens = analizar(result)
    for row in tabla.get_children():
        tabla.delete(row)
    print (tokens)
    for token in tokens:
        token_r = ''
        token_r = token_r + token + '\n'
        t = token_r.split(',')
        tabla.insert(
        "",
        tk.END,
        text=t[0].split('(')[1],
        values=(t[1], t[-2]))

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
lbred.grid(column=0, row=0, pady=10, padx=10, columnspan=5)
#Caja de texto
tituloInstrucion = tkFont.Font(family="Lucida Grande", size=10, weight=tkFont.BOLD)
lbInstruction = Label(root, text="Ingrese el algoritmo a analizar:", font=tituloInstrucion)
lbInstruction.grid(column=0, row=1, pady=10)
lbTituloLexico = Label(root, text="Analisis Lexico", font=tituloInstrucion)
lbTituloLexico.grid(column=1, row=1, pady=10)
#Tabla resultado tokens lexico
tabla = Treeview(root,height = 15, columns =("tipo", "codigo") )
tabla.grid(row = 2, column = 1, padx=10)
tabla.heading('#0', text = 'Nombre', anchor = CENTER)
tabla.heading('tipo', text = 'Tipo', anchor = CENTER)
tabla.heading('codigo', text = 'Codigo', anchor = CENTER)
#Cuadro de texto para el algoritmo
Cajatexto = Text(root)
Cajatexto.grid(column=0, row=2)
Cajatexto.config(width=55, height=15, font=("Consolas",12),pady=20)
#titulo Sintactico
lbTituloSintactico = Label(root, text="Analisis Sintactico", font=tituloInstrucion)
lbTituloSintactico.grid(column=0, row=3, pady=15)
# Botones de Analisis Lexico
btnLexico = Button(root, text="Compilar", width=30, command=Compilacion)
btnLexico.grid(row=6, column=1)
# Botones de Analisis Sintactico
btnLimpiar = Button(root, text="Limpiar Codigo", width=30, command=Limpiar)
btnLimpiar.grid( row=3, column=1)
# Resultado Analisis Sintatico
text_code_lex = st.ScrolledText(root, width=60, height=5)
text_code_lex.grid(column=0, row=6, padx=10, pady=10)


root.mainloop()