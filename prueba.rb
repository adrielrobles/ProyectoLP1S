#PROYECTO PRIMER PARCIAL PARTE A 
#NOMBRES:
#Darinka Townsend
#Jean Moreano
# Adriel Robles

#CODIGO DE PRUEBA 
  
#ESCRITURA DE VARIABLES
edad=12
_nOMBRE_="Darinka"
apellido="Townsend"
@gravedad=9.8
$altura=168

#ENTRADA Y SALIDA DE DATOS

print("Hola mundo")
puts "¿En qué ciudad te gustaría vivir?"

# gets y chomp
ciudad = gets.chomp
puts "La ciudad es " + ciudad


#ARREGLO
my_arr = Array.new my_other_arr = []
my_third_array = ["one", "two", "three"]
my_arr.push("animal")
array = ["Jean", "Adriel", "Darinka"] array.delete_at(1)

#HASH
calificaciones = { 'Carlos' => 5,
  'Dora' => 10
  }
  
  puts calificaciones
  



#CLASE
class Integer
a = Array.new  + [12345]  #  Array  agregado.
b = String.new + 'hello'  #  String agregado.
c = Time.new

puts 'a = '+a.to_s
puts 'b = '+b.to_s
puts 'c = '+c.to_s

#ESTRUCTURAS DE CONTROL
#if
if (calificacion >= 70)
  puts "Aprobado"
end

#until
iterador = 0 
until iterador > 5
  puts "el número es: "+String(iterador)
  iterador += 1
end

#case
edad = 5 case edad when 0 .. 2
  puts "Bebe" when 3 .. 12
  puts "Niño" when 13 .. 18
  puts "Adolescente" else
  puts "Adulto" end
  


#FUNCION
def IMC(peso,altura) 
  peso/altura**2
end

#MANEJO DE ARCHIVOS 
#lectura
content = File.read("contenido.txt") 
lines = content.split("\n")

lines.each do |line|
  puts line 
end

#escritura
File.write("cuento.txt", "Había una vez ...")

File.open("cuento.txt", "w") do |file| 
  file.write("Había una vez ...")
end


