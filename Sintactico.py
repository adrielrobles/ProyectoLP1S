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
                   | funcionesString
                   | limpiarDatos
                   | estructuraEscribirArchivo
                '''
def p_cuerpo(p):
    '''cuerpo : estructurasControl
              | estructuraSalida
              | estructuraAsignacion
              | llamadoFunciones
              | estructuraArray
              | funcionesArreglo
              | funcionesString
              | limpiarDatos
              | estructuraEscribirArchivo
    '''
  
# ---------------------------------- FUNCIONES GENERALES -------------------------------------
def p_valorTodos(p):
  '''valorTodos : ENTERO
           | FLOTANTE
           | CADENA
           | FALSE
           | TRUE
           | estructuraHash
           | estructuraArray
  '''

def p_cuerpo(p):
  '''cuerpo : imprimir
            | estructuraAsignacion
  '''
# ----------------------------------Operadores Asignacion----------------------------------
def p_estructuraAsignacion(p):
  '''estructuraAsignacion : TiposNomVariables tipoAsignacion variables
                          | TiposNomVariables IGUAL variablesTotales
                          | TiposNomVariables IGUAL estructuraComparacion
                          | TiposNomVariables IGUAL estructuraArray
                          | TiposNomVariables IGUAL estructuraLeerArchivo
                          | TiposNomVariables IGUAL estructuraEntrada
                          | TiposNomVariables IGUAL estructuraAbrirArchivo
                          | NOMBRE_VARIABLE IGUAL estructuraHash
                          | NOMBRE_VARIABLE IGUAL operacion                          
                '''

def p_tipoAsignacion(p):
  '''tipoAsignacion : MAS_IGUAL
                    | RESTA_IGUAL
                    | MULTIPLICACION_IGUAL
                    | DIVISION_IGUAL
                    | MODULO_IGUAL
                    | EXPONENCIAL_IGUAL
                '''

#---------------------------------- Operacion Matematicas -------------------------------
def p_operacion(p):
  ''' operacion : valorMate operador valorMate
                | valorMate operador valorMate operador operacion
  '''

def p_valorMate(p):
  '''valorMate : ENTERO
               | FLOTANTE
  '''

def p_operador(p):
  '''operador : MAS
              | MENOS
              | MULTIPLICACION
              | POTENCIA
              | DIV
              | MODULO
  '''
# -------------------------------Operadores Comparacion---------------------------------
def p_estructuraComparacion(p):
  'estructuraComparacion : elementocomparador comparador elementocomparador'

def p_elementocomparador(p):
  '''elementocomparador : ENTERO
                        | FLOTANTE
                        | NOMBRE_VARIABLE
                        
  '''
def p_comparador(p):
  '''comparador : MAS_IGUAL
                  | RESTA_IGUAL
                  | MULTIPLICACION_IGUAL
                  | DIVISION_IGUAL
                  | MODULO_IGUAL
                  | EXPONENCIAL_IGUAL
                  | MENOR_QUE
                  | MAYOR_QUE
                  | MAYOR_IGUAL
                  | DOBLE_IGUAL
                  | MENOR_IGUAL
                  | NO_IGUAL
  '''
# ----------------------------------Estructura de Control---------------------------------
def p_estructurasControl(p):
  '''estructurasControl : estructuraIf
                        | estructuraUntil
                        | estructuraCase
   '''

def p_estructuraIf(p):
  '''estructuraIf : IF PAR_I estructuraComparacion PAR_D cuerpo END
                  | IF PAR_I estructuraComparacion PAR_D cuerpo estructuraElse END
                '''

def p_estructuraUntil(p):
  '''estructuraUntil : UNTIL PAR_I estructuraComparacion PAR_D cuerpo END
                '''

def p_estructuraElse(p):
  '''estructuraElse : ELSE cuerpo
                '''

def p_estructuraCase(p):
  'estructuraCase: CASE NOMBRE_VARIABLE SALTO_LINEA estructuraWhenI END'

def p_estructuraWhenI(p):
  '''estructuraWhenI: estructuraWhen estructuraElse
  '''

def p_estructuraWhen(p):
  '''estructuraWhen: WHEN sentenciaWhen SALTO_LINEA cuerpo
                   | estructuraWhen SALTO_LINEA WHEN sentenciaWhen SALTO_LINEA cuerpo
  '''

def p_sentenciaWhen(p):
  ''' sentenciaWhen : estructuraComparacion
                    | intervaloW
  '''

def p_intervaloW(p):
  'intervaloW : ENTERO INTERVALO ENTERO '


def p_cuerpo(p):
  '''cuerpo : imprimir
            | estructuraAsignacion
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
  '''nombreFuncionesA : PUSH PAR_I variablesTotales PAR_D
                      | DELETE PAR_I ENTERO PAR_D
  '''  
