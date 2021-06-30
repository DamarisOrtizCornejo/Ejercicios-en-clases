class ciclo:

    def _init_(self,numero=10):
        self.numero=numero
        
            
    def usowhile (self):
        print("dentro de clase",self.numero)
        LETRA=""
        while LETRA not in ("a","e","i","o","u"):
            LETRA =input("ingrese una vocal: ").lower()
            #caracter= caracter.lower()

        print("Exelente, es la letra correcta:{} si es vocal".format(LETRA))
ciclo1= ciclo()
print(ciclo1.usowhile())
print("fuera de la clase",ciclo1.numero)