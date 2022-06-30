
import ply.yacc as yacc

#Importe todos los tokens para usarlo en las reglas
from ProyectoLP import tokens

def p_instrucciones(p):
  '''instrucciones : estructurasControl
                   | estructuraFunciones
                   | estructuraSalida
                '''
def p_cuerpo(p):
    '''cuerpo : estructurasControl
              | estructuraSalida
    '''
# ----------------------------------Operadores Asignacion----------------------------------

# ----------------------------------Operadores Comparacion---------------------------------
def p_estructuraComparacion(p):
  '''estructuraComparacion : 
                '''
# ----------------------------------Estructura de Control---------------------------------
def p_estructurasControl(p):
  '''estructurasControl : estructuraIf
   '''

def p_estructuraIf(p):
  '''estructuraIf : IF PAR_I estructuraComparacion PAR_D cuerpo END
                  | IF PAR_I estructuraComparacion PAR_D cuerpo estructuraElse END
                '''
def p_estructuraElse(p):
  '''estructuraElse : ELSE cuerpo
                '''

               
# ----------------------------------Estructura de Datos-----------------------------------
# ----------------------------------Funciones-----------------------------------
def p_estructuraFunciones(p):
  '''estructuraFunciones : DEF funcionSinAtributos END
  '''
  
def p_funcionSinAtributos(p):
  '''funcionSinAtributos : NOMBRE_FUNCION PAR_I PAR_D cuerpo
  '''
# ----------------------------------Entrada y salida de Datos-----------------------------------
def p_estructuraSalida(p):
  '''estructuraSalida : operadoresSalidas cuerpoSalida
                      | operadoresSalidas PAR_I cuerpoSalida PAR_D
                '''
def p_operadoresSalidas(p):
  '''operadoresSalidas : PUTS
                       | PRINT 
                '''

def p_cuerpoSalida(p):
  '''cuerpoSalida : variables
                  | CADENA MAS TiposNomVariables
  '''
# ----------------------------------Casting-----------------------------------
# ----------------------------------Manejo de archivos-----------------------------------

# ----------------------------------Variables-----------------------------------
def p_variables(p):
  '''variables : CADENA
               | numericos
               | TiposNomVariables
               | boleanos '''

def p_tiposNomVariables(p):
  '''tiposNomVariables : NOMBRE_VARIABLE
                       | VARIABLE_GLOBAL
                       | VARIABLE_INSTANCIA
                       | VARIABLE_CLASE '''

def p_boleanos(p):
    '''boleanos : TRUE 
                | FALSE
    '''
def p_numericos(p):
    '''numericos : ENTERO 
                 | FLOTANTE
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