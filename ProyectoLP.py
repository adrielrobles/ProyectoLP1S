from re import T
import ply.lex as lexico
reservadas = {
  #Empieza Adriel Robles
  #Palabras reservadas
  "in":"IN","alias":"ALIAS","break":"BREAK","undef":"UNDEF","defined?":"DEFINED",
  "class":"CLASS","ensure":"ENSURE","unlees":"UNLEES","in":"IN","module":"MODULE",
  "next":"NEXT","nil":"NIL","in":"IN","redo":"REDO","rescue":"RESCUE",
  "retry":"RETRY","yield":"YIELD","self":"SELF","super":"SUPER","then":"THEN",
  "_FILE_":"VFILE","_LINE_":"LINE","val":"VAL","new":"NEW",
  #estructura de control
  "if":"IF","else":"ELSE","until":"UNTIL","end":"END","case":"CASE","elseif":"ELSEIF",
  "do":"DO","for":"FOR","when":"WHEN","while":"WHILE", "each":"EACH",
  #tipado
  "String":"STRING","Integer":"INTEGER","Float":"FLOAT","Array":"ARRAY",
  #funciones
  "def":"DEF","end":"END","return":"RETURN",
  #Termina Adriel Robles

  # Empieza Jean Moreano
  #STRING
  "insert":"INSERT","size":"SIZE",
  #clases
  "class" : "CLASS",
  #boolean
  "false" : "FALSE","true": "TRUE",
  #casting
  "to_s" :"TOSTRING", "to_i":"TOINTEGER", "to_f":"TOFLOAT",
  #manejo de archivos
  "File" : "FILE","read":"READ","write":"WRITE","open":"OPEN", "split":"SPLIT","STDOUT":"STDOUT",
  "readlines":"READLINES",

  # Termina Jean Moreano

  #Empieza Darinka Townsend
  #OPERADORES DE COMPARACION
  "and" : "AND","or" : "OR","not" : "NOT",
  #HASHES
  "dict" : "DICCIONARIO","push" : "PUSH","delete" : "DELETE", "default" : "DEFAULT", "empty" : "EMPTY","Hash" : "HASH",
  "has_key" : "HAS_KEY","has_value" : "HAS_VALUE","key" : "KEY","keys" : "KEYS","length" : "LENGTH","values":"VALUES",
  "clear" : "CLEAR",
  #MANEJO DE ENTRADA Y SALIDA DE DATOS
  "puts" : "PUTS",
  "gets" : "GETS",
  "chomp" : "CHOMP",
  "flush" : "FLUSH",
  "print" : "PRINT"
  #termina Darinka Townsend
}

tokens = ["MAS", "MENOS", "DIV", "MULTIPLICACION", "MODULO","DOBLE_IGUAL","MULTIPLICACION_IGUAL","EXPONENCIAL_IGUAL", 
          "MENOR_IGUAL","NO_IGUAL","BACKS", "MENOR_QUE", "MAYOR_IGUAL","IGUAL", "PAR_I", "PAR_D","NOMBRE_VARIABLE","VARIABLE_GLOBAL",
           "VARIABLE_INSTANCIA","VARIABLE_CLASE","NOMBRE_CLASE", "DIVISION_IGUAL","RESTA_IGUAL","MODULO_IGUAL", "ENTERO","FLOTANTE","CADENA",
          "CORCHETE_D","INTERROGACION","CORCHETE_I","ASIGNACION","PIPE","POTENCIA","LLAVE_I","INTERVALO","LLAVE_D","NOMBRE_FUNCION","PUNTO","MAS_IGUAL","COMA","MAYOR_QUE"] +list(reservadas.values())

