import ply.yacc as yacc

#Importe todos los tokens para usarlo en las reglas
from ProyectoLP import tokens

ParserTree={}
ParserTreeTodo={}
Errores=[]


def p_instrucciones(p):
  '''instrucciones : variablesTotales
                   | estructuraAsignacion
                   | estructuraComparacion
                   | estructurasControl
                   | estructuraArray
                   | funcionesArreglo
                   | funcionesString
                   | estructuraHash
                   | estructuraFunciones
                   | operacion
                   | estructuraSalida
                   | estructuraCasting
                   | limpiarDatos
                   | estructuraEscribirArchivo
                   | estructuraClase
                   | estructuraRecorrerArchivo
                   | metodosHash
                '''
  
def p_cuerpo(p):
    '''cuerpo : variablesTotales
              | estructuraAsignacion
              | estructuraComparacion
              | estructurasControl
              | estructuraArray
              | funcionesArreglo
              | funcionesString
              | estructuraHash
              | estructuraFunciones
              | llamadoFunciones
              | operacion
              | estructuraSalida
              | estructuraCasting
              | limpiarDatos
              | estructuraEscribirArchivo
              | estructuraRecorrerArchivo
    '''

# ----------------------------------Variables (Darinka Townsend)-----------------------------------
def p_variablesTotales(p):
    '''variablesTotales : variables 
                        | boleanos
    '''

def p_variables(p):
  '''variables : CADENA
               | numericos
               | TiposNomVariables
  '''


