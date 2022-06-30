import ply.yacc as yacc

#Importe todos los tokens para usarlo en las reglas
from ProyectoLP import tokens

def p_instrucciones(p):
  '''instrucciones : estructurasControl
                   | estructuraFunciones
                   | estructuraSalida
                   | estructuraAsignacion
                   | llamadoFunciones
                   | estructuraArray
                   | funcionesArreglo
                '''
def p_cuerpo(p):
    '''cuerpo : estructurasControl
              | estructuraSalida
              | estructuraAsignacion
              | llamadoFunciones
              | estructuraArray
              | funcionesArreglo
    '''
# ----------------------------------Operadores Asignacion----------------------------------
def p_estructuraAsignacion(p):
  '''estructuraAsignacion : TiposNomVariables tipoAsignacion variables
                          | TiposNomVariables IGUAL variablesTotales
                          | TiposNomVariables IGUAL estructuraComparacion
                          | TiposNomVariables IGUAL estructuraArray
                          | TiposNomVariables IGUAL estructuraAbrirArchivo
                          Falta operaciones matematicas, llamados de funciones, hashes,
                          , casting, entrada de datos
                '''

def p_tipoAsignacion(p):
  '''tipoAsignacion : MAS_IGUAL
                    | RESTA_IGUAL
                    | MULTIPLICACION_IGUAL
                    | DIVISION_IGUAL
                    | MODULO_IGUAL
                    | EXPONENCIAL_IGUAL
                '''
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
# ----------------------------------Array-----------------------------------

def p_estructuraArray(p):
  '''estructuraArray : CORCHETE_I CORCHETE_D
                     | ARRAY PUNTO NEW
                     | CORCHETE_I parametrosA CORCHETE_D
                '''
                
def p_parametrosA(p):
  '''parametrosA : variablesTotales
                 | variablesTotales COMA parametrosA
  '''

def p_funcionesArreglo(p):
  '''funcionesArreglo : TiposNomVariables PUNTO nombreFuncionesA 
  '''

def p_nombreFuncionesA(p):
  '''nombreFuncionesA : PUSH  PAR_I variablesTotales PAR_D
                      | DELETE PAR_I ENTERO PAR_D
  '''  
# ----------------------------------String-----------------------------------

# ----------------------------------Hashes-----------------------------------


# ----------------------------------Funciones-----------------------------------
def p_estructuraFunciones(p):
  '''estructuraFunciones : DEF funcionSinAtributos END
                         | DEF funcionConAtributos END
  '''
  
def p_funcionSinAtributos(p):
  '''funcionSinAtributos : NOMBRE_FUNCION PAR_I PAR_D cuerpo
  '''

def p_funcionConAtributos(p):
  '''funcionConAtributos : NOMBRE_FUNCION PAR_I parametrosFunciones PAR_D cuerpo
  '''

def p_parametrosFunciones(p):
  '''parametrosFunciones : TiposNomVariables
                         | TiposNomVariables COMA parametrosFunciones
  '''
def p_llamadoFunciones(p):
  '''llamadoFunciones : NOMBRE_FUNCION PAR_I PAR_D 
                      | NOMBRE_FUNCION PAR_I parametrosFunciones PAR_D
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
  '''cuerpoSalida : variablesTotales
                  | CADENA MAS TiposNomVariables
  '''
# ----------------------------------Casting-----------------------------------
# ----------------------------------Manejo de archivos-----------------------------------
# ----------------------------------Leer archivos-----------------------------------
def p_estructuraAbrirArchivo(p):
    '''estructuraAbrirArchivo : FILE PUNTO READ  PAR_I TiposNomVariables PAR_D
                              | FILE PUNTO READ  PAR_I CADENA PAR_D
    '''
# ----------------------------------Escribir archivos-----------------------------------

# ----------------------------------Variables-----------------------------------
def p_variablesTotales(p):
    '''variablesTotales : variables 
                        | boleanos
    '''
def p_variables(p):
  '''variables : CADENA
               | numericos
               | TiposNomVariables
                '''

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
