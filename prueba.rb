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
calificaciones.default = 0
calificaciones.clear
calificacion.empty?
calificaciones.has_key?('Carlos')
calificaciones.has_value?(5)
calificaciones.key(5)
calificaciones.keys
calificaciones.length
calificaciones.delete('Carlos')
calificaciones.values
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

print("Hola mundo")
puts "¿En qué ciudad te gustaría vivir?"
ciudad = gets.chomp
puts "La ciudad es " + ciudado

123.5.to_s 
String(123.5) 
"123.50".to_i	
Integer("123.50") 

"123.50".to_f 
Float("123.50") 

content = File.read("contenido.txt")
lines = content.split("\n") 

lines = File.readlines("contenido.txt") 
lines = File.open("cuento.txt", "w")

lines.each do |line| puts line end 
File.readlines("contenido.txt").each do |line| puts line end
File.read("contenido.txt").split("\n").each do |line| puts line end
File.open("cuento.txt", "w") do |file| file.write("Había una vez ...") end