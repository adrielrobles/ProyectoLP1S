peso/altura

edad=12
_nOMBRE_="Darinka"
apellido="Townsend"
@gravedad=9.8
$altura=168
$opcion =    true

var = 10+4-(8*$altura)

var = 5 <= 8 and not false
5 <= 8 and not false

#ESTRUCTURAS DE CONTROL
#if
if (calificacion >= 70)
  iterador += 1
end

#until
iterador = 0 
until (iterador > 5)
  iterador += 1
end

#case
edad = 5 
case edad
when 0 .. 2 
  iterador += 1
when 3 .. 12
  iterador += 1
when 13 .. 18
  iterador += 1
else
  iterador += 1
end

#ARREGLO
my_arr = Array.new
my_other_arr = []
my_third_array = ["one", "two", "three"]
my_arr.push("animal")
array = ["Jean", "Adriel", "Darinka"] 
array.delete_at(1)
#SRING
apellido="Townsend"
apellido.size
apellido.insert(0,"hola ")
#HASH
calificaciones = { 'Carlos' => 5, 'Dora' => 10 }
#FUNCION
def IMC(peso,altura) 
  peso/altura
end

def IMC() 
  peso/altura
end

def IMC(peso=0,altura=5) 
  peso/altura
end
var = IMC()