#Definir expresiones regulares
#Empieza Darinka Townsend
#OPERADORES ARITMETICOS
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION= r'\*'
t_POTENCIA=r'\*\*'
t_DIV= r'\/'
t_MODULO = r'%'
t_MAS_IGUAL=r'\+='
t_MULTIPLICACION_IGUAL = r'\*='
t_EXPONENCIAL_IGUAL = r'\*\*='
t_PAR_D = r'\)'
t_PAR_I = r'\('
t_IGUAL = r'='

#HASHES
t_ASIGNACION = r'=>'
t_LLAVE_I = r'\{'
t_LLAVE_D = r'\}'
t_INTERROGACION = r'\?'


#OPERADORES LOGICOS
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_MAYOR_IGUAL = r'>='
t_DOBLE_IGUAL= r'=='
t_MENOR_IGUAL = r'<='
t_NO_IGUAL = r'!='
t_ignore = " \t"
t_ignore_comment = r'\#.*'

#caractere especiales
t_BACKS = r'\\'
t_CORCHETE_I=r'\['
t_CORCHETE_D=r'\]'
t_PUNTO=r'\.'
t_COMA=r'\,'
t_INTERVALO=r'\.\.'
t_PIPE=r'\|'
# termina Darinka Townsend
# empieza Jean Moreano

#operadores de asignacion
t_RESTA_IGUAL=r'-='
t_DIVISION_IGUAL = r'/='
t_MODULO_IGUAL = r'%='

#Tipos de datos
t_ENTERO = r'0|\-?[1-9][0-9]*'
t_FLOTANTE = r'(0|\-?[1-9][0-9]*)\.([0-9]*)'


#Termina Jean Moreano

#Empieza Darinka Townsend
def t_NOMBRE_VARIABLE(t):
  r'([a-z]|_)[a-zA-Z0-9_]*'
  t.type = reservadas.get(t.value,"NOMBRE_VARIABLE")
  return t
  
def t_VARIABLE_GLOBAL(t):
  r'\$[a-zA-Z0-9_]*'
  t.type = reservadas.get(t.value,"VARIABLE_GLOBAL")
  return t

def t_VARIABLE_INSTANCIA(t):
  r'\@[a-zA-Z0-9_]*'
  t.type = reservadas.get(t.value,"VARIABLE_INSTANCIA")
  return t

def t_VARIABLE_CLASE(t):
  r'\@@[a-zA-Z0-9_]*'
  t.type = reservadas.get(t.value,"VARIABLE_CLASE")
  return t

def t_COMENTARIO(t):
  r'\#.*'

# termina Darinka Townsend
#Empieza Adriel Robles
def t_NOMBRE_FUNCION(t):
  r'[a-zA-Z][a-zA-Z0-9_]*'
  t.type = reservadas.get(t.value,"NOMBRE_FUNCION")
  return t
#termina Adriel Robles

#Empieza Jean Moreano
def t_NOMBRE_CLASE(t):
  r'[A-Z][a-z]+(_[A-Z][a-z]+|[A-Z][a-z]+)*'
  t.type = reservadas.get(t.value,"NOMBRE_CLASE")
  return t

def t_CADENA(t):
  r'(\"|\').*?(\"|\')'
  t.value = t.value[1:-1]
  return t

#Termina Jean Moreano
#Empieza Adriel Robles
def t_contadorLineas(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

error = []   
toks = []

def t_error(t):
    error.append(f"LexToken(Caracter no reconocido,{t.value[0]},{t.lineno},{t.lineno})")
    t.lexer.skip(1)
    

def analizar(data):
    validador = lexico.lex()
    global toks
    toks =[]
    global error
    error = []
    validador.input(data)
    while True:
        tok = validador.token()
        if not tok:
            break 
        toks.append(str(tok))
    if len(error)> 0:
        for er in error:
          toks.append(er)
    return toks


'''
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break 
        print(tok)


print("Analisis terminado... :)")


linea=" "
codigo = open("prueba.rb",encoding="utf8")
for linea in codigo:
  validador.input(linea)
  getTokens(validador)
codigo.close()
'''
#termina Adriel Robles
