class Condicion:
             def _init_(self, num1, num2):
                	self.numero1=num1
                	self.numero2=num2
                	numero = self.numero1+self.numero2
                	self.numero3=numero
                	
              def condicion(self):
                	if self.numero1==self.numero2:
                		print("numero1: {} y numero2: {} son iguales".format(self.numero1,self.numeto2))
                	elif self.numero1< self.numero3:
                		print("numero1: {} es menor numero3: {}".format(self.numero3))
                	else:
                		print("No es igual")
                	print("Fin drl metodo")

lista= [8,18]
condi1 = Condicion(lista)
print(condi1.nemero3)
print(condi1.condicion())