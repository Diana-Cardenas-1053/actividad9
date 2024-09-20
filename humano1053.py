print("ACTIVIDAD 9 clase humano")
print("Diana Mabel Cardenas Castillo mat: 22308051281053")
#zona de class
class humano1053:
    #zona de atributos dentro de la clase
    edad=0
    peso=0
    FechaDeNacimiento=0
    estatura=0
    ColorDeCabello=0
    
    #zona de funciones dentro de la clase
    def correr1053(self,n):
        print(f"{n} esta corriendo")
        
    def reir1053(self,n):
        print(f"{n} esta riendo")
        
    def orar1053(self,n):
        print(f"{n} esta orando")
        
    def amor1053(self,n):
        print(f"{n} esta enamorada de Fer")
    
    def amorr1053(self,n):
        print(f"{n} esta enamorado de Mabel")
        
        
#zona de creacion de objetos
mabel=humano1053()
fer=humano1053()

#zona de usando objetos
print("resultados para Mabel")
mabel.edad=17
mabel.peso=45
mabel.FechaDeNacimiento="14 de febrero 2007"
mabel.estatura=1.59
mabel.ColorDeCabello="verde"
print(f"edad: {mabel.edad}")
print(f"peso: {mabel.peso}")
print(f"fecha de nacimiento: {mabel.FechaDeNacimiento}")
print(f"estatura: {mabel.estatura}")
print(f"Color de cebello: {mabel.ColorDeCabello}")
mabel.correr1053("Mabel")
mabel.reir1053("Mabel")
mabel.orar1053("Mabel")
mabel.amor1053("Mabel")

print("resultados para Fer")
fer.edad=24
fer.peso=70
fer.FechaDeNacimiento="15 de octubre del 2000"
fer.estatura=1.70
fer.ColorDeCabello="cafe oscuro"
print(f"edad: {fer.edad}")
print(f"peso: {fer.peso}")
print(f"fecha de nacimiento: {fer.FechaDeNacimiento}")
print(f"estatura: {fer.estatura}")
print(f"Color de cebello: {fer.ColorDeCabello}")
fer.correr1053("Fer")
fer.reir1053("Fer")
fer.orar1053("Fer")
fer.amorr1053("Fer")