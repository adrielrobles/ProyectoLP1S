
import ply.yacc as yacc

#Importe todos los tokens para usarlo en las reglas
from ProyectoLP import tokens

def p_sentencias(p):
  '''sentencias : NOMBRE_VARIABLE
                '''
#Imprime errores según las reglas
def p_error(p):
    if p:
        print("Error de sintaxis en token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Error de sintaxis EOF")

# Construye el parser
sintactico = yacc.yacc()

while True:
    try:
      linea = input('vb.net>> ')
    except EOFError:
        break
    if not linea: continue
    result = sintactico.parse(linea)
    print(result)

'''
linea=" "
codigo = open("source.vb")
for linea in codigo:
  result = sintactico.parse(linea)
  print(result)
codigo.close()

print("Proyecto casi terminado... :)")
'''