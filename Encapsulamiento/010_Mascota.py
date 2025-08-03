class Mascota:
  def __init__(self,nombre,tipo_animal,edad):
      self.__nombre = nombre
      self.__tipo_animal=tipo_animal
      self.__edad = edad
  def mostrar_info(self):
      print(f"el nombre de tu mascota es |{self.__nombre}|")
      print(f"su animal preciado es un |{self.__tipo_animal}|")
      print(f"la edad del amor de su vida es |{self.__edad}|")
  def cumplir_años(self):
        self.__edad +=1
        print(f"¡Feliz cumpleaños, {self.__nombre}! Ahora tienes {self.__edad} años.")
  def emitir_sonidos(self):
        if self.__tipo_animal.lower() == "gato":
         print(f"su animal es {self.__tipo_animal} y emite un Miau miau 🐱")
        elif self.__tipo_animal.lower() == "perro":
         print(f"su animal es {self.__tipo_animal} y emite un Guau guau 🐶")
        else:
         print(f"su animal es {self.__tipo_animal} y emite un sonido especial 🐾")
#informacion 
informacion = ["Sammy", "gato", 2]
Mascota1 = Mascota(informacion[0], informacion[1], informacion[2])

#Mostrar
Mascota1.mostrar_info()
Mascota1.cumplir_años()
Mascota1.emitir_sonidos()