class ciclo:
	
	def _init_(self,num=10):
		self.numero=num
		
	def usowhile (self):
		print("dentro de clase",self.numero)
		LETRA=""
		while LETRA not in ("a","e","i","o","u"):
			LETRA =input("Ingrese una vocal: ").lower()
			#caracter= caracter.lower()
			
		print("Excelente, es la letra correcta: {} si es vocal ".format(LETRA))
ciclo1= ciclo()
print("Fuera de la clase", ciclo1.numero)
print(ciclo1.usowhile( ))
