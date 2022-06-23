import ply.lex as lexico

reservadas = {
  #Palabras reservadas
  "in":"IN",
  "class":"CLASS",
  "puts":"PUTS",
  #estructura de control
  "if":"IF",
  "else":"ELSE",
  "until":"UNTIL",
  "end":"END",
  "case":"case",
  "elseif":"ELSEIF",
  #tipado
  "String":"STRING",
  "Integer":"INTEGER",
  "Float":"FLOAT",
  #funciones
  "def":"DEF",
  "end":"END",
  "return":"RETURN",

  #Darinka Townsend
  #OPERADORES DE COMPARACION
  "and" : "AND",
  "or" : "OR",
  "not" : "NOT",
  #HASHES
  "dict" : "DICCIONARIO"

  
}

tokens = ("MAS", "MENOS", "DIV", "MULTIPLICACION", "MODULO","DOBLE_IGUAL","MULTIPLICACION_IGUAL","EXPONENCIAL_IGUAL"       , "MENOR_IGUAL","NO_IGUAL","BACKS", "MENOR_QUE", "MAYOR_IGUAL",
         "IGUAL", "PAR_I", "PAR_D",
         "NOMBRE_VARIABLE","VALOR_ENTERO","VALOR_DECIMAL","CORCHETE_D","CORCHETE_I","ASIGNACION","t_LLAVE_I","t_LLAVE_D") + tuple(reservadas.values())

#Definir expresiones regulares
#Darinka Townsend
#OPERADORES ARITMETICOS
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION= r'\*'
t_DIV= r'/'
t_MODULO = r'%'
t_MULTIPLICACION_IGUAL = r'\*='
t_EXPONENCIAL_IGUAL = r'\*\*='
t_PAR_D = r'\)'
t_PAR_I = r'\('
t_IGUAL = r'='

#HASHES
t_ASIGNACION = r'=>'
t_LLAVE_I = r'\{'
t_LLAVE_D = r'\}'




#OPERADORES LOGICOS
t_MENOR_QUE = r'<'
t_MAYOR_IGUAL = r'>='
t_DOBLE_IGUAL= r'=='
t_MENOR_IGUAL = r'<='
t_NO_IGUAL = r'!='
t_ignore = " \t"


#caractere especiales
t_BACKS = r'\\'
t_VALOR_ENTERO=r'[0-9]+'
t_VALOR_DECIMAL=r'[0-9]+.[0-9]+'
t_CORCHETE_I=r'\['
t_CORCHETE_D=r'\]'

#Darinka Townsend
def t_NOMBRE_VARIABLE(t):
  r'([a-z]|_|\$|\@)[a-zA-Z0-9_]+'
  t.type = reservadas.get(t.value,"NOMBRE_VARIABLE")
  return t



def t_contadorLineas(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print(f"Caracter no reconocido {t.value[0]} en línea {t.lineno}")
    t.lexer.skip(1)
  
validador = lexico.lex()

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break 
        print(tok)

linea=" "
codigo = open("source.vb")
for linea in codigo:
  validador.input(linea)
  getTokens(validador)
codigo.close()

print("Analisis terminado... :)")