def p_TiposNomVariables(p):
  '''TiposNomVariables : NOMBRE_VARIABLE
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

def p_estructuraClase(p):
  'estructuraClase : CLASS NOMBRE_CLASE'
  ParserTree.append("estructuraClase")

def p_valorTodos(p):
  '''valorTodos : variablesTotales
                | estructuraHash
                | estructuraArray
  '''
 
# ----------------------------------Operadores Asignacion (Jean Moreano)----------------------------------
def p_estructuraAsignacion(p):
  '''estructuraAsignacion : TiposNomVariables tipoAsignacion variables
                          | TiposNomVariables IGUAL variablesTotales
                          | TiposNomVariables IGUAL operacion
                          | TiposNomVariables IGUAL estructuraComparacion
                          | TiposNomVariables IGUAL estructuraArray
                          | TiposNomVariables IGUAL estructuraHash
                          | TiposNomVariables IGUAL llamadoFunciones
                          | TiposNomVariables IGUAL estructuraCasting
                          | TiposNomVariables IGUAL estructuraEntrada
                          | TiposNomVariables IGUAL estructuraLeerArchivo
                          | TiposNomVariables IGUAL estructuraLeerArchivoLinea
                          | TiposNomVariables IGUAL estructuraAbrirArchivo
                          | TiposNomVariables IGUAL estructuraSplit
  '''
  Recorrido("estructuraAsignacion","Asignación")
  

def p_tipoAsignacion(p):
  '''tipoAsignacion : MAS_IGUAL
                    | RESTA_IGUAL
                    | MULTIPLICACION_IGUAL
                    | DIVISION_IGUAL
                    | MODULO_IGUAL
                    | EXPONENCIAL_IGUAL
                '''

#---------------------------------- Operacion Matematicas (Darinka Townsend)-------------------------------

def p_operacion(p):
  ''' operacion : variablesoperacion operador variablesoperacion
                | PAR_I variablesoperacion operador variablesoperacion PAR_D
                | variablesoperacion operador variablesoperacion operador operacion
                | PAR_I variablesoperacion operador variablesoperacion PAR_D operador operacion
  '''
  Recorrido("operacion","Operacion Matematica")
  

def p_variablesoperacion(p):
  ''' variablesoperacion : numericos
                         | TiposNomVariables
  '''

def p_operador(p):
  '''operador : MAS
              | MENOS
              | MULTIPLICACION
              | POTENCIA
              | DIV
              | MODULO
  '''
# -------------------------------Operadores Comparacion (Darinka Townsend)---------------------------------
def p_estructuraComparacion(p):
  '''estructuraComparacion : variablesTotales comparador variablesTotales
                           | NOT variablesTotales comparador variablesTotales
                           | NOT variables
                           | NOT boleanos
                           | variablesTotales comparador variablesTotales operadoresComparacion estructuraComparacion
                           '''
  
  Recorrido("estructuraComparacion","Comparación")                        

def p_comparador(p):
  '''comparador : MENOR_QUE
                | MAYOR_QUE
                | MAYOR_IGUAL
                | DOBLE_IGUAL
                | MENOR_IGUAL
                | NO_IGUAL
  '''

def p_operadoresComparacion(p):
  '''operadoresComparacion : AND
                           | OR
  '''
  
# ----------------------------------Estructura de Control (Todos)---------------------------------
def p_estructurasControl(p):
  '''estructurasControl : estructuraIf
                        | estructuraUntil
                        | estructuraCase
   '''
  
  Recorrido("estructurasControl","Estructura de Control")    
    

def p_estructuraIf(p):
  '''estructuraIf : IF PAR_I estructuraComparacion PAR_D cuerpo END
                  | IF estructuraComparacion cuerpo END
                  | IF PAR_I estructuraComparacion PAR_D cuerpo estructuraElse END
                  | IF estructuraComparacion cuerpo estructuraElse END
  '''
  Recorrido("estructuraIf","If")    

def p_estructuraUntil(p):
  '''estructuraUntil : UNTIL PAR_I estructuraComparacion PAR_D cuerpo END
                     | UNTIL estructuraComparacion cuerpo END
  '''
  Recorrido("estructuraUntil","Until")
  

def p_estructuraElse(p):
  'estructuraElse : ELSE cuerpo'
  
  Recorrido("estructuraElse","Else")

def p_estructuraCase(p):
  'estructuraCase : CASE NOMBRE_VARIABLE estructuraWhenI END'
  Recorrido("estructuraCase","Case")

def p_estructuraWhenI(p):
  'estructuraWhenI : estructuraWhen estructuraElse'
  


def p_estructuraWhen(p):
  '''estructuraWhen : WHEN sentenciaWhen cuerpo
                    | estructuraWhen WHEN sentenciaWhen cuerpo
  '''
  Recorrido("estructuraWhen","When")

def p_sentenciaWhen(p):
  ''' sentenciaWhen : estructuraComparacion
                    | intervaloW
  '''
  Recorrido("sentenciaWhen","Cuerpo de la Estructura When")

def p_intervaloW(p):
  'intervaloW : ENTERO INTERVALO ENTERO '
  Recorrido("intervaloW","Rango de numeros")
  



# ----------------------------------Estructura de Datos-----------------------------------
# ----------------------------------Array (Adriel Robles)-----------------------------------

def p_estructuraArray(p):
  '''estructuraArray : CORCHETE_I CORCHETE_D
                     | ARRAY PUNTO NEW
                     | CORCHETE_I parametrosA CORCHETE_D
                '''
  
  Recorrido("estructuraArray","Array")
                
def p_parametrosA(p):
  '''parametrosA : variablesTotales
                 | variablesTotales COMA parametrosA
  '''
  Recorrido("parametrosA","Parametros del Array")

def p_funcionesArreglo(p):
  '''funcionesArreglo : TiposNomVariables PUNTO nombreFuncionesA
                      | estructuraArray PUNTO nombreFuncionesA
  '''
  Recorrido("funcionesArreglo","Funcion de un Arreglo")

def p_nombreFuncionesA(p):
  '''nombreFuncionesA : PUSH PAR_I variablesTotales PAR_D
                      | DELETE PAR_I ENTERO PAR_D
  '''  
  Recorrido("nombreFuncionesA","Nombre de Función de un Arreglo")
# ----------------------------------String (Jean Moreano)-----------------------------------
def p_funcionesString(p):
  '''funcionesString : TiposNomVariables PUNTO nombreFuncionesS
                     | CADENA PUNTO nombreFuncionesS
  '''
  
  Recorrido("funcionesString","Funcion String")

def p_nombreFuncionesS(p):
  '''nombreFuncionesS : INSERT PAR_I ENTERO COMA CADENA PAR_D
                      | INSERT PAR_I ENTERO COMA TiposNomVariables PAR_D
                      | INSERT PAR_I TiposNomVariables COMA CADENA PAR_D
                      | INSERT PAR_I TiposNomVariables COMA TiposNomVariables PAR_D
                      | SIZE PAR_I  PAR_D
                      | SIZE
  '''
  Recorrido("nombreFuncionesS","Nombre de Funcion String")
# ----------------------------------Hashes (Darinka Townsend)-----------------------------------

def p_estructuraHash(p):
  'estructuraHash : LLAVE_I cuerpoH LLAVE_D'
  Recorrido("estructuraHash","Hash")

def p_cuerpoH(p):
  '''cuerpoH : CADENA ASIGNACION valorTodos
             | cuerpoH COMA CADENA ASIGNACION valorTodos
  '''
  Recorrido("cuerpoH","Cuerpo del Hash")



def p_metodosHash(p):
  '''metodosHash : TiposNomVariables PUNTO HAS_VALUE INTERROGACION PAR_I valorTodos PAR_D
                         | TiposNomVariables PUNTO HAS_KEY INTERROGACION PAR_I CADENA PAR_D
                         | TiposNomVariables PUNTO EMPTY INTERROGACION
                         | TiposNomVariables PUNTO CLEAR
                         | TiposNomVariables PUNTO KEYS
                         | TiposNomVariables PUNTO LENGTH
                         | TiposNomVariables PUNTO VALUES
                         | TiposNomVariables PUNTO KEY PAR_I valorTodos PAR_D
                         | TiposNomVariables PUNTO DELETE PAR_I CADENA PAR_D
                         | TiposNomVariables PUNTO DEFAULT IGUAL valorF

  '''
  Recorrido("metodosHash","Metodo del Hash")

# ----------------------------------Funciones (Adriel Robles)-----------------------------------
def p_estructuraFunciones(p):
  'estructuraFunciones : definicionF END'
  Recorrido("estructuraFUnciones","Estructura de una Funcion")

def p_definicionF(p):
  ''' definicionF : DEF funcionSinAtributos
                  | DEF funcionConAtributos
                  | DEF funcionConDefectos
  '''
  Recorrido("definicionF","Definicion de funcion")
  
def p_funcionSinAtributos(p):
  '''funcionSinAtributos : NOMBRE_FUNCION PAR_I PAR_D cuerpo
  '''
  Recorrido("funcionSinAtributos","Funcion sin atributos")

def p_funcionConAtributos(p):
  '''funcionConAtributos : NOMBRE_FUNCION PAR_I parametrosFunciones PAR_D cuerpo
  '''
  Recorrido("funcionConAtributos","Funcion con atributos")

def p_parametrosFunciones(p):
  '''parametrosFunciones : NOMBRE_VARIABLE
                         | NOMBRE_VARIABLE COMA parametrosFunciones
  '''
  Recorrido("parametrosFunciones","Parametros de la funcion")

def p_llamadoFunciones(p):
  '''llamadoFunciones : NOMBRE_FUNCION PAR_I PAR_D 
                      | NOMBRE_FUNCION PAR_I parametrosA PAR_D
  '''
  Recorrido("llamadoFunciones","llamar a una función")
  


def p_funcionConDefectos(p):
  'funcionConDefectos : NOMBRE_FUNCION PAR_I parametrosFuncionesDefecto PAR_D cuerpo'
  Recorrido("funcionConDefectos","Funcion con atributos por defecto")

def p_parametrosFuncionesDefecto(p):
  '''parametrosFuncionesDefecto : NOMBRE_VARIABLE IGUAL valorF
                                | NOMBRE_VARIABLE IGUAL valorF COMA parametrosFuncionesDefecto 
                                
  '''
  Recorrido("parametrosFuncionesDefecto","Parametros de la funcion")

def p_valorF(p):
  '''valorF : ENTERO
            | FLOTANTE
            | CADENA
            | TRUE
            | FALSE
  '''

# ----------------------------------Entrada y salida de Datos (Adriel y Jean)-----------------------------------
def p_estructuraSalida(p):
  '''estructuraSalida : operadoresSalidas cuerpoSalida
                      | operadoresSalidas PAR_I cuerpoSalida PAR_D
                '''
  
  Recorrido("estructuraSalida","Salida de Datos")
  
def p_operadoresSalidas(p):
  '''operadoresSalidas : PUTS
                       | PRINT 
                '''
  Recorrido("operadoresSalidas","Metodo de salida")

def p_cuerpoSalida(p):
  '''cuerpoSalida : variablesTotales
                  | CADENA MAS TiposNomVariables
                  | operacion
  '''
  Recorrido("cuerpoSalida","Cuerpo")

def p_estructuraEntrada(p):
  '''estructuraEntrada : GETS PUNTO CHOMP
                '''
  Recorrido("estructuraEntrada","Entrada de Datos")

def p_limpiarDatos(p):
  '''limpiarDatos : STDOUT PUNTO FLUSH
                '''
  Recorrido("limpiarDatos","Limpiar Datos")
# ----------------------------------Casting (Darinka Townsend)-----------------------------------
def p_estructuraCasting(p):
  ''' estructuraCasting : castingString
                        | castingInteger
                        | castingFloat
  '''
  
  

def p_castingString(p):
  ''' castingString : ENTERO PUNTO TOSTRING
                    | FLOTANTE PUNTO TOSTRING
                    | STRING PAR_I ENTERO PAR_D
                    | STRING PAR_I FLOTANTE PAR_D
  '''
  Recorrido("castingString","Casting a String")

def p_castingInteger(p):
  ''' castingInteger : CADENA PUNTO TOINTEGER
                    | FLOTANTE PUNTO TOINTEGER
                    | INTEGER PAR_I CADENA PAR_D
                    | INTEGER PAR_I FLOTANTE PAR_D
  '''
  Recorrido("castingInteger","Casting a Entero")

def p_castingFloat(p):
  ''' castingFloat : ENTERO PUNTO TOFLOAT
                    | CADENA PUNTO TOFLOAT
                    | FLOAT PAR_I ENTERO PAR_D
                    | FLOAT PAR_I CADENA PAR_D
  '''
  Recorrido("castingFloat","Casting a Flotante")
  
 


# ----------------------------------Manejo de archivos-----------------------------------
# ----------------------------------Leer archivos (Adriel Robles)-----------------------------------
def p_estructuraLeerArchivo(p):
    '''estructuraLeerArchivo : FILE PUNTO READ PAR_I TiposNomVariables PAR_D
                             | FILE PUNTO READ PAR_I CADENA PAR_D
    '''
    Recorrido("estructuraLeerArchivo","Leer Archivo")

def p_estructuraLeerArchivoLinea(p):
    '''estructuraLeerArchivoLinea : FILE PUNTO READLINES PAR_I TiposNomVariables PAR_D
                                  | FILE PUNTO READLINES PAR_I CADENA PAR_D
    '''
    Recorrido("estructuraLeerArchivoLinea","Linea")
    
def p_estructuraAbrirArchivo(p):
  '''estructuraAbrirArchivo : FILE PUNTO OPEN PAR_I TiposNomVariables COMA CADENA PAR_D
                              | FILE PUNTO OPEN PAR_I CADENA COMA CADENA PAR_D
  '''
  Recorrido("estructuraAbrirArchivo","Abrir Archivo")
# ----------------------------------RECORRER ARCHIVO (Adriel Robles) -----------------------------------

def p_estructuraRecorrerArchivo(p):
    '''estructuraRecorrerArchivo : variablesRecorrer PUNTO EACH DO PIPE NOMBRE_VARIABLE PIPE cuerpo END
                                 | TiposNomVariables PUNTO EACH DO PIPE NOMBRE_VARIABLE PIPE cuerpo END
                                 | estructuraAbrirArchivo DO PIPE NOMBRE_VARIABLE PIPE cuerpo END
    '''
    Recorrido("estructuraRecorrerArchivo","Recorrer Archivo")

def p_estructuraSplit(p):
  '''estructuraSplit : TiposNomVariables PUNTO SPLIT PAR_I CADENA PAR_D
                       | estructuraLeerArchivo PUNTO SPLIT PAR_I CADENA PAR_D'''
  Recorrido("estructuraSplit","Split")   

def p_variablesRecorrer(p):
    '''variablesRecorrer : estructuraLeerArchivoLinea
                         | estructuraSplit
    '''
     
# ----------------------------------Escribir archivos (Jean Moreano)-----------------------------------
def p_estructuraEscribirArchivo(p):
  '''estructuraEscribirArchivo : FILE PUNTO WRITE PAR_I TiposNomVariables COMA TiposNomVariables PAR_D
                                 | FILE PUNTO WRITE PAR_I TiposNomVariables COMA CADENA PAR_D
                                 | FILE PUNTO WRITE PAR_I CADENA COMA CADENA PAR_D
                                 | FILE PUNTO WRITE PAR_I CADENA COMA TiposNomVariables PAR_D
                                 | TiposNomVariables PUNTO WRITE PAR_I CADENA PAR_D
    '''
  Recorrido("estructuraEscribirArchivo","Escribir Archivo")
    

#Imprime errores según las reglas
def p_error(p):
  if p:
    resultadop="Error de sintaxis en el token {}".format(p.type)
    #print(resultadop)
    Errores.append("Error de sintaxis en el token {}".format(p.type))
  # Just discard the token and tell the parser it's okay.
  else:
    print("Error de sintaxis EOF en analizador sintáctico")
    Errores.append("Error de sintaxis EOF en analizador sintáctico")
   

#recorrido del parse
def Recorrido(regla,lectura):
  ParserTree[regla]=lectura
  ParserTreeTodo[regla]=lectura



def ValidaEstructuraGeneral():
  
  return Errores


#analizar código entrante
def AnalizadorSintactico(linea):
  sintactico = yacc.yacc()
  result=sintactico.parse(linea)
  
  if result is None:
    salida = (ParserTree.copy(),ParserTreeTodo,Errores)    
    
  else:
    salida = "Anàlisis Sintàctico no valido\n"  
  limpiarParseTree()
  return salida

def limpiarParseTree():
  ParserTree.clear()

def limpiarParserTreeTodo():
  ParserTreeTodo.clear()
  Errores.clear()



'''
archivo = open("prueba.rb", "r")

for linea in archivo:
        if linea != "\n" and linea[0] != '#':
            if linea[:3] == "def" or linea[:2] == "if" or linea[:5] == "until" or linea[:4] == "case" :
                nuevaLinea = linea.replace("\n", "")
                for Slinea in archivo:
                    nuevaLinea += " " + Slinea.replace("\n", "").replace("\t", "")
                    if Slinea[:3] == "end":
                        break
                linea = nuevaLinea
            print(linea.replace("\n", ""))
            result = sintactico.parse(linea)
            print()
            if result is None:
                linea = "Bloque o linea de codigo correcto \n"
            else:
                linea = "Error en la sintaxis \n"
            print(linea)

'''



