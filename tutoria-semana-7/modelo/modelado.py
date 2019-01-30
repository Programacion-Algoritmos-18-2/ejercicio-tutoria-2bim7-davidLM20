class Persona(): # clase para crear el objeto

	def __init__(self, nombre, apellido, edad): # se crea los atributos golabales de la clase

		self.nombre = nombre
		self.apellido = apellido
		self.edad = int(edad) # se tranforma en entero la variable edad

	# metodos para agregar el nombre apellido y edad	
	def setNombre(self, nombre): 
		self.nombre = nombre

	def setApellido(self, apellido):
		self.apellido = apellido

	def setEdad(self,edad):
		self.edad = edad

	# metodos para obtener o devolber la informacion
	def getNombre(self):
		return self.nombre 

	def getApellido(self):
		return self.apellido

	def getEdad(self):
		return self.edad

	def __str__(self):
		
		cadena = "%s %s %d" % (self.getNombre(), self.getApellido(), self.getEdad())
		return cadena
		