# ----------------------------------String-----------------------------------
def p_funcionesString(p):
  '''funcionesString : TiposNomVariables PUNTO nombreFuncionesS
                     | CADENA PUNTO nombreFuncionesS
  '''

def p_nombreFuncionesS(p):
  '''nombreFuncionesS : INSERT PAR_I ENTERO COMA CADENA PAR_D
                      | INSERT PAR_I ENTERO COMA TiposNomVariables PAR_D
                      | INSERT PAR_I TiposNomVariables COMA CADENA PAR_D
                      | INSERT PAR_I TiposNomVariables COMA TiposNomVariables PAR_D
                      | SIZE PAR_I  PAR_D
                      | SIZE
  '''
# ----------------------------------Hashes-----------------------------------

def p_estructuraHash(p):
  'estructuraHash : LLAVE_I cuerpoH LLAVE_D'

def p_cuerpoH(p):
  '''cuerpoH : CADENA ASIGNACION valorTodos
             | cuerpoH COMA CADENA ASIGNACION valorTodos
  '''



# ----------------------------------Funciones-----------------------------------
def p_estructuraFunciones(p):
  '''estructuraFunciones : DEF funcionSinAtributos END
                         | DEF funcionConAtributos END
                         | DEF funcionConDefectos END
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

def p_funcionConDefectos(p):
  'funcionConDefectos : NOMBRE_FUNCION PAR_I parametrosFuncionesDefecto PAR_D cuerpo'

def p_parametrosFuncionesDefecto(p):
  '''parametrosFuncionesDefecto : NOMBRE_VARIABLE IGUAL valorF
                                | NOMBRE_VARIABLE IGUAL valorF COMA parametrosFuncionesDefecto 
                                
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
def p_estructuraEntrada(p):
  '''estructuraEntrada : GETS PUNTO CHOMP
                '''
def p_limpiarDatos(p):
  '''limpiarDatos : STDOUT PUNTO FLUSH
                '''
# ----------------------------------Casting-----------------------------------

def p_castingString(p):
  ''' castingString : ENTERO PUNTO TOSTRING
                    | FLOTANTE PUNTO TOSTRING
                    | STRING PAR_I ENTERO PAR_D
                    | STRING PAR_I FLOTANTE PAR_D
  '''

def p_castingInteger(p):
  ''' castingString : CADENA PUNTO TOINTEGER
                    | FLOTANTE PUNTO TOINTEGER
                    | INTEGER PAR_I CADENA PAR_D
                    | INTEGER PAR_I FLOTANTE PAR_D
  '''

def p_castingFloat(p):
  ''' castingString : ENTERO PUNTO TOFLOAT
                    | CADENA PUNTO TOFLOAT
                    | FLOAT PAR_I ENTERO PAR_D
                    | FLOAT PAR_I CADENA PAR_D
  '''
# ----------------------------------Manejo de archivos-----------------------------------
# ----------------------------------Leer archivos-----------------------------------
def p_estructuraLeerArchivo(p):
    '''estructuraLeerArchivo : FILE PUNTO READ PAR_I TiposNomVariables PAR_D
                              | FILE PUNTO READ PAR_I CADENA PAR_D
    '''

def p_estructuraAbrirArchivo(p):
    '''estructuraAbrirArchivo : FILE PUNTO OPEN PAR_I TiposNomVariables COMA MODOAPERTURA PAR_D
                              | FILE PUNTO OPEN PAR_I CADENA COMA MODOAPERTURA PAR_D
    '''
# ----------------------------------Escribir archivos-----------------------------------
def p_estructuraEscribirArchivo(p):
    '''estructuraEscribirArchivo : FILE PUNTO WRITE PAR_I TiposNomVariables COMA TiposNomVariables PAR_D
                                 | FILE PUNTO WRITE PAR_I TiposNomVariables COMA CADENA PAR_D
                                 | FILE PUNTO WRITE PAR_I CADENA COMA CADENA PAR_D
                                 | FILE PUNTO WRITE PAR_I CADENA COMA TiposNomVariables PAR_D
    '''
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
